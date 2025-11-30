# function location(ll, lg)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Метод позволяет отправить местоположение в формате, поддерживаемом конкретным мессенджером.
В параметрах метода `(ll,lg)` передается широта и долгота.
  

##### Примеры значений
Используется для отправки координат, принимает широту и долготу:
```
state: Location  
        q!: location  
        script:  
            $reactions.location(59.8762548, 30.3160391);  

```

Эквивалентно использованию `$response.replies`:
```
$response.replies.push({  
type:"location",  
lat:59.8762548,  
lon:30.3160391  
}  

```