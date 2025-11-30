# SberDocs MCP Server

MCP-сервер для семантического поиска по документации SberSalute Code с использованием FAISS и LlamaIndex.

## Структура проекта

```
sber-code-docs-mcp/
├── builder.py          # Скрипт построения индекса (запускать при обновлении docs/)
├── server.py           # MCP-сервер (FastMCP, имя: "SberDocs")
├── requirements.txt    # Зависимости Python
├── docs/               # Markdown-документация SberSalute Code
├── storage/            # Метаданные LlamaIndex (генерируется builder.py)
├── faiss_index.bin     # FAISS индекс (генерируется builder.py)
└── venv/               # Виртуальное окружение Python
```

## Категории документации (docs/)

| Категория | Описание |
|-----------|----------|
| js-api/ | JavaScript API для SmartApp |
| nlp/ | NLP и обработка естественного языка |
| project/ | Настройки проекта |
| response/ | Форматы ответов |
| sa-dsl/ | SmartApp DSL |
| templates/ | Шаблоны |
| testing/ | Тестирование |
| root | Корневые файлы (README.md, overview.md, current-datetime.md) |

## MCP-инструменты

### search_documentation(query, category?, top_k?)
Семантический поиск по документации.
- `query` — поисковый запрос (русский/английский)
- `category` — фильтр по категории (например: `js-api`, `nlp`)
- `top_k` — количество результатов (1-20, по умолчанию 7)

### read_full_file(file_path)
Чтение файла документации целиком.
- `file_path` — путь относительно docs/ (например: `js-api/overview.md`)
- Для корневых файлов: `root/README.md`

### list_categories()
Список всех категорий документации с количеством файлов.

### find_file_by_name(filename)
Поиск файлов по имени (регистронезависимый).
- `filename` — подстрока для поиска (например: `inference`)

### list_files_in_category(category)
Список всех файлов в категории с заголовками.
- `category` — название категории (например: `nlp/api`)

### get_table_of_contents(file_path)
Оглавление файла (все заголовки #, ##, ###).
- `file_path` — путь к файлу

### search_exact(text, category?)
Точный текстовый поиск (grep-подобный).
- `text` — искомый текст
- `category` — опционально, фильтр по категории

## Технологии

- **FAISS** (faiss-cpu) — быстрый векторный поиск
- **LlamaIndex** — RAG-фреймворк, индексация и retriever
- **sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2** — мультиязычные эмбеддинги (384 измерения)
- **FastMCP** — MCP-сервер по протоколу stdio

## Конфигурация клиента (.mcp.json)

```json
{
  "mcpServers": {
    "sber-code-docs": {
      "type": "stdio",
      "command": "cmd",
      "args": [
        "/c",
        "C:\\Users\\Roman\\My MCP Servers\\sber-code-docs-mcp\\venv\\Scripts\\python.exe",
        "C:\\Users\\Roman\\My MCP Servers\\sber-code-docs-mcp\\server.py"
      ]
    }
  }
}
```

## Обновление индекса

При добавлении/изменении файлов в docs/:

```powershell
cd "C:\Users\Roman\My MCP Servers\sber-code-docs-mcp"
.\venv\Scripts\Activate.ps1
python builder.py
```

После индексации перезапустите Claude Code для переподключения к серверу.
