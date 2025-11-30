# smartPush в Code
Обновлено 15 июля 2025
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Сервис для отправки push-уведомлений на различные поверхности.
Сервис недоступен в проектах SaluteBot.
Перед использованием сервиса:
  1. [Подключите в Studio проект SmartServices](https://developers.sber.ru/docs/ru/va/smartservices/smartprofile/integration#kak-sozdat-proekt-smart-service).
  2. [Получите доступы к SmartPush](https://developers.sber.ru/docs/ru/va/smartservices/smartpush/integration).
  3. [Создайте шаблон push-уведомлений](https://developers.sber.ru/docs/ru/va/smartservices/smartpush/push-template#sozdanie-shablona).

Для использования сервиса в проект надо [подключить скрипт](https://developers.sber.ru/docs/ru/va/chat/script/preload-js) `smartPush.js`:
```
scriptsPreLoad:  
global:  
- /jsapi/smartPush.js  

```

## Получение разрешения
Запрос разрешения на отправку push-уведомлений передается с помощью метода `getRuntimePermissions()`:
```
$smartPush.getRuntimePermissions()  

```

В ответ на запрос возвращается сообщение `TAKE_RUNTIME_PERMISSIONS`:
```
{  
"messageId":"1605196199186625000",  
"sessionId":"0062530b-5521-42cc-90b0-a9d65dea4e98",  
"messageName":"TAKE_RUNTIME_PERMISSIONS",  
"payload":{  
"permitted_actions":[  
"service_push"  
],  
"status_code":{  
"code":1,  
"description":"success"  
}  
},  
"uuid":{  
"userId":"ec8a9097-1508-4bec-8d97-67f2329c03e0",  
"userChannel":"B2C"  
}  
}  

```

Тело сообщения сохраняется в поле `data.eventData` системной переменной `$request`. Например, код ответа можно получить обратившись к полю `code`:
```
$request.data.eventData.payload.status_code.code  

```

Поле `code` может содержать значения:
## Отправка уведомлений
Уведомления отправляются с помощью метода `send()`:
```
$smartPush.send(deliveryConfig, authConfig);  

```

Где:
  * `authConfig` — обязательный параметр с настройками авторизации:
    * `client_id` — идентификатор пользователя сервиса в виде строки, заданный с помощью переменной из раздела [**Токены**](https://developers.sber.ru/docs/ru/va/chat/script/data/token-management). Необязательный параметр. Используйте его для переопределения [системных параметров](https://developers.sber.ru/docs/ru/va/smartservices/smartpush/integration#poluchenie-dostupov-k-smart-push) при ручной настройке авторизации запросов к SmartPush.
    * `secret` — секрет пространства в виде строки, заданный с помощью переменной из раздела **Токены**. Необязательный параметр. Используйте поле для переопределения [системных параметров](https://developers.sber.ru/docs/ru/va/smartservices/smartpush/integration#poluchenie-dostupov-k-smart-push) при ручной настройке авторизации запросов к SmartPush.
    * `scope` — скоуп действия параметров авторизации в виде строки. Необязательный параметр, используется для ручной настройки авторизации запросов к SmartPush. Используйте поле для переопределения [системных параметров](https://developers.sber.ru/docs/ru/va/smartservices/smartpush/integration#poluchenie-dostupov-k-smart-push) при ручной настройке авторизации запросов к SmartPush. Для работы с сервисом указывайте значение `SMART_PUSH`.
  * `deliveryConfig` — обязательный параметр с данными о рассылке. Параметр может содержать либо настройки уведомлений для приложения Салют (`MobileAppParameters`), либо настройки уведомлений для SberBox (`DeviceParameters`). Параметр содержит поля:
    * `DeliveryMode` — обязательное поле с типом распространения уведомления. Возможные значения:
      * `BROADCAST` — уведомление отправляется на все поверхности;
      * `SEQUENTIAL` — уведомление отправляется последовательно по приоритету. Рассылка прекращается при успешной доставке сообщения на одну из поверхностей.
    * `surface` — обязательное поле с названием поверхности, на которой отобразится уведомление. При выборе нескольких поверхностей, для каждой из них формируется объект в массиве `destinations` ([описание формата push-уведомления в API SmartPush](https://developers.sber.ru/docs/ru/va/smartservices/smartpush/api/sending-notifications)). Строка с максимальной длиной 128 символов. Возможные значения:
      * `COMPANION` — мобильное приложение Салют;
      * `SBERBOX` — SberBox;
      * `TIME` — SberBox Time;
      * `TV_HUAWEI` — Huawei Vision;
      * `TV` — Салют ТВ.
    * `TemplateContent` — поле с параметрами уведомления:
      * `id` — обязательный [идентификатор шаблона](https://developers.sber.ru/docs/ru/va/smartservices/smartpush/push-template#sozdanie-shablona) в виде строки. Максимальная длина — 36 символов. Идентификатор должен содержать `templateId` согласованного шаблона.
      * `headerValues` — объект с парами ключ-значение. Значение передается в виде строки. Содержит переменные заголовка push-уведомления для подстановки в шаблон.
      * `bodyValues` — объект с парами ключ-значение. Значение передается в виде строки. Содержит переменные тела push-уведомления для подстановки в шаблон.
      * `MobileAppParameters` — параметры deeplink в push-уведомлениях для приложения Салют. Передается, если заданы соответствующие [параметры шаблона](https://developers.sber.ru/docs/ru/va/smartservices/smartpush/push-template#deeplink). Не передается, если заданы параметры уведомлений для SberBox (`DeviceParameters`). Содержит следующие поля:
        * `buttonText` — текст кнопки. Максимальная длина — 30 символов.
        * `deeplinkAndroid` — сценарий для Android-устройств. Максимальная длина — 350 символов.
        * `deeplinkIos` — сценарий для iOS-устройств. Максимальная длина — 350 символов.
      * `DeviceParameters` — параметры deeplink в push-уведомлениях для SberBox. Передается, если заданы соответствующие [параметры шаблона](https://developers.sber.ru/docs/ru/va/smartservices/smartpush/push-template#deeplink). Не передается, если заданы параметры уведомлений для приложения Салют (`MobileAppParameters`). Содержит следующие поля:
        * `deeplink` — сценарий для SberBox. Максимальная длина — 350 символов.

## Примеры
Отправка push-уведомления в сценарии:
```
script:var deliveryConfig ={  
deliveryMode:'BROADCAST',  
surface:'COMPANION',  
templateContent:{  
id:'49061553-27c7-4471-9145-d8d6137c57da',  
//Переменные заголовка уведомления, заданные в шаблоне  
headerValues:{},  
//Переменные тектса уведомления, заданные в шаблоне  
bodyValues:{},  
mobileAppParameters:{  
deeplinkAndroid:'example-listen-android',  
deeplinkIos:'example-mai-listen-ios',  
buttonText:'Слушать',  
},  
},  
};  
  
//Авторизация вызова  
//Параметр надо передавать, если в проекте не заданы системные токены  
var authConfig ={  
client_id:'$clietnId',  
secret:'$secret',  
scope:'SMART_PUSH',  
};  
  
$smartPush  
.send(deliveryConfig, authConfig)  
.then(function(success){  
        $response.data='success response';  
        $response.status= success.status;  
        $response.response= success.response;  
return success;  
})  
.catch(function(error){  
        $response.data='fail response';  
        $response.status= error.status;  
        $response.response= error.response;  
        $response.error= error.error;  
});  

```