# function checkUrls(method, urls, findFirst)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
[](https://public.oprosso.sberbank.ru/p/docs_csi_2025)
Метод проверки доступности сайтов. Возвращает список: из одного или нескольких сайтов, в зависимости от флага `findFirst`.
  

##### Синтаксис
```
$http.checkUrls(method:HEAD|POST|GET,urls:[''..],findFirst:true|false)  

```

  

##### Примеры значений
```
state:  
        q!: *  
        script:  
            $temp.url = $http.checkUrls("HEAD", ['http://orrp.ru:8013/live_192', 'http://hosting.express.net.ua:13000', 'http://nashe.streamr.ru/rock-128.mp3'], true);  
        a: {{ $temp.url }}  

```