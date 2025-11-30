# function random(max)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Генератор случайных чисел. Метод возвращает целочисленные значения от `0` до `max` (не включая `maх`).
Отличается от `Math.random()` тем, что возвращаемые им значения могут быть переопределены в тестах.
Метод является вспомогательным для функции `$reactions.random()`. Использовать его напрямую не рекомендуется.
  

##### Примеры значений
```
functiongetRandomGenre(music){  
var id = $jsapi.random(5)+1;  
var randomGenre = music[id];  
return randomGenre;  
}  

```