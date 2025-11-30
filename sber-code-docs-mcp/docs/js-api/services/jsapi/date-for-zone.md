# function dateForZone(zone, format)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Метод предназначен для получения текущей даты в заданном формате.
Дата прописывается строкой, используйте [шаблон синтаксиса формата даты ](https://docs.oracle.com/javase/tutorial/i18n/format/simpleDateFormat.html).
Тайм-зона прописывается согласно [классификации ](https://garygregory.wordpress.com/2013/06/18/what-are-the-java-timezone-ids/).
  

##### Примеры значений
```
log($jsapi.dateForZone("Europe/Moscow","dd.MM"))  
  
14:47:07.460[main]INFO  js -07.05  

```