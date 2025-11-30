---
title: Асихронная отправка сообщения боту
source_url: https://developers.sber.ru/docs/ru/salutebot/salutebot-chatapi/send-chat-api-message-async
---

# Асихронная отправка сообщения боту
Отправка запроса клиента или события в чат-приложении. В отличие от [POST /chatapi/bot/{token}](send-chat-api-message-async.md#operation/post-chatapi-token) в ответ на запрос придет только идентификатор запроса, а сообщение бота будет отправлено на вебхук, указанный в настройках канала Chat API.
## Запрос
## Ответы
200
400
404
408
500
OK
Invalid request payload
ChannelChat config not found for token {token} and channel CHATAPI
Request timeout
Internal server error
Это полезный материал?