# function transition(transition)
Обновлено 26 марта 2024
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Функция осуществляет переход в указанное состояние.
Функция может принимать:
  * Cтроку, в которой указано состояние для перехода. В формате `/path`.
  * Объект `transition`, который в поле `value` содержит путь к нужному стейту и флаг отложенного перехода `deferred`. Флаг принимает значения `true` и `false`.
Функция с флагом отложенного перехода `deferred=true` эквивалентна тегу [`go`](../../../sa-dsl/tags/reaction-tags.md#teg-go2).
Функция с флагом отложенного перехода `deferred=false` эквивалентна тегу [`go!`](../../../sa-dsl/tags/reaction-tags.md#teg-go12).
Описание объекта отличается от аналогичного в переменной [`$temp`](../../variables/temp.md).

  

##### Синтаксис
Путь после тега может быть как абсолютным, так и относительным:
  * `/` — корневая тема;
  * `.` — текущее состояние;
  * `..` — состояние на уровень выше;
  * `./..` — разделение элементов пути.

  

##### Примеры значений
```
script: $reactions.transition('/Welcome');  
$reactions.transition({value:'/Welcome',deferred:true});  

```