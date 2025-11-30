"""
MCP-сервер для семантического поиска по документации SaluteBot.
"""

import re
from pathlib import Path
from typing import Optional

import faiss
import numpy as np
from fastmcp import FastMCP
from llama_index.core import StorageContext, load_index_from_storage
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

BASE_DIR = Path(__file__).parent
DOCS_DIR = BASE_DIR / "docs"
STORAGE_DIR = BASE_DIR / "storage"
FAISS_INDEX_PATH = BASE_DIR / "faiss_index.bin"

EMBED_MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

mcp = FastMCP("SaluteBotDocs")

# Глобальные переменные для ленивой загрузки
_embed_model = None
_faiss_index = None
_llama_index = None
_nodes = None


def get_embed_model():
    global _embed_model
    if _embed_model is None:
        _embed_model = HuggingFaceEmbedding(model_name=EMBED_MODEL_NAME)
    return _embed_model


def get_faiss_index():
    global _faiss_index
    if _faiss_index is None:
        _faiss_index = faiss.read_index(str(FAISS_INDEX_PATH))
    return _faiss_index


def get_llama_index():
    global _llama_index, _nodes
    if _llama_index is None:
        storage_context = StorageContext.from_defaults(persist_dir=str(STORAGE_DIR))
        _llama_index = load_index_from_storage(
            storage_context,
            embed_model=get_embed_model(),
        )
        _nodes = list(_llama_index.docstore.docs.values())
    return _llama_index, _nodes


def get_category(file_path: Path) -> str:
    """Извлекает категорию из пути файла."""
    try:
        rel_path = file_path.relative_to(DOCS_DIR)
        parts = rel_path.parts
        if len(parts) == 1:
            return "root"
        return "/".join(parts[:-1])
    except ValueError:
        return "unknown"


def get_all_md_files() -> list[Path]:
    """Возвращает все markdown файлы в docs/."""
    return list(DOCS_DIR.rglob("*.md"))


def get_file_title(file_path: Path) -> str:
    """Извлекает заголовок из markdown файла."""
    try:
        content = file_path.read_text(encoding="utf-8")
        for line in content.split("\n"):
            line = line.strip()
            if line.startswith("# "):
                return line[2:].strip()
        return file_path.stem
    except Exception:
        return file_path.stem


@mcp.tool()
def search_documentation(
    query: str,
    category: Optional[str] = None,
    top_k: int = 7,
) -> str:
    """
    Семантический поиск по документации SaluteBot.

    Args:
        query: Поисковый запрос (русский/английский)
        category: Фильтр по категории (например: bot-development, scenario)
        top_k: Количество результатов (1-20, по умолчанию 7)
    """
    top_k = max(1, min(20, top_k))

    embed_model = get_embed_model()
    faiss_index = get_faiss_index()
    _, nodes = get_llama_index()

    # Получаем эмбеддинг запроса
    query_emb = np.array([embed_model.get_text_embedding(query)], dtype="float32")
    faiss.normalize_L2(query_emb)

    # Поиск в FAISS (берём больше, если есть фильтр по категории)
    search_k = top_k * 5 if category else top_k
    scores, indices = faiss_index.search(query_emb, min(search_k, len(nodes)))

    results = []
    for score, idx in zip(scores[0], indices[0]):
        if idx < 0 or idx >= len(nodes):
            continue

        node = nodes[idx]
        node_category = node.metadata.get("category", "")
        rel_path = node.metadata.get("rel_path", "")

        # Фильтр по категории
        if category and not node_category.startswith(category):
            continue

        content = node.get_content()
        # Обрезаем контент для отображения
        preview = content[:500] + "..." if len(content) > 500 else content

        results.append({
            "score": float(score),
            "file": rel_path,
            "category": node_category,
            "preview": preview,
        })

        if len(results) >= top_k:
            break

    if not results:
        return "Ничего не найдено."

    output = []
    for i, r in enumerate(results, 1):
        output.append(
            f"## {i}. {r['file']} (score: {r['score']:.3f})\n"
            f"Категория: {r['category']}\n\n"
            f"{r['preview']}\n"
        )

    return "\n---\n".join(output)


@mcp.tool()
def read_full_file(file_path: str) -> str:
    """
    Чтение файла документации целиком.

    Args:
        file_path: Путь относительно docs/ (например: scenario/blocks/conditions.md)
                   Для корневых файлов: root/overview.md
    """
    # Обработка root/ префикса
    if file_path.startswith("root/"):
        file_path = file_path[5:]

    full_path = DOCS_DIR / file_path

    if not full_path.exists():
        return f"Файл не найден: {file_path}"

    if not full_path.is_file():
        return f"Это не файл: {file_path}"

    try:
        content = full_path.read_text(encoding="utf-8")
        return f"# Файл: {file_path}\n\n{content}"
    except Exception as e:
        return f"Ошибка чтения файла: {e}"


@mcp.tool()
def list_categories() -> str:
    """
    Список всех категорий документации с количеством файлов.
    """
    categories = {}
    for f in get_all_md_files():
        cat = get_category(f)
        categories[cat] = categories.get(cat, 0) + 1

    # Сортировка по количеству файлов
    sorted_cats = sorted(categories.items(), key=lambda x: -x[1])

    output = ["# Категории документации SaluteBot\n"]
    output.append("| Категория | Файлов |")
    output.append("|-----------|--------|")
    for cat, count in sorted_cats:
        output.append(f"| {cat} | {count} |")

    return "\n".join(output)


@mcp.tool()
def find_file_by_name(filename: str) -> str:
    """
    Поиск файлов по имени (регистронезависимый).

    Args:
        filename: Подстрока для поиска (например: intent, conditions)
    """
    filename_lower = filename.lower()
    matches = []

    for f in get_all_md_files():
        if filename_lower in f.name.lower():
            rel_path = f.relative_to(DOCS_DIR)
            title = get_file_title(f)
            matches.append({
                "path": str(rel_path),
                "title": title,
                "category": get_category(f),
            })

    if not matches:
        return f"Файлы с '{filename}' не найдены."

    output = [f"# Найдено файлов: {len(matches)}\n"]
    for m in matches:
        output.append(f"- **{m['path']}** — {m['title']} (категория: {m['category']})")

    return "\n".join(output)


@mcp.tool()
def list_files_in_category(category: str) -> str:
    """
    Список всех файлов в категории с заголовками.

    Args:
        category: Название категории (например: bot-development/entities)
    """
    matches = []

    for f in get_all_md_files():
        file_cat = get_category(f)
        if file_cat == category or file_cat.startswith(category + "/"):
            rel_path = f.relative_to(DOCS_DIR)
            title = get_file_title(f)
            matches.append({
                "path": str(rel_path),
                "title": title,
            })

    if not matches:
        return f"Категория '{category}' не найдена или пуста."

    # Сортировка по пути
    matches.sort(key=lambda x: x["path"])

    output = [f"# Файлы в категории: {category}\n"]
    for m in matches:
        output.append(f"- **{m['path']}** — {m['title']}")

    return "\n".join(output)


@mcp.tool()
def get_table_of_contents(file_path: str) -> str:
    """
    Оглавление файла (все заголовки #, ##, ###).

    Args:
        file_path: Путь к файлу относительно docs/
    """
    # Обработка root/ префикса
    if file_path.startswith("root/"):
        file_path = file_path[5:]

    full_path = DOCS_DIR / file_path

    if not full_path.exists():
        return f"Файл не найден: {file_path}"

    try:
        content = full_path.read_text(encoding="utf-8")
    except Exception as e:
        return f"Ошибка чтения файла: {e}"

    headings = []
    for line in content.split("\n"):
        line = line.strip()
        if line.startswith("#"):
            # Считаем уровень заголовка
            level = 0
            for ch in line:
                if ch == "#":
                    level += 1
                else:
                    break
            if level <= 3:
                title = line[level:].strip()
                indent = "  " * (level - 1)
                headings.append(f"{indent}- {title}")

    if not headings:
        return f"Заголовки не найдены в файле: {file_path}"

    output = [f"# Оглавление: {file_path}\n"]
    output.extend(headings)

    return "\n".join(output)


@mcp.tool()
def search_exact(text: str, category: Optional[str] = None) -> str:
    """
    Точный текстовый поиск (grep-подобный).

    Args:
        text: Искомый текст
        category: Опционально, фильтр по категории
    """
    text_lower = text.lower()
    results = []

    for f in get_all_md_files():
        file_cat = get_category(f)

        # Фильтр по категории
        if category and not file_cat.startswith(category):
            continue

        try:
            content = f.read_text(encoding="utf-8")
        except Exception:
            continue

        if text_lower in content.lower():
            rel_path = f.relative_to(DOCS_DIR)

            # Находим строки с совпадениями
            matches = []
            for i, line in enumerate(content.split("\n"), 1):
                if text_lower in line.lower():
                    matches.append(f"  L{i}: {line.strip()[:100]}")
                    if len(matches) >= 3:  # Максимум 3 совпадения на файл
                        break

            results.append({
                "path": str(rel_path),
                "category": file_cat,
                "matches": matches,
            })

            if len(results) >= 20:  # Максимум 20 файлов
                break

    if not results:
        return f"Текст '{text}' не найден."

    output = [f"# Найдено в {len(results)} файлах\n"]
    for r in results:
        output.append(f"## {r['path']} (категория: {r['category']})")
        output.extend(r["matches"])
        output.append("")

    return "\n".join(output)


if __name__ == "__main__":
    mcp.run()
