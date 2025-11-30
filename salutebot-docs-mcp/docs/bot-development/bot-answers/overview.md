---
title: Ответы чат-бота
source_url: https://developers.sber.ru/docs/ru/salutebot/bot-development/bot-answers/overview
tags: [Code]
---

# Ответы чат-бота

В Code вы можете создавать сообщения различных типов:
  * [текстовые](https://developers.sber.ru/docs/ru/va/code/response/message-types#text);
  * [подсказки в диалоге с пользователем](https://developers.sber.ru/docs/ru/va/code/response/message-types#buttons);
  * [изображения](https://developers.sber.ru/docs/ru/va/code/response/message-types#image);
  * [произвольные ответы](https://developers.sber.ru/docs/ru/va/code/response/message-types#raw).

Произвольные ответы позволяют передавать [команды](https://developers.sber.ru/docs/ru/va/api/smartapp-api-commands) и [действия](https://developers.sber.ru/docs/ru/va/api/smartapp-api-actions), которые соответствуют протоколу SmartApp API.
Ответы сохраняются в массиве `$response.replies` , который содержит [строго типизированные элементы](https://developers.sber.ru/docs/ru/va/code/response/message-types). Массив наполняется с помощью метода `$response.replies.push()`.