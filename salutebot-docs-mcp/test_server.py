"""Тестирование MCP-инструментов."""

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.path.insert(0, r"C:\Users\Roman\My MCP Servers\salutebot-docs-mcp")

from server import mcp

# Получаем оригинальные функции из декорированных инструментов
search_documentation = mcp._tool_manager._tools["search_documentation"].fn
read_full_file = mcp._tool_manager._tools["read_full_file"].fn
list_categories = mcp._tool_manager._tools["list_categories"].fn
find_file_by_name = mcp._tool_manager._tools["find_file_by_name"].fn
list_files_in_category = mcp._tool_manager._tools["list_files_in_category"].fn
get_table_of_contents = mcp._tool_manager._tools["get_table_of_contents"].fn
search_exact = mcp._tool_manager._tools["search_exact"].fn

def test_all():
    print("=" * 60)
    print("1. list_categories()")
    print("=" * 60)
    result = list_categories()
    print(result[:1000])
    print("\n")

    print("=" * 60)
    print("2. search_documentation('как создать интент')")
    print("=" * 60)
    result = search_documentation("как создать интент", top_k=3)
    print(result[:1500])
    print("\n")

    print("=" * 60)
    print("3. find_file_by_name('intent')")
    print("=" * 60)
    result = find_file_by_name("intent")
    print(result)
    print("\n")

    print("=" * 60)
    print("4. list_files_in_category('scenario/blocks')")
    print("=" * 60)
    result = list_files_in_category("scenario/blocks")
    print(result)
    print("\n")

    print("=" * 60)
    print("5. get_table_of_contents('bot-development/intents-phrases/overview.md')")
    print("=" * 60)
    result = get_table_of_contents("bot-development/intents-phrases/overview.md")
    print(result)
    print("\n")

    print("=" * 60)
    print("6. search_exact('slot-filling')")
    print("=" * 60)
    result = search_exact("slot-filling", category=None)
    print(result[:1500])
    print("\n")

    print("=" * 60)
    print("7. read_full_file('quick-start/quick-start.md') - первые 500 символов")
    print("=" * 60)
    result = read_full_file("quick-start/quick-start.md")
    print(result[:500])
    print("\n")

    print("=" * 60)
    print("ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")
    print("=" * 60)

if __name__ == "__main__":
    test_all()
