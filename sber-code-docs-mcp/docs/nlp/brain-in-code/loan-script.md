# Сценарий опроса клиента Brain в Code
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
В данном сценарии мы опрашиваем клиента, который хочет заказать пиццу. Задача смартапа передать полученную информацию от клиента: название пиццы, размер и количество.
В файл `order.sc` добавьте следующий сценарий:
```
theme: /Order  
    state: Pizza  
        intent!: /OrderPizza  
        script:  
            $session.PizzaName = $parseTree._PizzaName  
            $session.PizzaSize = $parseTree._PizzaSize  
            $session.PizzaCount = $parseTree._PizzaCount  
        go!: /Order/Result  
  
    state: Result  
        a: Название пиццы: {{ $session.PizzaName }}  
        a: Размер пиццы: {{ $session.PizzaSize }}  
        a: Количество: {{ $session.PizzaCount }}  

```

Здесь:
  * При намерении пользователя заказать пиццу `/OrderPizza` срабатывает стейт `Pizza`. Если слоты сущностей для интента не заполнены, то мы дозапрашиваем информацию при помощи процесса слот-филлинга. Полученные данные записываем в `$session` для финального вывода полученной информации от клиента.

```
    state: Pizza  
        intent!: /OrderPizza  
        script:  
            $session.PizzaName = $parseTree._PizzaName  
            $session.PizzaSize = $parseTree._PizzaSize  
            $session.PizzaCount = $parseTree._PizzaCount  
        go!: /Order/Result  

```

  * Выводим всю полученную смартапом информацию.

```
    state: Result  
        a: Название пиццы: {{ $session.PizzaName }}  
        a: Размер пиццы: {{ $session.PizzaSize }}  
        a: Количество: {{ $session.PizzaCount }}  

```

[Протестируйте работу смартапа при помощи тестового виджета](./test.md).