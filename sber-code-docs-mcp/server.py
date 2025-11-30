import os
import faiss
from mcp.server.fastmcp import FastMCP
from llama_index.core import StorageContext, load_index_from_storage, Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.llms import MockLLM
from llama_index.vector_stores.faiss import FaissVectorStore

# ═══════════════════════════════════════════════════════════════════
# НАСТРОЙКИ
# ═══════════════════════════════════════════════════════════════════

Settings.llm = MockLLM()
Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

# Определяем базовую директорию (где лежит server.py)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

STORAGE_DIR = os.path.join(BASE_DIR, "storage")
FAISS_INDEX_PATH = os.path.join(BASE_DIR, "faiss_index.bin")
DOCS_DIR = os.path.join(BASE_DIR, "docs")

# ═══════════════════════════════════════════════════════════════════
# ЗАГРУЗКА ИНДЕКСА
# ═══════════════════════════════════════════════════════════════════

if not os.path.exists(STORAGE_DIR):
    raise RuntimeError(
        f"Хранилище не найдено: {STORAGE_DIR}\n"
        "Сначала запустите: python builder.py"
    )

if not os.path.exists(FAISS_INDEX_PATH):
    raise RuntimeError(
        f"FAISS индекс не найден: {FAISS_INDEX_PATH}\n"
        "Сначала запустите: python builder.py"
    )

# Загружаем FAISS индекс из файла (НЕ создаём новый пустой!)
faiss_index = faiss.read_index(FAISS_INDEX_PATH)
vector_store = FaissVectorStore(faiss_index=faiss_index)

# Загружаем метаданные LlamaIndex
storage_context = StorageContext.from_defaults(
    persist_dir=STORAGE_DIR,
    vector_store=vector_store
)
index = load_index_from_storage(storage_context)

# Создаём retriever для поиска
retriever = index.as_retriever(similarity_top_k=7)

# ═══════════════════════════════════════════════════════════════════
# MCP СЕРВЕР
# ═══════════════════════════════════════════════════════════════════

mcp = FastMCP("SberDocs")


@mcp.tool()
def search_documentation(query: str, category: str = None, top_k: int = 7) -> str:
    """
    Поиск по документации SberSalute Code.

    Передайте ключевые слова или вопрос на русском или английском языке.

    Параметры:
    - query: поисковый запрос
    - category: фильтр по категории (например: 'js-api', 'nlp', 'project', 'root')
    - top_k: количество результатов (по умолчанию 7, максимум 20)

    Примеры запросов:
    - search_documentation("inference") - поиск везде
    - search_documentation("inference", category="nlp") - поиск только в NLP
    - search_documentation("состояние", top_k=10) - больше результатов
    """
    try:
        # Ограничиваем top_k
        top_k = min(max(1, top_k), 20)

        # Создаём retriever с нужным количеством результатов
        # Если есть фильтр по категории, запрашиваем больше для последующей фильтрации
        fetch_k = top_k * 3 if category else top_k
        custom_retriever = index.as_retriever(similarity_top_k=fetch_k)

        nodes = custom_retriever.retrieve(query)

        if not nodes:
            return "Не найдено подходящих фрагментов по запросу."

        # Фильтруем по категории если указана
        if category:
            category_lower = category.lower().replace("\\", "/")
            filtered_nodes = []
            for node in nodes:
                node_category = node.metadata.get("category", "").lower().replace("\\", "/")
                # Проверяем точное совпадение или начало пути
                if node_category == category_lower or node_category.startswith(category_lower + "/"):
                    filtered_nodes.append(node)
            nodes = filtered_nodes[:top_k]
        else:
            nodes = nodes[:top_k]

        if not nodes:
            return f"Не найдено результатов в категории '{category}'."

        results = []
        for i, node in enumerate(nodes, 1):
            file_path = node.metadata.get("file_path", "Неизвестный файл")
            node_category = node.metadata.get("category", "")
            score = f"{node.score:.3f}" if node.score else "N/A"
            text_content = node.node.get_content()

            results.append(
                f"─── Результат {i} ───\n"
                f"Файл: {file_path}\n"
                f"Категория: {node_category}\n"
                f"Релевантность: {score}\n"
                f"Содержимое:\n{text_content}\n"
            )

        return "\n".join(results)

    except Exception as e:
        return f"Ошибка при поиске: {e}"


@mcp.tool()
def read_full_file(file_path: str) -> str:
    """
    Прочитать файл документации целиком.

    Укажите путь относительно папки docs/, например:
    - 'js-api/services/caila/inference.md'
    - 'nlp/api/overview.md'
    - 'root/current-datetime.md' (для файлов в корне docs/)

    Функция защищена от выхода за пределы папки docs/.
    """
    try:
        # Убираем "root/" если указано (файлы в корне docs/)
        if file_path.startswith("root/"):
            file_path = file_path[5:]  # len("root/") = 5

        base = os.path.abspath(DOCS_DIR)
        abs_path = os.path.abspath(os.path.join(base, file_path))

        # Защита от path traversal
        if not abs_path.startswith(base):
            return "Ошибка: доступ за пределы папки docs/ запрещён."

        if not os.path.exists(abs_path):
            return f"Ошибка: файл не найден: {file_path}"

        with open(abs_path, "r", encoding="utf-8") as f:
            content = f.read()

        return f"─── Файл: {file_path} ───\n\n{content}"

    except Exception as e:
        return f"Ошибка при чтении файла: {e}"


@mcp.tool()
def list_categories() -> str:
    """
    Показать список категорий (разделов) документации.

    Возвращает структуру папок внутри docs/ с количеством файлов в каждой.
    Полезно для навигации по документации.
    """
    try:
        categories = {}

        for root, dirs, files in os.walk(DOCS_DIR):
            md_files = [f for f in files if f.endswith(".md")]
            if md_files:
                rel_path = os.path.relpath(root, DOCS_DIR)
                if rel_path == ".":
                    rel_path = "root"
                categories[rel_path] = {
                    "count": len(md_files),
                    "files": md_files[:5]  # Первые 5 файлов для примера
                }

        if not categories:
            return "Категории не найдены. Проверьте наличие .md файлов в папке docs/"

        result = ["─── Категории документации ───\n"]

        for cat, info in sorted(categories.items()):
            result.append(f"📁 {cat} ({info['count']} файлов)")
            for f in info["files"]:
                result.append(f"   └─ {f}")
            if info["count"] > 5:
                result.append(f"   └─ ... и ещё {info['count'] - 5} файлов")
            result.append("")

        return "\n".join(result)

    except Exception as e:
        return f"Ошибка при получении категорий: {e}"


@mcp.tool()
def find_file_by_name(filename: str) -> str:
    """
    Поиск файлов документации по имени.

    Ищет все файлы, содержащие указанную подстроку в имени.
    Поиск регистронезависимый.

    Примеры:
    - find_file_by_name("inference") - найдёт inference.md, simple-inference.md
    - find_file_by_name("overview") - найдёт все overview.md файлы
    """
    try:
        filename_lower = filename.lower()
        found_files = []

        for root, dirs, files in os.walk(DOCS_DIR):
            for f in files:
                if f.endswith(".md") and filename_lower in f.lower():
                    rel_path = os.path.relpath(root, DOCS_DIR)
                    if rel_path == ".":
                        category = "root"
                        full_path = f
                    else:
                        category = rel_path.replace(os.sep, "/")
                        full_path = f"{category}/{f}"

                    found_files.append({
                        "file": f,
                        "path": full_path,
                        "category": category
                    })

        if not found_files:
            return f"Файлы с '{filename}' в имени не найдены."

        result = [f"─── Найдено файлов: {len(found_files)} ───\n"]

        for item in sorted(found_files, key=lambda x: x["path"]):
            result.append(f"📄 {item['file']}")
            result.append(f"   Путь: {item['path']}")
            result.append(f"   Категория: {item['category']}")
            result.append("")

        return "\n".join(result)

    except Exception as e:
        return f"Ошибка при поиске файла: {e}"


@mcp.tool()
def list_files_in_category(category: str) -> str:
    """
    Показать все файлы в указанной категории.

    Параметры:
    - category: название категории (например: 'js-api', 'nlp/api', 'root')

    Возвращает полный список файлов с первыми строками (заголовками) каждого файла.
    """
    try:
        # Нормализуем путь
        if category == "root":
            target_dir = DOCS_DIR
        else:
            category = category.replace("/", os.sep)
            target_dir = os.path.join(DOCS_DIR, category)

        if not os.path.exists(target_dir):
            return f"Категория '{category}' не найдена."

        if not os.path.isdir(target_dir):
            return f"'{category}' не является категорией (папкой)."

        files_info = []

        for f in sorted(os.listdir(target_dir)):
            if f.endswith(".md"):
                file_path = os.path.join(target_dir, f)
                # Читаем первую непустую строку (заголовок)
                title = ""
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        for line in file:
                            line = line.strip()
                            if line and line.startswith("#"):
                                title = line.lstrip("#").strip()
                                break
                            elif line and not line.startswith("["):
                                title = line[:80]
                                break
                except:
                    title = "(не удалось прочитать)"

                files_info.append({
                    "file": f,
                    "title": title or "(без заголовка)"
                })

        if not files_info:
            return f"В категории '{category}' нет .md файлов."

        result = [f"─── Файлы в категории '{category}' ({len(files_info)}) ───\n"]

        for item in files_info:
            result.append(f"📄 {item['file']}")
            result.append(f"   {item['title']}")
            result.append("")

        return "\n".join(result)

    except Exception as e:
        return f"Ошибка при получении списка файлов: {e}"


@mcp.tool()
def get_table_of_contents(file_path: str) -> str:
    """
    Получить оглавление (заголовки) файла документации.

    Извлекает все заголовки (#, ##, ###) для быстрой навигации по документу.

    Параметры:
    - file_path: путь к файлу относительно docs/ (например: 'nlp/api/inference.md')
                 для файлов в корне используйте 'root/filename.md'
    """
    try:
        # Убираем "root/" если указано
        if file_path.startswith("root/"):
            file_path = file_path[5:]

        base = os.path.abspath(DOCS_DIR)
        abs_path = os.path.abspath(os.path.join(base, file_path))

        # Защита от path traversal
        if not abs_path.startswith(base):
            return "Ошибка: доступ за пределы папки docs/ запрещён."

        if not os.path.exists(abs_path):
            return f"Ошибка: файл не найден: {file_path}"

        headings = []
        with open(abs_path, "r", encoding="utf-8") as f:
            for line_num, line in enumerate(f, 1):
                line = line.rstrip()
                if line.startswith("#"):
                    # Подсчитываем уровень заголовка
                    level = 0
                    for char in line:
                        if char == "#":
                            level += 1
                        else:
                            break
                    title = line[level:].strip()
                    if title:
                        indent = "  " * (level - 1)
                        headings.append(f"{indent}• {title} (строка {line_num})")

        if not headings:
            return f"В файле '{file_path}' не найдено заголовков."

        result = [f"─── Оглавление: {file_path} ───\n"]
        result.extend(headings)

        return "\n".join(result)

    except Exception as e:
        return f"Ошибка при чтении оглавления: {e}"


@mcp.tool()
def search_exact(text: str, category: str = None) -> str:
    """
    Точный текстовый поиск (grep-подобный).

    Ищет точное вхождение текста во всех файлах документации.
    Полезно для поиска конкретных терминов, URL, примеров кода.

    Параметры:
    - text: текст для поиска (регистронезависимый)
    - category: опционально, искать только в указанной категории

    Примеры:
    - search_exact("$jsapi") - найти использование $jsapi
    - search_exact("smartapp-code.sberdevices.ru") - найти URL
    """
    try:
        text_lower = text.lower()
        results = []
        max_results = 20

        # Определяем директорию для поиска
        if category:
            if category == "root":
                search_dirs = [DOCS_DIR]
            else:
                search_dirs = [os.path.join(DOCS_DIR, category.replace("/", os.sep))]
        else:
            search_dirs = [DOCS_DIR]

        for search_dir in search_dirs:
            if not os.path.exists(search_dir):
                continue

            for root, dirs, files in os.walk(search_dir):
                if len(results) >= max_results:
                    break

                for f in files:
                    if len(results) >= max_results:
                        break

                    if not f.endswith(".md"):
                        continue

                    file_path = os.path.join(root, f)
                    rel_path = os.path.relpath(file_path, DOCS_DIR).replace(os.sep, "/")

                    try:
                        with open(file_path, "r", encoding="utf-8") as file:
                            for line_num, line in enumerate(file, 1):
                                if text_lower in line.lower():
                                    # Обрезаем длинные строки
                                    line_preview = line.strip()
                                    if len(line_preview) > 100:
                                        # Находим позицию совпадения и показываем контекст
                                        pos = line.lower().find(text_lower)
                                        start = max(0, pos - 30)
                                        end = min(len(line_preview), pos + len(text) + 30)
                                        line_preview = "..." + line_preview[start:end] + "..."

                                    results.append({
                                        "file": rel_path,
                                        "line": line_num,
                                        "content": line_preview
                                    })

                                    if len(results) >= max_results:
                                        break
                    except:
                        continue

        if not results:
            msg = f"Текст '{text}' не найден"
            if category:
                msg += f" в категории '{category}'"
            return msg + "."

        output = [f"─── Найдено совпадений: {len(results)} ───\n"]

        for r in results:
            output.append(f"📍 {r['file']}:{r['line']}")
            output.append(f"   {r['content']}")
            output.append("")

        if len(results) >= max_results:
            output.append(f"(показаны первые {max_results} результатов)")

        return "\n".join(output)

    except Exception as e:
        return f"Ошибка при поиске: {e}"


# ═══════════════════════════════════════════════════════════════════
# ЗАПУСК
# ═══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    # MCP-спецификация: НЕ использовать print() — это ломает JSON-RPC
    # Все сообщения должны идти в stderr или в файл
    mcp.run()
