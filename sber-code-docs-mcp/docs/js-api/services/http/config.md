# function config(settings)
Обновлено 7 июля 2025
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Метод позволяет задать настройки по умолчанию для http-клиента.
Метод можно использовать только внутри тега [init:](../../../sa-dsl/tags/declarative-tags.md#init2).
Параметр `settings` может содержать набор следующих необязательных полей:
  * `authService` — объект в котором указывается название сервиса данные для авторизации запроса к нему. Содержит следующие поля:
    * `service` — строка с названием сервиса, к которому осуществляется доступ:
      * Для доступа к сервисам SmartPush и SmartProfile используйте значение `smartServices`.
    * `name` — имя переменной, которая будет передаваться в заголовке или теле запроса для авторизации.
    * `value` — значение переменной для авторизации в виде строки, заданное с помощью [переменной из раздела **Токены**](https://developers.sber.ru/docs/ru/va/chat/script/data/token-management).
    * `settingType` — строка, которая указывает часть запроса, где будет передаваться переменная для авторизации. Возможные значения:
      * `QUERY` — переменная будет передаваться в теле запроса.
      * `HEADER` — переменная будет передаваться в заголовке запроса.
    * `app_key` — ключ пространства в виде строки, заданный с помощью переменной из раздела **Токены**. Не указывайте параметр, если хотите использовать системные настройки.
    * `app_secret` — секрет пространства в виде строки, заданный с помощью переменной из раздела **Токены**. Не указывайте параметр, если хотите использовать системные настройки.
    * `client_id` — идентификатор пользователя сервиса в виде строки, заданный с помощью переменной из раздела **Токены**. Параметр используется для ручной настройки авторизации запросов к SmartPush. Не указывайте параметр, если хотите использовать системные настройки.
    * `secret` — секрет пространства в виде строки, заданный с помощью переменной из раздела **Токены**. Параметр используется для ручной настройки авторизации запросов к SmartPush. Не указывайте параметр, если хотите использовать системные настройки.
    * `scope` — скоуп действия параметров авторизации в виде строки. Для работы с сервисом SmartPush указывайте значение `SMART_PUSH`.
  * `url` — объект, позволяет задать базовый `url`, относительно которого будет строиться итоговый `url` при вызове `$http.query` с относительным `url`. Должен содержать обязательные поля:
    * `protocol` — протокол, поддерживаются http и https;
    * `host` — url-хост;
    * `port` — url-порт.
  * `timeout` — максимальное время выполнения запроса после установки http-соединения в миллисекундах.
  * `authHeader` — заголовок авторизации.
  * `cacheTimeToLiveInSeconds` — время в секундах, на которое кэшируются http-ответы, при вызове `$http.query` с указанием необходимости кэширования вызова. Является обязательным параметром для использования http-кэша.

## Примеры значений
  * Авторизации запросов к SmartPush с использованием системных настроек:

```
init:  
    $http.config({  
authService:{  
service:'smartServices',  
},  
});  

```

  * Параметры ручной авторизации запросов к сервисам SmartPush:

```
init:  
    $http.config({  
authService:{  
service:'platformV',  
client_id:'$smartClientid',// переменная из раздела Токены  
secret:'$smartSecret',// переменная из раздела Токены  
scope:'SMART_PUSH',  
},  
});  

```

  * Указываем конфигурацию по умолчанию. В запросах прописываем только путь/параметры.

```
init:  
    $http.config({  
cacheTimeToLiveInSeconds:1*60*30  
});  
  
state:Weather  
    q!: Сколько градусов в питере  
script:  
var url = "https://api.apixu.com/v1/current.json?key=d43686318b1647dabb8181701181811&q=saint%20petersburg”;  
var settings ={  
method:"GET",  
cachingRequired:true  
};  
var response = $http.query(url, settings);  
if(response.isOk){  
            $temp.degree= response.data.current.temp_c;  
}  
a: Сейчас в Питере {{ $temp.degree}}°C.  
  

```

  * Установка времени жизни объектов кэша.

```
init: $http.config({  
cacheTimeToLiveInSeconds:2,  
});  

```

  * Установка базового `url` и вызов `http://example.com/path`.

```
init:  
    $http.config({  
url:{  
protocol:'http',  
host:'example.com',  
port:'80'  
}  
});  
state:  
    q!:*  
script:  
        $http.get('/path');  

```

  * Установка таймаута вызова в 1 секунду и заголовка авторизации.

```
init:  
    $http.config({  
timeout:1000,  
authHeader:'Basic VXNlcm5hbWU6UGFzc3dvcmQ='// для basic авторизации  
authHeader:'Bearer 1/mZ1edKKACtPAb7zGlwSzvs72PvhAbGmB8K1ZrGxpcNM'// для OAuth авторизации  
});  

```

  * Передача данных авторизации в заголовке:

```
init:  
    $http.config({  
authService:{  
service:'external',  
name:'auth_header_name',  
value:'$external_auth_secret',  
settingType:'HEADER',  
},  
});  

```

  * Передача данных авторизации в query-параметре:

```
init:  
    $http.config({  
authService:{  
service:'external',  
name:'auth_query_name',  
value:'$external_auth_secret',  
settingType:'QUERY',  
},  
});  

```

  * Односторонняя аутентификация с помощью TLS:

```
init:  
    $http.config({  
authService:{  
service:'tls',  
cert:'<значение сертификата — переменная из раздела Токены>'  
key:'<значение ключа — переменная из раздела Токены>'  
}  
});  

```

Также доступна двусторонняя аутентификация запроса (протокол TLS + заголовок Authorization).
Это возможно сделать двумя способами.
  * Указать authService в виде массива:

```
var settings ={  
authService:[{  
service:"tls",  
cert:"$public_key",  
key:"$private_key"  
},  
{  
service:"external",  
name:"Authorization",  
value:"$personSearchToken",  
settingType:"HEADER"  
}],  
headers:{  
"content-type":"application/json; charset=UTF-8"  
},  

```

`authService` также может являться массивом.
  * Использовать в `$http` токены в headers или query параметрах:

```
var settings ={  
authService:{  
service:"tls",  
cert:"$public_key",  
key:"$private_key"  
},  
headers:{  
"Authorization":'$personSearchToken',  
"content-type":"application/json; charset=UTF-8"  
},  

```

Для сертификатов поддерживается только формат [pkcs8 ](https://en.wikipedia.org/wiki/PKCS_8).
Если у сертификата формат `rsa`, его можно сконвертировать в формат `pem` с помощью библиотеки [openssl ](https://docs.openssl.org/master/man1/openssl-pkcs8/):
`openssl rsa -in <path-to-key-file> -outform pem -out <path-to-pem-file>`,
а затем получившийся ключ сконвертировать в формат `pkcs8`:
`openssl pkcs8 -topk8 -nocrypt -in xxx.key -out xxx_PKCS8.key`.