# function currentTime()
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Возвращает текущее время системы в миллисекундах.
Значение может быть переопределено в тестах.
  

##### Примеры значений
```
state: CurrentTime  
        q!: который час  
        script:  
            var timestamp = moment($jsapi.currentTime());  
            $temp.time = timestamp.format("HH:mm:ss");  
        a: Сейчас: {{ $temp.time }}  

```