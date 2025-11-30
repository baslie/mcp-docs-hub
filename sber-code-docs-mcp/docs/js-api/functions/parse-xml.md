# function parseXml(xmlString)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Преобразует переданный xml-текст в JSON-объект.
  

##### Примеры значений
```
script:  
    var o = $jsapi.parseXml("<test><a>1</a><a>2</a></test>");  
    log(o);  

```

Распечатает следующий объект:
```
{"test":{"a":[1,2]}}  

```