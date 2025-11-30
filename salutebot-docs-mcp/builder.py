"""
Скрипт построения FAISS индекса для документации SaluteBot.
Запуск: python builder.py
"""

import os
import shutil
from pathlib import Path

import faiss
from llama_index.core import (
    SimpleDirectoryReader,
    StorageContext,
    VectorStoreIndex,
)
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.vector_stores import SimpleVectorStore

BASE_DIR = Path(__file__).parent
DOCS_DIR = BASE_DIR / "docs"
STORAGE_DIR = BASE_DIR / "storage"
FAISS_INDEX_PATH = BASE_DIR / "faiss_index.bin"

EMBED_MODEL_NAME = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
EMBED_DIM = 384


def get_category(file_path: str) -> str:
    """Извлекает категорию из пути файла."""
    rel_path = Path(file_path).relative_to(DOCS_DIR)
    parts = rel_path.parts
    if len(parts) == 1:
        return "root"
    return "/".join(parts[:-1])


def build_index():
    print(f"Загрузка эмбеддинг-модели: {EMBED_MODEL_NAME}")
    embed_model = HuggingFaceEmbedding(model_name=EMBED_MODEL_NAME)

    print(f"Чтение документов из: {DOCS_DIR}")
    reader = SimpleDirectoryReader(
        input_dir=str(DOCS_DIR),
        recursive=True,
        required_exts=[".md"],
    )
    documents = reader.load_data()
    print(f"Загружено документов: {len(documents)}")

    # Добавляем метаданные категории
    for doc in documents:
        file_path = doc.metadata.get("file_path", "")
        doc.metadata["category"] = get_category(file_path)
        # Относительный путь для удобства
        try:
            doc.metadata["rel_path"] = str(Path(file_path).relative_to(DOCS_DIR))
        except ValueError:
            doc.metadata["rel_path"] = file_path

    print("Разбиение на чанки...")
    splitter = SentenceSplitter(chunk_size=512, chunk_overlap=50)
    nodes = splitter.get_nodes_from_documents(documents)
    print(f"Создано чанков: {len(nodes)}")

    print("Создание эмбеддингов и индекса...")
    # Очистка старого storage
    if STORAGE_DIR.exists():
        shutil.rmtree(STORAGE_DIR)
    STORAGE_DIR.mkdir(parents=True, exist_ok=True)

    # Создаем индекс с LlamaIndex
    storage_context = StorageContext.from_defaults()
    index = VectorStoreIndex(
        nodes,
        embed_model=embed_model,
        storage_context=storage_context,
        show_progress=True,
    )

    # Сохраняем LlamaIndex storage
    index.storage_context.persist(persist_dir=str(STORAGE_DIR))
    print(f"LlamaIndex storage сохранен в: {STORAGE_DIR}")

    # Создаем и сохраняем FAISS индекс
    print("Построение FAISS индекса...")
    embeddings = []
    for node in nodes:
        emb = embed_model.get_text_embedding(node.get_content())
        embeddings.append(emb)

    import numpy as np
    embeddings_np = np.array(embeddings, dtype="float32")

    faiss_index = faiss.IndexFlatIP(EMBED_DIM)  # Inner Product для косинусного сходства
    faiss.normalize_L2(embeddings_np)  # Нормализация для косинусного сходства
    faiss_index.add(embeddings_np)

    faiss.write_index(faiss_index, str(FAISS_INDEX_PATH))
    print(f"FAISS индекс сохранен в: {FAISS_INDEX_PATH}")

    print("Готово!")


if __name__ == "__main__":
    build_index()
