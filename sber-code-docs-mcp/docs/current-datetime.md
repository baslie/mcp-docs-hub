# Текущие дата и время в Code
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Этот сервис просто возвращает текущие дату и время в указанном часовом поясе.
`https://smartapp-code.sberdevices.ru/tools/api/now?tz=Europe/Moscow&format=dd/MM/yyyy`
## Параметры
В качестве параметров запроса можно указать:
  * `tz` — код часового пояса (список кодов можно увидеть [здесь ](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones));
  * `format` — в каком формате нужно вернуть дату-время ([синтаксис ](https://docs.oracle.com/en/java/javase/11/docs/api/java.base/java/text/SimpleDateFormat.html) форматов).

По умолчанию сервис вернет текущие дату и время в часовом поясе UTC в формате `dd/MM/yyyy HH:mm`.
## Ответ сервиса
В ответе сервис возвращает JSON такого вида
```
{  
"timezone":"Etc/UTC",  
"formatted":"16.08.2018 13:45",  
"timestamp":1534427103257,  
"weekDay":4,  
"day":16,  
"month":8,  
"year":2018,  
"hour":13,  
"minute":45  
}  

```