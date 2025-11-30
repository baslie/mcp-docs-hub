# $fetch.query(url, settings)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Выполняет запросы к внешнему серверу.
Параметры:
  * `url` — адрес сервера в виде строки, может содержать параметры, которые будут заполнены из поля `query`, переданного в параметре `settings`.
  * `settings` — валидный JSON с параметрами запроса:
    * `method` — http-метод запроса: `GET`, `POST`, `PUT` и т.д.
    * `query` — параметры запроса для подстановки в `url`.
    * `body` — тело запроса.
    * `form` — форма.
    * `headers` — http-заголовки.
    * `datаType` — тип возвращаемых данных: `json`, `xml` или `text`.
    * `timeout` — таймаут выполнения запроса в миллисекундах.

Возвращаемый объект имеет следующие поля:
  * `isOk` — при успешном выполнении запроса принимает значение `true`. При ошибке внутри сервиса или при истечении таймаута принимает значение `false`.
  * `response` — полный дамп ответа. При ошибке внутри сервиса или при истечении таймаута запроса принимает значение `{}`. Может быть использован для получения http-заголовков.
  * `error` — строка с описанием ошибки. В случае успешного запроса принимает значение `undefined`. При истечении таймаута принимает значение `Read timed out`
  * `status` — числовой код состояния http (например, 200 или 401). При ошибке внутри сервиса или при истечении таймаута запроса принимает значение `-1`.

Обратите внимание на поведение http-вызовов при различных `datаType` и `Content-Type`:
Для вызова метода API, который принимает входные параметры в формате [HTML-форм ](https://developer.mozilla.org/ru/docs/Learn/Forms), в параметрах http-вызова используется объект `form` вместо `body`.
Такой вызов будет иметь заголовок `Content-Type` со значением `application/x-www-form-urlencoded` и соответствующим образом закодированные поля формы в теле запроса.
Так как поля формы передаются в теле запроса, использование метода `GET` не предусмотрено.
## Примеры
В примере ниже `$fetch.query` делает запрос, по указанному `url` с заданными параметрами:
```
state: getId  
    q!: запрос  
script:  
var url ="https://example.ru/patch";  
var settings ={method:"PATCH"};  
        $fetch.query(url, settings)  
.then(function(response){  
if(response.isSuccessful()){  
                    $temp.answer= response.serialize();  
}else{  
                    $temp.answer= response.serialize();  
}  
                $jsapi.log("$$$$$$$ log: "+toPrettyString($temp.answer));  
});  
a: id ={{toPrettyString($temp.answer.content)}}.  

```