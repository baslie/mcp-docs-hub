---
title: Используем имя, телефон и email
source_url: https://developers.sber.ru/docs/ru/salutebot/scenario/scenario-management/using-user-data
tags: [Graph, Code]
---

# Используем имя, телефон и email

Если у вас есть проект SaluteBot, подключенный к каналам Jivo, вы можете использовать в сценарии данные пользователя – имя, телефон и электронный адрес.
Graph
Code
В Graph вы можете воспользоваться системной переменной [`$clientProfile`](https://developers.sber.ru/docs/ru/va/graph/variables/system_variables):
  * `$clientProfile.name` — ФИО.
  * `$clientProfile.email` — электронный адрес.
  * `$clientProfile.phone` — номер телефона.

Например, чтобы поприветствовать пользователя, используя имя:
  1. Добавьте в сценарий [блок Текст](../blocks/text.md) с приветствием.
  2. Добавьте в блок вывод имени пользователя через переменную `$clientProfile.name`.
  3. Соберите сценарий и протестируйте чат-бот в подключенном канале Jivo.

При запуске чат-ботов с `$clientProfile.name` в тестовом виджете будет возникать ошибка, так как чат-бот не может получить данные канала Jivo.
В Code вы можете воспользоваться системной переменной [`$rawRequest`](https://developers.sber.ru/docs/ru/va/code/js-api/variables/request):
  * `$request.rawrequest.sender.name` — ФИО.
  * `$request.rawrequest.sender.email` — электронный адрес.
  * `$request.rawrequest.sender.phone` — номер телефона.

Например, вы можете поприветствовать пользователя, используя имя:
```
state: Start  
    q!: $regex</start>  
    a: Привет {{ $request.rawrequest.sender.name }}! Чем могу помочь?  

```