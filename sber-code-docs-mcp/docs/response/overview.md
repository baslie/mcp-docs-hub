# Формат ответа приложения в Code
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/ChatApp.png)Chat App ](https://developers.sber.ru/docs/ru/va/chat/title-page)
В Code вы можете создавать сообщения различных типов:
  * [текстовые](./message-types.md#text3);
  * [подсказки в диалоге с пользователем](./message-types.md#buttons2);
  * [изображения](./message-types.md#image2);
  * [карточки](./message-types.md#card);
  * [списки](./message-types.md#card-list);
  * [произвольные ответы](./message-types.md#raw2).

Произвольные ответы позволяют передавать [команды](https://developers.sber.ru/docs/ru/va/api/smartapp-api-commands) и [действия](https://developers.sber.ru/docs/ru/va/api/smartapp-api-actions), которые соответствуют протоколу SmartApp API.
Ответы сохраняются в массиве `$response.replies` , который содержит [строго типизированные элементы](./message-types.md). Массив наполняется с помощью метода `$response.replies.push()`.