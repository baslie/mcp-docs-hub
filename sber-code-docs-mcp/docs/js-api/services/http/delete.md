# function delete(url, settings)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Эквивалентен вызову `$http.query(url, settings)`, при условии, что `settings.method == 'DELETE'`.
Может содержать сторонний адрес.
В одном запросе можно совершить максимум 15 вызовов. При превышении количества вызовов возращается ошибка:
```
{  
"error":"Callback limit reached",  
"status":-1,  
"isOk":false  
}  

```

Адрес может быть как абсолютным, так и относительным. Для использования относительного адреса, необходимо задать базовый адрес с помощью метода [`$http.config(settings)`](./config.md).
Подробнее о работе с [`$http.query(url, settings)`](./query.md)