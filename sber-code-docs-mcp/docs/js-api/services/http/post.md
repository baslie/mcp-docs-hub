# function post(url, settings)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Эквивалентен вызову `$http.query(url, settings)`, при условии, что `settings.method == 'POST'`.
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
## Примеры значений
Получаем информацию о городе по `cityId`.
Файл скрипта:
```
functiongetCityInfo(cityId){  
var url ='https://project/api/city/info';  
var options ={  
dataType:'json',  
headers:{  
'Content-Type':'application/json',  
},  
body:{  
cityId: cityId,  
},  
};  
var response = $http.post(url, options);  
return response.isOk? response.data:false;  
}  

```

Файл сценария:
```
state: TakeawayDiscountSpb  
        q!: Скидка на самовывоз в Питере  
        script:  
            var idSpb = 192;  
            $temp.response = getCityInfo(idSpb);  
        if: $temp.response  
            a: В городе {{ $temp.response.name }} скидка при самовывозе составляет {{ $temp.response.takeaway_discount }}%.  
        else:  
            a: Не знаю...  

```

Подробнее о работе с [`$http.query(url, settings)`](./query.md)
[Подробнее об отправке файлов на сторонний сервис POST-запросом](https://developers.sber.ru/docs/ru/va/chat/script/data/upload-file)