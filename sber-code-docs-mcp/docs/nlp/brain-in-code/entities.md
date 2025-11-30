# Заполнение сущностей Brain в Code
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Заполните сущности, которые далее мы будем использовать в сценарии `loan.sc`:
  * [название пиццы](./entities.md#nazvanie-pitstsy);
  * [размер пиццы](./entities.md#razmer-pitstsy);
  * [количество](./entities.md#kolichestvo).

[Подробнее о создании пользовательских сущностей](https://developers.sber.ru/docs/ru/va/chat/voice-interface/command-recognition/entities/entities-types)
Используйте тестовый виджет для тестирования распознавания сущностей и интентов в различных сообщениях.
## Название пиццы
Добавьте сущность определения названия пиццы `PizzaName` со следующими паттернами:
  * для "Маргариты": `маргарит*`;
  * для "Пепперони": `(пепперон*/пеперон*)`;
  * для "Гавайской": `гавайск*`.

В `DATA` для каждого паттерна укажите значение сущности в формате `string`, в данном случае, это название пиццы: Маргарита, Пепперони, Гавайская.
![LoanType](https://developers.sber.ru/docs/assets/images/entities-1-68106fc1e96d9d25610fd4af5cc11d1e.png)
## Размер пиццы
Добавьте сущность определения размера пиццы `PizzaSize` со следующими паттернами:
  * маленькая: `(маленьк*/поменьш*)`;
  * средняя: `средн*`;
  * большая: `*больш*`.

В `DATA` для каждого паттерна укажите значение сущности в формате `string`, В данном случае, это размер пиццы: маленькая, средняя, большая.
![LoanSizeType](https://developers.sber.ru/docs/assets/images/entities-2-ea5ac36aabce25577d7d538235622097.png)
## Количество
[Активируйте распознавание системной сущности](https://developers.sber.ru/docs/ru/va/chat/voice-interface/command-recognition/entities/entities-types#sistemnye-sushnosti3) `@duckling.number`.
Далее приступайте к [заполнению интентов](./intents.md).