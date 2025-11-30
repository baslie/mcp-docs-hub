# Тестирование сценария Brain в Code
Обновлено 20 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
[](https://public.oprosso.sberbank.ru/p/docs_csi_2025)
Для тестирования сценария смартапа перейдите _Редактор_ > _Сценарии_ > запустите тестовый виджет, нажав в нижнем правом углу кнопку _Тестировать._
Далее рассмотрим основные кейсы нашего сценария:
  1. Ассистент приветствует клиента и по-разному реагирует, в зависимости от того, был ли заполнен слот для сущности `@pymorphy.name` (распозналось ли имя):

![slots](https://developers.sber.ru/docs/assets/images/test-1-af9afdd68d3dd450ad79e832e77ac2d5.png)
![slots](https://developers.sber.ru/docs/assets/images/test-2-89ba2cff5224c4bd18151c2173296068.png)
  1. Клиент выражает свое намерение `заказать пиццу`, но при этом этих данных недостаточно для движения далее по сценарию, так как слоты сущностей `@PizzaName`, `@PizzaSize` и `@PizzaCount` не заполнены. При помощи слот-филлинга мы дозапрашиваем информацию у клиента.

![slots](https://developers.sber.ru/docs/assets/images/test-3-65d5bc84e619886282452ae15c375347.png)
  1. После того, как все слоты были заполнены, смартап возвращается к основному сценарию. Здесь будет выведена вся собранная информация.

![slots](https://developers.sber.ru/docs/assets/images/test-4-161f381bf08732c21bcb26463cde0293.png)
[Напишите тесты на сценарий смартапа](../../testing/tests-xml.md).
  1. Приступайте к процедуре [публикации смартапа](https://developers.sber.ru/docs/ru/va/about/publication/app-publication).