# function check(method, urls)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Метод проверки доступности сайтов. Возвращает один сайт.
  

##### Синтаксис
```
$http.check(method:HEAD|POST|GET,urls:[''..])  

```

  

##### Примеры значений
```
state:  
        q!: *  
        script:  
            $temp.url = $http.check("HEAD", ['http://orrp.ru:8013/live_192', 'http://hosting.express.net.ua:13000', 'http://nashe.streamr.ru/rock-128.mp3']);  
        a: {{ $temp.url }}  

```