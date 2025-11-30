# function get(url, settings)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Эквивалентен вызову `$http.query(url, settings)`, при условии, что `settings.method == 'GET'`.
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
```
patterns:  
    $city = (москв*:moscow/питер*:saint_petersburg) || converter = function($pt){return $pt.value.replace("_","%20");}  
  
state: Weather  
    q!: Сколько градусов в $city  
    script:  
        var q = $parseTree.value;  
        var url = "https://api.apixu.com/v1/current.json?key=" + $injector.wheatherApiKey + "&q=" + q;  
        var response = $http.get(url);  
        if (response.isOk) {  
            $temp.degree = response.data.current.temp_c;  
        }  
    a: Сейчас {{ $temp.degree }}°C.  

```

Подробнее о работе с [`$http.query(url, settings)`](./query.md)