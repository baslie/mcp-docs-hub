# MCP Docs Hub

Коллекция MCP серверов для семантического поиска по документациям различных платформ. Серверы предоставляют инструменты для работы с документацией через Model Context Protocol в Claude Code и других совместимых клиентах.

## Содержимое репозитория

| Сервер | Описание | Документация |
|--------|----------|--------------|
| [jivo-docs-mcp](./jivo-docs-mcp/) | Документация Jivo API — виджет чата, webhooks, Chat API, Bot API | 6 файлов |
| [salutebot-docs-mcp](./salutebot-docs-mcp/) | Документация SaluteBot — платформа для создания чат-ботов | 147 файлов |
| [sber-code-docs-mcp](./sber-code-docs-mcp/) | Документация SberSalute Code — SmartApp, JS API, NLP | 179 файлов |

## Быстрый старт

### 1. Клонирование репозитория

```bash
git clone https://github.com/baslie/mcp-docs-hub.git
cd mcp-docs-hub
```

### 2. Настройка сервера (на примере jivo-docs-mcp)

```bash
cd jivo-docs-mcp

# Создание виртуального окружения
python -m venv venv

# Активация (Windows)
venv\Scripts\activate

# Активация (Linux/macOS)
source venv/bin/activate

# Установка зависимостей
pip install -r requirements.txt
```

### 3. Создание индексов

**Важно:** Файлы индексов (`faiss_index.bin`, `storage/`) не включены в репозиторий для уменьшения размера. После клонирования необходимо создать их:

```bash
python builder.py
```

Скрипт создаст векторный индекс FAISS для семантического поиска по документации.

### 4. Подключение к Claude Code

Добавьте сервер в конфигурацию MCP (`.mcp.json`):

```json
{
  "mcpServers": {
    "jivo-docs": {
      "command": "path/to/venv/Scripts/python.exe",
      "args": ["path/to/jivo-docs-mcp/server.py"]
    }
  }
}
```

## Структура каждого сервера

```
<server-name>/
├── server.py           # FastMCP сервер
├── builder.py          # Скрипт для создания индексов
├── requirements.txt    # Python зависимости
├── README.md           # Документация сервера
└── docs/               # Markdown файлы документации
```

## Доступные инструменты MCP

Каждый сервер предоставляет следующие инструменты:

- `search_documentation(query, category?, top_k?)` — семантический поиск
- `read_full_file(file_path)` — чтение файла целиком
- `list_categories()` — список категорий документации
- `find_file_by_name(filename)` — поиск файлов по имени
- `list_files_in_category(category)` — список файлов в категории
- `get_table_of_contents(file_path)` — оглавление файла
- `search_exact(text, category?)` — точный текстовый поиск

## Технологии

- **FastMCP** — фреймворк для создания MCP серверов
- **LlamaIndex** — RAG фреймворк для индексации
- **FAISS** — векторная база для быстрого поиска
- **sentence-transformers** — модель эмбеддингов `paraphrase-multilingual-MiniLM-L12-v2`

---

## Планы развития

В будущем сюда будут добавляться документации других платформ и API. Следите за обновлениями репозитория.

---

**Дата актуальной сверки данных:** 30 ноября 2025, 16:00 МСК
