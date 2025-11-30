# function newSession(object)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
[](https://public.oprosso.sberbank.ru/p/docs_csi_2025)
Метод предназначен для явного создания новой сессии из скрипта.
Вы можете использовать [метод `$jsapi.startSession()` для начала новой сессии](./start-session.md) и [метод `$jsapi.stopSession()` для завершения сессии](./stop-session.md).
  

##### Примеры значений
```
state: reset  
        q!: reset  
        script:  
            $jsapi.newSession({message: "/start", data: $request.data});  

```

[Подробнее о сессиях: session lifetime control](../../session-lifetime-control.md)