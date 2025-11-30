import os
import shutil
import faiss
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, Settings, StorageContext
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import MarkdownNodeParser
from llama_index.core.llms import MockLLM
from llama_index.vector_stores.faiss import FaissVectorStore

# ═══════════════════════════════════════════════════════════════════
# НАСТРОЙКИ
# ═══════════════════════════════════════════════════════════════════

# Отключаем генеративную модель — RAG работает только как поисковик
Settings.llm = MockLLM()

# Модель эмбеддингов: мультиязычная, лёгкая, работает на CPU
Settings.embed_model = HuggingFaceEmbedding(
    model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

DOCS_DIR = "./docs"           # Папка с Markdown-документацией
STORAGE_DIR = "./storage"     # Папка для метаданных LlamaIndex
FAISS_INDEX_PATH = "./faiss_index.bin"  # Файл FAISS индекса

# Размерность эмбеддингов MiniLM-L12-v2
EMBEDDING_DIM = 384


# ═══════════════════════════════════════════════════════════════════
# ФУНКЦИИ
# ═══════════════════════════════════════════════════════════════════

def get_file_metadata(file_path: str) -> dict:
    """
    Формируем метаданные для каждого файла:
    - file_path: относительный путь к файлу от docs/
    - file_name: имя файла
    - category: категория (подпапка относительно docs/)
    """
    abs_file = os.path.abspath(file_path)
    abs_docs = os.path.abspath(DOCS_DIR)

    # Относительный путь к файлу от docs/
    rel_path = os.path.relpath(abs_file, abs_docs)

    # Категория = директория файла (или "root" для корневых)
    dir_part = os.path.dirname(rel_path)
    category = dir_part.replace(os.sep, "/") if dir_part else "root"

    return {
        "file_path": rel_path.replace(os.sep, "/"),  # Используем / для консистентности
        "file_name": os.path.basename(file_path),
        "category": category
    }


def build_index():
    """Построение векторного индекса из Markdown-файлов."""

    print("=" * 60)
    print("ПОСТРОЕНИЕ ИНДЕКСА ДОКУМЕНТАЦИИ")
    print("=" * 60)

    # 1. Очистка старого хранилища
    if os.path.exists(STORAGE_DIR):
        print(f"Удаление старого хранилища: {STORAGE_DIR}")
        shutil.rmtree(STORAGE_DIR)

    if os.path.exists(FAISS_INDEX_PATH):
        print(f"Удаление старого FAISS индекса: {FAISS_INDEX_PATH}")
        os.remove(FAISS_INDEX_PATH)

    # 2. Чтение документов
    print(f"\nЧтение документов из: {DOCS_DIR}")
    reader = SimpleDirectoryReader(
        input_dir=DOCS_DIR,
        recursive=True,
        required_exts=[".md"],
        file_metadata=get_file_metadata
    )
    documents = reader.load_data()
    print(f"Загружено документов: {len(documents)}")

    # 3. Настройка парсера Markdown
    parser = MarkdownNodeParser()

    # 4. Создание FAISS индекса
    print("\nСоздание FAISS индекса...")
    faiss_index = faiss.IndexFlatL2(EMBEDDING_DIM)
    vector_store = FaissVectorStore(faiss_index=faiss_index)

    # 5. Создание контекста хранилища
    storage_context = StorageContext.from_defaults(vector_store=vector_store)

    # 6. Построение индекса
    print("Индексация документов (это может занять несколько минут)...")
    index = VectorStoreIndex.from_documents(
        documents,
        transformations=[parser],
        storage_context=storage_context,
        show_progress=True
    )

    # 7. Сохранение метаданных LlamaIndex
    print(f"\nСохранение метаданных в: {STORAGE_DIR}")
    index.storage_context.persist(persist_dir=STORAGE_DIR)

    # 8. Сохранение FAISS индекса отдельно
    print(f"Сохранение FAISS индекса в: {FAISS_INDEX_PATH}")
    faiss.write_index(faiss_index, FAISS_INDEX_PATH)

    print("\n" + "=" * 60)
    print("ИНДЕКСАЦИЯ ЗАВЕРШЕНА УСПЕШНО")
    print("=" * 60)

    # Статистика
    categories = set()
    for doc in documents:
        cat = doc.metadata.get("category", "unknown")
        categories.add(cat)

    print(f"\nСтатистика:")
    print(f"  - Документов: {len(documents)}")
    print(f"  - Категорий: {len(categories)}")
    print(f"  - Размер FAISS индекса: {faiss_index.ntotal} векторов")


if __name__ == "__main__":
    build_index()
