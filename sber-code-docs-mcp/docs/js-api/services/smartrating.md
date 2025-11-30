# smartRating в Code
Обновлено 19 февраля 2025
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/SmartRating.png)SmartRating ](https://developers.sber.ru/docs/ru/va/smartservices/smartrating/overview)
[](https://public.oprosso.sberbank.ru/p/docs_csi_2025)
Сервис для запроса пользовательской оценки смартапа. Чем больше пользователей оценят ваш смартап и чем выше будет средняя оценка, тем выше будет позиция смартапа в выдаче.
Статистика по оценкам доступна в Studio в разделе [Оценки](https://developers.sber.ru/docs/ru/va/about/smartapp/metrics#otsenki).
Перед использованием сервиса ознакомьтесь с [правилами](https://developers.sber.ru/docs/ru/va/smartservices/smartrating/rules).
## Запрос
Запрос вызывает сервис по инициативе пользователя. Добавьте запрос в стейт, который будет обрабатывать действие пользователя.
```
$smartRating.callRating();  

```

Чтобы добавить дополнительные настройки вызова, используйте следующий код:
```
script:  
    $response.replies = $response.replies ||[];  
    $response.replies.push({  
'type':"raw",  
'messageName':'CALL_RATING'  
'body':{}  
});  

```

## Ответ
### Пример ответа
При успешном выполнении метода возвращается сообщение `RATING_RESULT`:
Пример
Описание
```
{  
"messageId":1605196199186625000,  
"sessionId":"0062530b-5521-42cc-90b0-a9d65dea4e98",  
"messageName":"RATING_RESULT",  
"payload":{  
"rating":{  
"estimation":5  
},  
"status_code":{  
"code":1,  
"description":"SUCCESS"  
}  
},  
"uuid":{  
"userId":"ec8a9097-1508-4bec-8d97-67f2329c03e0"  
}  
}  

```

messageId
number
Идентификатор сообщения
sessionId
uuid4
Идентификатор сессии
messageName
string
По умолчанию: `RATING_RESULT`
Название сообщения. В ответ на сообщение `CALL_RATING` приходит сообщение `RATING_RESULT`.
**
payload
**
object
Результат оценки
**
rating
**
object
Информация об оценке
estimation
number
Пользовательская оценка. От 1 до 5
**
status_code
**
object
Описание ответа
code
number
**Возможные значения:** [`1`, `101`, `104`]
Код ответа
description
string
**Возможные значения:** [`SUCCESS`, `SKIP BY USER`, `FORBIDDEN`]
Статус ответа. Возможные значения:
    * `SUCCESS` — Получена оценка от пользователя. Соответствует коду `1`
    * `SKIP BY USER` — Пользователь отклонил выставление оценки или закрыл приложение. Соответствует коду `101`
    * `FORBIDDEN` — Запрет на вызов сервиса по прочим причинам. Соответствует коду `104`
**
uuid
**
object
userId
uuid4
Идентификатор пользователя

Доступ к полю с кодом состояния можно получить с помощью точечной нотации: `status_code.code`.
### Обработка ответа
Для обработки ответа `RATING_RESULT` добавьте в стейт, куда будет возвращен пользователь после оценки или отказа, строку:
```
event!: RATING_RESULT  

```