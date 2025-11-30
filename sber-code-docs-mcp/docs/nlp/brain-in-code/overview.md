# Пример использования SmartApp Brain
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
В этом разделе на примере смартапа для заказа пиццы демонстрируется использование SmartApp Brain в среде разработки [Code](../../overview.md).
Этот смартап умеет:
  * принимать заказ и передавать его для дальнейшей обработки;
  * узнавать название пиццы, ее размер и количество

Для корректной работы смартапа вам потребуются:
  * [интенты](../../sa-dsl/tags/intents-tags.md);
  * [системные и пользовательские сущности](../entities/overview.md);
  * [модуль слот-филлинга](../slot-filling/overview.md).

Чтобы создать смартап на основе SmartApp Brain нужно выполнить следующие шаги:
  1. [Создание проекта Code](https://developers.sber.ru/docs/ru/va/chat/script/project-creation#sozdanie-proekta-code).
  2. [Подготовка проекта Code](./project.md).
  3. [Основной сценарий смартапа](./input-script.md).
  4. [Сценарий опроса пользователя](./loan-script.md).
  5. [Заполнение сущностей](./entities.md).
  6. [Заполнение интентов](./intents.md).
  7. [Тестирование сценария](./test.md).