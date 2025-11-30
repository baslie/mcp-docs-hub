# smartProfile в Code
Обновлено 19 февраля 2025
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/SmartProfile.png)SmartProfile ](https://developers.sber.ru/docs/ru/va/smartservices/profile)
Сервис для получения данных пользователей с их согласия.
Перед использованием сервиса, ознакомьтесь с [условиями подключения сервиса SmartProfile](https://developers.sber.ru/docs/ru/va/smartservices/smartprofile/integration). С принципом работы, типами сообщений и кодами ошибок можно ознакомиться в разделе [API SmartProfile](https://developers.sber.ru/docs/ru/va/smartservices/smartprofile/api).
Сервис недоступен в проектах SaluteBot. Проверить работу сервиса в тестовом виджете нельзя.
## Методы
### getProfileData
Возвращает данные из профиля пользователя.
Пример вызова:
```
script: $smartProfile.getProfileData();  

```

### chooseProfileData
Позволяет изменить адрес доставки, телефонный номер и адрес электронной почты пользователя.
Пример вызова:
```
script:  
var payload ={  
"changeAddress":true,  
"changePhone":true,  
"changeEmail":true,  
}  
  
   $smartProfile.chooseProfileData(payload)  

```

Параметры метода:
  * `changeAddress` — обязательное поле. Логический тип. Может принимать значения `true` или `false`. Указывает на необходимость изменения адреса доставки.
  * `changePhone` — обязательное поле. Логический тип. Может принимать значения `true` или `false`. Указывает на необходимость изменения телефонного номера заказчика.
  * `changeEmail` — обязательное поле. Логический тип. Может принимать значения `true` или `false`. Указывает на необходимость изменения адреса электронной почты заказчика.

### detailedProfileData
Предлагает пользователю уточнить данные адреса. Например, указать подъезд или этаж.
Пример вызова:
```
script: $smartProfile.detailedProfileData();  

```

## Пример ответа
Пример запроса данных пользователя можно посмотреть в [демонстрационном приложении](https://developers.sber.ru/docs/ru/va/smartservices/smartprofile/example).
При успешном выполнении методов возвращается сообщение [`TAKE_PROFILE_DATA`](https://developers.sber.ru/docs/ru/va/smartservices/smartprofile/api#format-otveta29).
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
"customer_name":"Иван",  
"surname":"Иванов",  
"patronymic":"Иванович",  
"birthDate":"01.01.2000",  
"phone_number":79161234567,  
"email":"ivanov@site.ru",  
"address":{  
"location":{  
"latitude":56.77,  
"longitude":23.88  
},  
"address_string":"Кутузовский пр-т 32",  
"country":"Россия",  
"region":"Москва",  
"city":"Москва",  
"settlement":"Поселок",  
"district":"Ленинский",  
"street":"Кутузовский проспект",  
"house":32,  
"building":1,  
"floor":12,  
"entrance":3,  
"apartment":134,  
"door_code":134,  
"alias":"Офис в Москве",  
"comment":"Дома после 18 часов",  
"address_type":"Рабочий"  
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
device
object
**
profile_data
**
object
customer_name
string
Имя
surname
string
Фамилия
patronymic
string
Отчество
birthDate
string
Дата рождения
phone_number
string
Номер телефона
email
string
Адрес электронной почты
**
address
**
object
Данные адреса
**
location
**
object
Географические координаты
latitude
string
Широта
longitude
string
Долгота
address_string
string
Строка с данными адреса
country
string
Страна
region
string
Регион
city
string
Город
settlement
string
Тип населенного пункта
district
string
Район
street
string
Улица
house
string
Дом
building
string
Строение
floor
string
Этаж
entrance
string
Подъезд
apartment
string
Номер квартиры или офиса
door_code
string
Код подъезда
alias
string
Название адреса
comment
string
Комментарий
address_type
string
Тип адреса
**
status_code
**
object
code
int32
**Возможные значения:** [`1`, `100`, `101`, `102`, `103`, `104`]
Код ответа
description
string
**Возможные значения:** [`SUCCESS`, `EMPTY DATA`, `CLIENT DENIED`, `FORBIDDEN`, `FORBIDDEN REQUEST`, `ACCESS DENIED`]
Описание ответа. Возможные значения:
    * `SUCCESS` — Данные существуют и получено согласие пользователя. Соответствует коду `001`
    * `EMPTY DATA` — Данные отсутствуют в профиле. Соответствует коду `100`
    * `CLIENT DENIED` — Пользователь отклонил автозаполнение. Соответствует коду `101`
    * `FORBIDDEN` — Запрещенный вызов от смартапа для `GET_PROFILE_DATA`. Соответствует коду `102`
    * `FORBIDDEN REQUEST` — Запрещенный вызов от смартапа для `CHOOSE_PROFILE_DATA` и `DETAILED_PROFILE_DATA` при отсутствии согласия пользователя. Соответствует коду `103`
    * `ACCESS DENIED` — Запрещенный вызов от смартапа для `CHOOSE_PROFILE_DATA` и `DETAILED_PROFILE_DATA` при отсутствии прав на изменение или уточнение данных. Соответствует коду `104`

После получения сообщения `TAKE_PROFILE_DATA` необходимо его обработать с помощью тега `event:`. Затем данные профиля сохранятся в поле `{{data.eventData.profile_data }}` системной переменной `{{$request }}`.
Теперь можно вывести, например, номер телефона:
```
state:  
  
    event!: TAKE_PROFILE_DATA  
  
    a: Номер телефона: {{$request.data.eventData.profile_data.phone_number}}  

```

Также необходимую информацию можно получить с помощью выражения:
```
$request.rawRequest.payload.profile_data.phone_number  

```

Это выражение выведет данные напрямую из поля `rawRequset.payload.profile_data` системной переменной `$request`.
Значительной разницы между вариантами доступа к данным нет.