# smartGeo в Code
Обновлено 19 февраля 2025
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/SmartGeo.png)SmartGeo ](https://developers.sber.ru/docs/ru/va/smartservices/smartgeo/overview)
Сервис для получения данных о местоположении пользователей с их согласия.
Перед использованием сервиса, ознакомьтесь с [условиями подключения сервиса SmartGeo](https://developers.sber.ru/docs/ru/va/smartservices/smartgeo/integration). С принципом работы, типами сообщений и кодами ошибок можно ознакомиться в разделе [API SmartGeo](https://developers.sber.ru/docs/ru/va/smartservices/smartgeo/api).
Сервис недоступен в проектах SaluteBot. Проверить работу сервиса в тестовом виджете нельзя.
## Методы
### getProfileData
Возвращает данные из профиля пользователя.
Пример вызова:
```
script: $smartProfile.getProfileData();  

```

## Пример ответа
Пример запроса данных пользователя можно посмотреть в [демонстрационном приложении](https://developers.sber.ru/docs/ru/va/smartservices/smartprofile/example).
При успешном выполнении методов возвращается [сообщение](https://developers.sber.ru/docs/ru/va/smartservices/smartgeo/api#format-otveta27) `TAKE_PROFILE_DATA`.
Пример
Описание
```
{  
"messageId":1605196199186625000,  
"sessionId":"0062530b-5521-42cc-90b0-a9d65dea4e98",  
"uuid":{  
"userId":"ec8a9097-1508-4bec-8d97-67f2329c03e0",  
"userChannel":"B2C"  
},  
"messageName":"TAKE_PROFILE_DATA",  
"payload":{  
"device":{},  
"profile_data":{  
"geo":{  
"reverseGeocoding":{  
"country":"Российская Федерация",  
"region_id":20666588000,  
"region":"Ненецкий автономный округ",  
"subregion_id":23575664000,  
"subregion":"Заполярный район",  
"city_id":27720392000,  
"city":"Верхний Шар"  
},  
"location":{  
"accuracy":100,  
"lat":50.125,  
"lon":70.0124,  
"timestamp":1432233446145000,  
"source":"gps"  
}  
}  
},  
"status_code":{  
"code":1,  
"description":"SUCCESS"  
}  
}  
}  

```

messageId
string
Идентификатор сообщения
sessionId
string
Идентификатор сессии
**
uuid
**
object
userId
string
Идентификатор пользователя
userChannel
string
Идентификатор канала коммуникации
messageName
string
Название сообщения
**
payload
**
object
Тело сообщения
device
object
Данные об устройстве
**
profile_data
**
object
Данные профиля пользователя
**
geo
**
object
Данные о положении устройства пользователя
**
reverseGeocoding
**
object
Декодированные данные о положении устройства пользователя
country
string
Страна
region_id
int64
Идентификатор региона
region
string
Название региона
subregion_id
int64
Идентификатор субрегиона
subregion
string
Название субрегиона
city_id
int64
Идентификатор города
city
string
Название города
**
location
**
object
Координаты устройства
accuracy
int32
Точность опредления положения
lat
number
Широта
lon
number
Долгота
timestamp
int64
Unix-время
source
string
Название источника данных
**
status_code
**
object
code
int32
**Возможные значения:** [`1`, `101`, `102`]
Код ответа
description
string
**Возможные значения:** [`SUCCESS`, `CLIENT DENIED`, `FORBIDDEN`]
Описание ответа. Возможные значения:
    * `SUCCESS` — Данные существуют и получено согласие пользователя. Соответствует коду `001`
    * `CLIENT DENIED` — Пользователь отклонил автозаполнение. Соответствует коду `101`
    * `FORBIDDEN` — Этот смартап не может использовать сервис SmartGeo. Соответствует коду `102`

После получения сообщения `TAKE_PROFILE_DATA` необходимо его обработать с помощью тега `event:`. Затем данные о местоположении сохранятся в поле `{{data.eventData.profile_data.geo }}` системной переменной `{{$request }}`.
Теперь можно вывести, например, страну местонахождения пользователя:
```
state:  
event!: TAKE_PROFILE_DATA  
a:Вы находитесь в:  
{{$request.data.eventData.profile_data.geo.reverseGeocoding.country}}  

```

Также необходимую информацию можно получить с помощью выражения:
```
$request.rawRequest.payload.profile_data.geo.reverseGeocoding.country  

```

Оно выведет данные напрямую из поля `rawRequest.payload.profile_data.geo` системной переменной `$request`. Значительной разницы между вариантами доступа к данным нет.