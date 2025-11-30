# $request
Обновлено 3 мая 2024
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/SmartAppAPI.png)SmartApp API ](https://developers.sber.ru/docs/ru/va/api/overview)
Данные запроса клиента.
Объект содержит следующие поля:
  * `version` — версия протокола, по умолчанию последняя версия.
  * `channelType` — тип поверхности.
  * `botId` — идентификатор смартапа, используется для сопоставления запроса со сценарием, которым он должен быть обработан.
  * `channelUserId` — идентификатор пользователя.
  * `questionId` — идентификатор запроса.
  * `query` — текстовый запрос пользователя.
  * `rawRequest` — необработанный исходный запрос.

**Внимание!** Не тестируйте сценарий, в котором есть `$rawRequest`, в тестовом виджете! Если вы добавите `$rawRequest` в сценарий, а затем нажмете **Тестировать** , Code вернет ошибку, так как смартап не может получить данные из ассистента, когда диалог идет в тестовом виджете.
## Примеры
Получение идентификатора пользователя:
```
theme: /  
  
    state: Start  
        q!: $regex</start>  
        a: Начнем.  
  
    state: Приветствие  
        intent!: /привет  
        a: Ваш идентификатор {{$request.channelUserId}}  

```

Сохранение города пользователя:
```
state: RememberCity  
script:  
     $client.city = $request.query;  
$session.cart = [];  
go!: /ChoosePizza  

```

Получение интента и голоса ассистента, который установлен у пользователя.
```
state: Request  
    q!: интент из запроса  
    a: {{$request.rawRequest.payload.intent}}, {{$request.rawRequest.payload.original_intent}}  
  
state: getCharacter  
    script:  
         $session.character = $request.rawRequest.payload.character.name  

```