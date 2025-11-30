---
title: Обрабатываем запросы пользователя
source_url: https://developers.sber.ru/docs/ru/salutebot/dialog/raw-request
tags: [Graph]
---

# Обрабатываем запросы пользователя

Для обработки данных запроса используется системная переменная [`$rawRequest`](https://developers.sber.ru/docs/ru/va/graph/variables/system_variables).
## Переменная rawRequest
Переменная содержит запрос пользователя в формате [SmartApp API](https://developers.sber.ru/docs/ru/va/api/overview).
Для доступа к полям переменной используется точечная нотация JavaScript:
```
$rawRequest.payload.message;  

```

При запуске чат-ботов с `$rawRequest` в тестовом виджете будет возникать ошибка.
## Подробнее о переменных
  * [Что такое переменные](https://developers.sber.ru/docs/ru/va/graph/variables/create-variables)
  * [Системные переменные](https://developers.sber.ru/docs/ru/va/graph/variables/system_variables)