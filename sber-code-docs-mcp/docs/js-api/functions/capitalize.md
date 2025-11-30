# function capitalize(string)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Переводит первую букву переданной строки в заглавную. Используется для вывода имен и названий.
  

##### Примеры значений
```
script:  
$reactions.answer(“Привет ” + capitalize($client.name));  

```

```
a: Здравствуй {{ capitalize($client.name) }}  

```