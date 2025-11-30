# function query(url, settings)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
[](https://public.oprosso.sberbank.ru/p/docs_csi_2025)
Метод предназначен для выполнения внешних http-вызовов.
Параметр `url` — адрес в виде строки, может содержать параметры, которые будут заполнены из параметра `query`.
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
Объект `settings` содержит параметры запроса:
  * `method` — http-метод запроса: `GET`, `POST`, `PUT` и т.д.
  * `query` — параметры запроса для подстановки в `url`.
  * `body` — тело запроса.
  * `form` — форма.
  * `headers` — http-заголовки.
  * `datаType` — тип возвращаемых данных: `json`, `xml` или `text`.
  * `timeout` — таймаут выполнения запроса в миллисекундах.

Возвращаемый объект имеет следующие поля:
  * `isOk` — при успешном выполнении запроса принимает значение `true`. При ошибке внутри `$http`-сервиса или при истечении таймаута принимает значение `false`.
  * `response` — полный дамп ответа. При ошибке внутри `$http`-сервиса или при истечении таймаута запроса принимает значение `{}`. Может быть использован для получения http-заголовков.
  * `error` — строка с описанием ошибки. В случае успешного запроса принимает значение `undefined`. При истечении таймаута принимает значение `Read timed out`
  * `status` — числовой код состояния http (например, 200 или 401). При ошибке внутри `$http`-сервиса или при истечении таймаута запроса принимает значение `-1`.

Обратите внимание на поведение http-вызовов при различных `datаType` и `Content-Type`:
`Content-Type` | `dataType` | Поведение  
---|---|---  
задан | задан | Исходящему запросу устанавливается заголовок `Content-Type` с заданным значением.   
  
Ответ от сервера обрабатывается в соответствии с заданным форматом.  
задан | не задан | Исходящему запросу устанавливается заголовок `Content-Type` с заданным значением.   
  
Ответ от сервера обрабатывается в формате, полученным в заголовке ответа `Content-Type`.  
не задан | задан | Исходящему запросу устанавливается заголовок `Content-Type` со значением определяемым по `dataType`:   
  
`json → application/json`,   
`xml → application/xml`,  
`text → text/plain`,  
`другое → application/json`.   
  
Ответ от сервера обрабатывается в соответствии с заданным форматом.  
не задан | не задан,  
`guess` | Исходящему запросу устанавливается заголовок `Content-Type`: `application/json`.   
  
Ответ от сервера обрабатывается в формате, полученным в заголовке ответа `Content-Type`.  
Развернуть таблицу
Стоит обратить внимание, что http-вызовы происходят синхронно. Выполнение функции, вызвавшей `$http.query` не будет продолжено, до тех пор, пока не будет получен результат вызова.
Для обратной совместимости с кодом, который использует асинхронную обработку результатов, объект, возвращаемый функцией `query`, удовлетворяет интерфейсу `Promise`.
Для вызова метода API, который принимает входные параметры в формате [HTML-форм ](https://developer.mozilla.org/ru/docs/Learn/Forms), в параметрах http-вызова используется объект `form` вместо `body`.
Такой вызов будет иметь заголовок `Content-Type` со значением `application/x-www-form-urlencoded` и соответствующим образом закодированные поля формы в теле запроса.
Поскольку поля формы передаются через тело запроса, использование метода `GET` не предусмотрено.
  

##### Примеры значений
  * Простейший http-вызов. Здесь `$http.query` делает запрос, по указанному `url` с параметрами по умолчанию.

```
state:  
    q!: test 1  
    script:  
        $reactions.answer($http.query('http://localhost:9001/method1').data.text);  

```

  * Запрос к Weather API.

```
patterns:  
    $city = (москв*:moscow/питер*:saint_petersburg) || converter = function($pt){return $pt.value.replace("_","%20");}  
  
state: Weather  
    q!: Сколько градусов в $city  
    script:  
        var q = $parseTree.value;  
        var url = "https://api.apixu.com/v1/current.json?key=" + $injector.wheatherApiKey + "&q=" + q;  
        var response = $http.query(url, {method: "GET"});  
        if (response.isOk) {  
            $temp.degree = response.data.current.temp_c;  
        }  
    a: Сейчас {{ $temp.degree }}°C.  

```

  * Запрос с параметром `form`.

```
  $http.post('https://example.com/register-form',{  
form:{  
username:'Иван',  
email:'ivan@example.com',  
password:'examplepass',  
gender:'MALE'  
}  
}  

```

  * Расширенный вариант запроса.

```
// URL может содержать параметры, которые будут заполнены из параметра query  
  
var result = $http.query('http://localhost:9000/get-with-params?resultPart1=${resultPart1}&resultPart2=${resultPart2}',{  
method:"POST",// http-метод запроса - GET, POST, PUT и т.д.  
query:{// параметры запроса, для подстановки в URL  
resultPart1:'query',  
resultPart2:'with parameters'  
},  
body:{payload:"text"},// тело запроса  
form:{formField1:'1',formField2:'2'},// форма  
headers:{"Content-Type":"application/json","Authorization":"Basic xxxx ="}// http-заголовки  
dataType:"json",// тип возвращаемых данных - json, xml или text. По умолчанию используется тип, соответствующий заголовку content-type в ответе  
timeout:10000// таймаут выполнения запроса в мс  
});  

```