---
title: Структура и конфигурация проекта
source_url: https://developers.sber.ru/docs/ru/salutebot/bot-development/project-structure/overview
tags: [Code]
---

# Структура и конфигурация проекта

Проект чат-бота может включать в себя следующие файлы:
  * `chatbot.yaml` — [конфигурационный файл](https://developers.sber.ru/docs/ru/salutebot/bot-steps/project-structure/configuration_file) чат-бота. Содержит имя главного файла сценария, информацию о подключаемых модулях, конфигурацию NLU-модуля, список тестов и другую конфигурационную информацию.
  * `.sc` — [файлы сценариев](https://developers.sber.ru/docs/ru/salutebot/bot-steps/project-structure/sc). Это основные файлы, задающие правила работы чат-бота.
  * `.js` — [файлы js-библиотек](https://developers.sber.ru/docs/ru/salutebot/bot-steps/project-structure/js). Содержат JavaScript-код, который можно использовать в файлах сценариев. Могут содержать функции, логику обработки запросов, вызовы внешних систем и пр.
  * `.csv` — [справочники именованных сущностей](https://developers.sber.ru/docs/ru/salutebot/bot-steps/project-structure/csv). Необходимы для обработки в паттернах большого количества каких-либо названий, например, названий городов, стран, имен и пр.
  * `.yaml` — справочники ответов и других параметров для использования в скриптах.
  * `.xml` — [файлы с тестами](https://developers.sber.ru/docs/ru/salutebot/bot-steps/project-structure/xml). Автоматические тесты, которые выполняются при деплое чат-бота.
  * `examples.json` — справочник примеров. Предназначен для обучения классификатора или ручной разметки.

Дескриптор сценария должен находиться в папке проекта: `Папка_проекта/chatbot.yaml`.
Тесты должны находиться в папке `test`: `Папка_проекта/test/ваши_тесты.xml`.
Все остальные файлы должны находиться в папке `src`: `Папка_проекта/src/прочие_файлы`.
Минимальный проект чат-бота состоит из:
  * файла `chatbot.yaml`, который содержит дескриптор проекта и лежит в корневой папке проекта.
  * папки `src`, в которой находится файл `main.sc` с основным сценарием работы чат-бота. В этой папке также могут находиться файлы с дополнительными сценариями, словари в формате `.csv` и скрипты в формате `.js`.
  * папки `test`, в которой лежат тесты `.xml` для сценария работы чат-бота.

## Смотрите также:
  * [JavaScript API в SmartApp DSL](https://developers.sber.ru/docs/ru/va/code/js-api/overview)
  * [SmartApp DSL](https://developers.sber.ru/docs/ru/va/code/sa-dsl/overview)