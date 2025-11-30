# Теги тестирования в Code
Обновлено 10 января 2024
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
## Тег a
Проверяет:
  * наличие ответа от ассистента;
  * текст ответа;
  * состояние, в котором ответ был сгенерирован;
  * состояние, с которого началось выполнение сценария.

В проверках текста не учитывается разница в пробелах и переносах строк.
На каждую реплику ассистента `a:` необходим тег `<a>` в тестах.
  

**Атрибуты**
  * `class` — `state`, с которого началось выполнение сценария для текущего запроса, необязательный атрибут.
  * `state` — `state`, в котором был сгенерирован ответ, необязательный атрибут.

  

**Тело**
Текст ожидаемого ответа, необязательно.
  

**Примеры**
```
<a></a>  
<a>Текст ответа</a>  
<astate="/End"/>  
<aclass="/Start"/>  
<astate="/End"class="/Start">Текст ответа</a>  

```

## Тег dateTime
Переопределяет дату и время, с которой будут работать функции JS API, такие, как `currentTime`, `dateForZone`, `timeForZone`.
  

**Тело**
Дата и время в формате `yyyy-MM-dd HH:mm:ss`.
  

**Примеры**
```
<dateTime>2016-06-07 13:23:55</dateTime>  

```

```
<dateTime>  
    2018-01-01 12:00:00  
</dateTime>  

```

## Тег event
Тег `event` эмулирует отправку события смартапу.
  

**Тело**
Имя события.
  

**Примеры**
  * Пользователь отправил данные о своем местоположении

```
<event>telegramSendLocation</event>  

```

  * Пользователь прикрепил файл.

```
<event>fileEvent</event>  

```

## Тег mail
Проверяет использование сервиса `$mail`.
  

**Атрибуты**
  * `recipient` — получатель, необязательный параметр.
  * `subject` — тема письма, необязательный параметр.
  * `body` — содержание письма, необязательный параметр.

  

**Примеры**
```
<mail/>  

```

```
<mailsubject="Здравствуйте, Иван Иванович!"/>  

```

Рассмотрим сценарий:
```
theme: /  
    state:  
        q!: *  
        script:  
            $mail.sendMessage(  
                "example@example.com",  
                "message subject",  
                "message body"  
            );  

```

Тест для сценария:
```
<test>  
<test-case>  
<q>send1</q>  
<mailrecipient="example@example.com"  
subject="message subject"  
body="message body"/>  
</test-case>  
  
<test-case>  
<q>send2</q>  
<mailrecipient="example@example.com"/>  
</test-case>  
  
<test-case>  
<q>send3</q>  
<mailsubject="message subject"  
body="message body"/>  
</test-case>  
</test>  

```

## Тег mockData
Тег `mockData` позволяет задать фиктивные ответы на http-вызовы из контента смартапа.
Элементы `query` и `parameters` формируют конечный url запроса, при обращении к которому из смартапа, ответ будет взят из тела тега `response`. При наличии элемента `body` будет дополнительно происходить сопоставление по телу запроса.
Важен порядок следования тегов `mockData` и чередования с другими тегами внутри `test-case`. При сопоставлении мока запросу учитываются все теги `mockData` внутри `test-case`, которые предшествуют запросу, но при совпадении по url и body предпочтение отдается последнему тегу `mockData`. Пример:
```
<test-case>  
<mockData>  
<query>http://example.com</query>  
<responsetype="text">Низкий приоритет</response>  
</mockData>  
<mockData>  
<query>http://example.com</query>  
<responsetype="text">Высокий приоритет</response>  
</mockData>  
<q>запроси example.com</q>  
<a>Высокий приоритет</a>  
<mockData>  
<query>http://example.com</query>  
<responsetype="text">Игнорируется при первом вызове, но используется при втором</response>  
</mockData>  
<q>запроси example.com<q>  
<a>Игнорируется при первом вызове, но используется во втором</a>  
</test-case>  

```

  

**Дочерние элементы**
  * `query` — описание запроса, обязательный элемент. 
    * атрибут `method`- HTTP-метод. По умолчанию: `GET`.

Тело: Шаблон url запроса, обязательно. Аналогичен шаблону, используемому в `$http`-сервисе JS API.
Обратите внимание на [необходимость экранирования в xml ](https://stackoverflow.com/questions/1091945/what-characters-do-i-need-to-escape-in-xml-documents) таких символов, как `&`.
  * `parameters` — параметры шаблона в виде элементов `xml`:

```
<имя-параметра>значение-параметра</имя-параметра>  

```

Функционально аналогичны параметру `query` в `$http`-сервисе JS API.
  * `body` — описание тела (HTTP message body) запроса, Необязательный элемент. 
    * атрибут `strictMatch` — строгость сопоставления. По умолчанию: false. В случае строго сопоставления, мок подходит, если количество и значения полей в json-объекте из тега `<body>` равны таковым в `HTTP message body` запроса. В случае нестрого сопоставления, мок подходит, если все значения полей из json-объекта равны соответствующим значениям полей `HTTP message body` запроса.
    * атрибут `field` — JsonPath-выражение, необязательный атрибут. Позволяет указать, что сопоставление нужно производить не по всему объекту из тела запроса, а только по его части.

Тело: JSON-объект или примитив, по которому происходит сопоставление мока наравне с url, обязательно.
Тег `body` позволяет задать дополнительный параметр соответствия мока http-запросу, наряду с тегом `query`.
Тег полезен в случае, когда все параметры запроса к стороннему API передаются через тело запроса.
  * `response` — описание ответа сервера, обязательный элемент. 
    * атрибут `status` — HTTP статус код ответа, по умолчанию `200`.
    * `type` — тип ответа. По умолчанию: `json`. В случае, если тип `json` или `xml`, ответ парсится и передается в скрипт в виде JavaScript объекта. В противном случае, ответ сервера передается в виде строки.

Тело: строка с ответом сервера, обязательно.
В случае, если тип ответа не `json` или `xml`, то ответ передается смартапу в виде строки, включающей все символы пробелов и переносы строк. Поэтому здесь разные ответы:
```
<responsetype="text">ok</response>  

```

```
<responsetype="text">  
    ok  
</response>  

```

Во втором случае текст ответа в скрипте будет равен следующей JS-строке:
```
'\n    ok\n';  

```

  

**Примеры**
  * `mock` ответа на запрос к `example.com`

```
<mockData>  
<querymethod="get">  
        http://example.com/${path}/?param1=${p1}&amp;param2=${p2}  
</query>  
<parameters>  
<path>путь</path>  
<p1>value 1</p1>  
<p2>value 2</p2>  
</parameters>  
<responsetype="json"status="200">  
        {"json": "response"}  
</response>  
</mockData>  

```

  * Функционально тот же `mock`, что и в предыдущем примере, но с атрибутами по умолчанию и параметрами шаблона, заданными непосредственно в `url`, а не в элементе `parameters`.

```
<mockData>  
<query>  
        http://example.com/%D0%BF%D1%83%D1%82%D1%8C/?param1=value+1&amp;param2=value+2  
</query>  
<response>{"json": "response"}</response>  
</mockData>  

```

  * Пример, раскрывающий семантику тегов `<body>` и переопределения моков внутри `<test-case>`:

```
//сценарий  
state:  
    q!: test  
script:  
        $response = $http.post('http://example.com',{  
body:{  
bodyParam1:"text1",  
bodyParam2:"text2",  
bodyObject:{  
bodyParam3:100,  
bodyParam4:false  
}  
}  
});  
a:{{ $response.data}}  

```

```
// test.xml  
<mockData>  
<querymethod="post">  
        http://example.com  
</query>  
<bodystrictMatch="true">  
        {  
            "bodyParam1": "text1",  
            "bodyParam2": "text2",  
            "bodyObject": {  
                "bodyParam3": 100,  
                "bodyParam4": false  
            }  
        }  
</body>  
<responsetype="text">ok1</response>  
</mockData>  
  
<test-case>  
<q>test</q>  
<a>ok1</a>  
  
<mockData>  
<querymethod="post">  
            http://example.com  
</query>  
<body>  
            {  
            "bodyParam1": "text1",  
            "bodyParam2": "text2"  
            }  
</body>  
<responsetype="text">ok2</response>  
</mockData>  
<q>test</q>  
<a>ok2</a>  
  
<mockData>  
<querymethod="post">  
            http://example.com  
</query>  
<bodyfield="bodyObject">  
            {  
            "bodyParam3": 100,  
            "bodyParam4": false  
            }  
</body>  
<responsetype="text">ok3</response>  
</mockData>  
<q>test</q>  
<a>ok3</a>  
  
<mockData>  
<querymethod="post">  
            http://example.com  
</query>  
<bodyfield="bodyObject">  
            {  
            "bodyParam3": 100  
            }  
</body>  
<responsetype="text">ok4</response>  
</mockData>  
  
<mockData>  
<querymethod="post">  
            http://example.com  
</query>  
<bodyfield="bodyObject"strictMatch="true">  
            {  
            "bodyParam3": 100  
            }  
</body>  
<responsetype="text">would not match</response>  
</mockData>  
<q>test</q>  
<a>ok4</a>  
  
<mockData>  
<querymethod="post">http://example.com</query>  
<responsetype="text">ok5</response>  
</mockData>  
<q>test</q>  
<a>ok5</a>  
  
<mockData>  
<querymethod="post">http://example.com</query>  
<bodyfield="bodyParam2">"text2"</body>  
<responsetype="text">ok6</response>  
</mockData>  
<q>test</q>  
<a>ok6</a>  
</test-case>  

```

## Тег newSession
Проверяет наличие и параметры реакции `newSession`
  

**Атрибуты**
  * `message` — стартовое сообщение, необязательный атрибут.

  

**Дочерние элементы**
  * `data` — JSON-объект, необязательный элемент. Данные `$session` для новой сессии,по умолчанию равен пустому объекту.

  

**Примеры**
  * Использование тега `newSession`:

```
<newSession/>  
  
<newSessionmessage="новая сессия"/>  
  
<newSessionmessage="новая сессия">  
<data>{ "myField": "myValue"}</data>  
</newSession>  

```

> Далее представлены примеры альтернативных проверок на наличие и параметры реакции `newSession`.
  * Использование тега `requestData` для передачи параметров запроса:

```
<test-case>  
<requestData>{ "fromNewSession": "true" }</requestData>  
<q>/start</q>  
<astate="/Start"/>  
</test-case>  

```

  * Использование встроенной функции `testMode()`, которая позволяет определить, находится ли система в режиме тестирования.

Объявляем функцию `startNewSession()` в файле `function.js`
```
functionstartNewSession(){  
var $context = $jsapi.context();  
if($context.request.data.fromNewSession){  
return;  
}  
  
log('New session for user');  
    $context.request.data.fromNewSession=true;  
    $reactions.newSession({request: $context.request});  
}  

```

Делаем проверку на `testMode()` в сценарии:
```
require: scripts/function.js  
require: common.js  
    module = common  
  
theme:/  
state:Start  
        q!:**start  
script:  
if(!testMode()){  
startNewSession();  
}  
a: Получилось?  
  
state:Yes  
q: да  
script:  
                $session.newField="yep";  

```

## Тег q
Тег `q` эмулирует отправку текстового сообщения ассистенту пользователем.
  

**Тело**
Текст сообщения, которое посылается ассистенту.
  

**Примеры**
```
<q>/start</q>  

```

```
<q>Ассистент, что ты умеешь?</q>  

```

## Тег random
Задает числа, которые будут возвращаться функцией `random` в JS API.
В случае, если в сценарии будет запрошено больше случайных чисел, чем определено в теге `<random>`, то функция `$jsapi.random` будет возвращать значение `0`.
Если в запросе к смартапу не определено поле `smartRandom`, то `$jsapi.random` используется для получения случайных чисел при вызове `$reactions.random`. Повторяющиеся числа при этом игнорируются.
`$reactions.random` так же используется при выборе варианта в теге `random` в сценариях.
Все сгенерированные в ходе выполнения теста случайные числа записываются в `response`.
  

**Тело**
Список чисел, разделенных символом `,`.
  

**Примеры**
```
<random>1, 2, 3, 4, 5</random>  

```

```
<random>  
    128, 0, 42  
</random>  

```

Рассмотрим сценарий:
```
theme: /  
state: Random  
q!: rand  
random:  
a: первый!   // 0  
a: второй!   // 1  
a: третий!   // 2  

```

Тест для сценария:
```
<test>  
<test-case>  
<random>1,2</random>  
  
<q>rand</q>      // 1  
<a>второй!</a>  
  
<q>rand</q>       // 2  
<a>третий!</a>  
  
<q>rand</q>       // 0  
<a>первый!</a>  
</test-case>  
</test>  

```

Здесь:
  1. (1) `$jsapi.random` возвращает `1`, возвращается ответ с индексом 1.
  2. (2) `$jsapi.random` возвращает `2`, возвращается ответ с индексом 2.
  3. (0) `$jsapi.random` возвращает `0`, так как закончились числа, определенные в теге `<random>`, возвращается ответ с индексом 0.

## Тег rawRequest
`rawRequest` позволяет передать структуру `$request.rawRequest,` в которую обычно сохраняется дамп запроса.
  

**Тело**
JSON-объект.
  

**Примеры**
Рассмотрим сценарий:
```
state:  
    q!: test  
a:{{ $request.rawRequest.data}}  

```

Тест для сценария:
```
<test-case>  
<rawRequest>{ "data": "данные запроса" }</rawRequest>  
<q>test</q>  
<a>данные запроса</a>  
</test-case>  

```

## Тег request
Тег `request` позволяет передать полный объект запроса и может использоваться для передачи любых параметров запроса.
Поля, не соответствующие формату запроса `BotRequest`, в сценарии недоступны.
  

**Тело**
JSON-объект в формате `BotRequest`.
  

**Примеры**
```
<request>{"targetState":"/Some state", "questionId":"id123", "event": "some_event"}</request>  

```

Рассмотрим сценарий:
```
state:Request  
    q!: request  
a:{{ $request.channelType}},{{ $request.data.field}}  
  
state:Unknown  
    q!: unknown  
a: unknownField:{{ $request.unknownField}}  

```

Тест для сценария:
```
<test-case>  
<request>{  
      "query": "request",  
      "channelType": "mockTest",  
      "data": {  
        "field": "данные из запроса"  
      }  
    }</request>  
<a>mockTest, данные из запроса</a>  
</test-case>  
  
<test-case>  
<request>{  
      "targetState": "/3",  
      "data": {  
        "field": "данные из запроса"  
      }  
    }</request>  
<a>, данные из запроса</a>  
</test-case>  
  
<test-case>  
<request>{  
      "query": "unknown",  
      "unknownField": "mockTest"  
    }</request>  
<a>unknownField: </a>  
</test-case>  

```

## Тег requestData
С помощью тега `requestData` можно передавать параметры запроса.
  

**Тело**
JSON-объект.
  

**Примеры**
Рассмотрим сценарий:
```
state:  
    q!: data  
a:{{ $request.data.field}}  
  
state:  
    q!: random  
random:  
a: первый  
a: второй  
random:  
a: первый!  
a: второй!  
a: третий!  

```

Тест для сценария:
```
<test-case>  
<requestData>{ "field": "данные из запроса" }</requestData>  
<q>data</q>  
<a>данные из запроса</a>  
</test-case>  
  
<test-case>  
<requestData>{ "smartRandom": [1, 2] }</requestData>   //Данные для `random` могут быть переданы через `requestData  
<q>random</q>  
<a>второй</a>  
<a>третий!</a>  
</test-case>  

```

## Тег responseData
Самый гибкий вариант проверки ответа смартапа. Тег `responseData` позволяет проверить на соответствие поля объекта `$response.data`. Проверяются только поля, указанные внутри тела тега.
  

**Атрибуты**
  * `field` - JSONPath-выражение, необязательный атрибут. Позволяет указать, какую часть объекта `$response.data` проверять на соответствие.

  

**Тело**
JSON-объект или примитив.
  

**Примеры**
```
<responseData>{  
  "replies": [  
    {  
      "type": "text",  
      "text": "Проверяем полный объект $response.data",  
      "state": "/1"  
    }  
  ],  
  "answer": "Проверяем полный объект $response.data"  
}</responseData>  
  
<responseData>{  
  "answer": "Не обязательно указывать все поля при проверке"  
}</responseData>  
  
<responseDatafield="replies[0].buttons">  
[  
    {"text": "Кнопка 1"},  
    {"text": "Кнопка 2", "transition": "/1/handler2"}  
]  
</responseData>  
  
<responseDatafield="smartRandom">[1, 2]</responseData> //Все сгенерированные в ходе выполнения теста случайные числа записываются в `$response.data.smartRandom`  

```

## Тег state
Принудительно переводит контекст диалога в указанное состояние. Все действия, производимые после использования тега, будут рассматриваться в контексте указанного состояния.
Функционально устанавливает значение `$session.contextPath` равным строке из тела тега.
  

**Тело**
Имя состояния.
  

**Примеры**
```
// сценарий  
theme:/  
state:1  
        q!:1  
a:1  
  
state:2  
q:2  
a:2  

```

```
<test>  
<test-case>  
<state>1</state>  
<q>2</q>  
<a>2</a>  
</test-case>  
</test>  

```

## Тег test-case
Непосредственно описывает тест. Перед проверкой тестов сбрасываются пользовательские данные, такие как `clientData` или `sessionData`.
  

**Атрибуты**
  * `id`:string — идентификатор (имя) теста. Необязательный атрибут.
  * `integration`:boolean — определяет, будут ли вызываться реальные внешние сервисы или будут использоваться только mock-данные для теста. Аналогичен атрибуту `integration` в теге test и может переопределять его поведение. Значение по умолчанию: значение атрибута `integration` тега `test`.

  

**Дочерние элементы**
Любой из тестовых тегов, кроме тега `<test>`.
  

**Примеры**
```
<test-caseid="test 1">  
<q>test 1</q>  
<a>test response</a>  
</test-case>  

```

```
<test-caseid="test 2">  
<requestData>  
        { "field": "данные из запроса" }  
</requestData>  
<q>test 2</q>  
<a>С помощью тэга requestData можно передавать параметры запроса</a>  
<a>данные из запроса</a>  
</test-case>  

```

```
<test-caseid="test 3">  
<request>  
    {  
      "query": "test 3",  
      "channelType": "mockTest",  
      "data": {  
        "field": "данные из запроса"  
      }  
    }  
</request>  
<a>mockTest, данные из запроса</a>  
</test-case>  

```

## Тег test
Обязательный корневой элемент `xml`-файла.
  

**Атрибуты**
  * `integration`:boolean — определяет использование реальных http-вызовов в тестах. При значении `true` будут сделаны настоящие http-вызовы вместо использования данных, определенных в тегах `mockData`. По умолчанию: `false`.

  

**Дочерние элементы**
  * `test-case`
  * `mockData`

  

**Примеры**
```
<test>  
<test-case>  
<q>question 1</q>  
<a>answer 1</a>  
</test-case>  
</test>  

```

```
<test>  
<mockData>  
<querymethod="get">http://number.example.com/</query>  
<responsetype="text">42</response>  
</mockData>  
  
<test-case>  
<q>число</q>  
<a>число с сервера: 42<a>  
</test-case>  
</test>  

```

```
<testintegration="true">  
<test-case>  
<q>число</q>  
<a>число с сервера: 36<a>  
</test-case>  
</test>  

```

## Тег timeout
Бездействие пользователя в течение времени, заданного ранее в сценарии реакцией таймаут.
  

**Примеры**
```
<test>  
  
<test-case>  
<q>/start</q>  
<a>Набери timeout, чтобы начать</a>  
<timeoutReplytargetState="/timeout"/>  
<timeout/>  
<a>Этот ответ должен быть выведен в случае, если клиент молчит</a>  
<timeoutReplyinterval="2"/>  
<timeout/>  
<a>Тест окончен</a>  
</test-case>  
</test>  

```

## Тег timeoutReply
Проверяет наличие и параметры реакции `timeout`.
  

**Атрибуты**
  * `targetState` — состояние, в которое должен перейти смартап по истечению таймаута, необязательный атрибут.
  * `interval` — интервал ожидания для реакции `timeout` в секундах, число, необязательный атрибут.

  

**Примеры**
```
<timeoutReply/>  
<timeoutReplyinterval="2"/>  
<timeoutReplytargetState="/timedout"interval="5"/>  

```