# $temp
Обновлено 4 марта 2024
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/SmartAppAPI.png)SmartApp API ](https://developers.sber.ru/docs/ru/va/api/overview)
Структура для хранения временных данных, время жизни которых ограничено временем выполнения одного запроса.
## Специальные поля
  * `targetState` — используется в препроцессорах для задания нового состояния, в котором нужно продолжить выполнение вместо того, которое вернул матчер.
  * `transition` — объект предназначен для обработки реакции `go` и является объектом с двумя полями `state` и `deferred`, соответствующими атрибутами тега `go/go!`.
Описание объекта отличается от аналогичного в функции [`transition(transition)`](../services/reactions/transition.md).

## Примеры значений
```
script:  
      $temp.sum = 5+6;  
      a: 5+6 = {{ $temp.sum }}  

```

```
$temp.totalSum+= variation.price* current_position.quantity;  

```

В значении можно использовать переменные, хранящиеся в объектах:
```
  a: "Мы ответили правильно на {{$temp.right}} {{$temp.ru__answers}} на текущем уровне сложности!"  

```