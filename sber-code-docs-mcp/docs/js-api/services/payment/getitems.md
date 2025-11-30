# function getItems()
Обновлено 15 декабря 2023
Функция `$payment.getItems()` возвращает список товаров, добавленных в счет.
```
script: $reactions.answer(JSON.stringify($payment.getItems()));  

```