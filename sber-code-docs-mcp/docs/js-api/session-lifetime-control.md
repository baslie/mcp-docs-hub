# Настройка времени сессии в приложении
Обновлено 21 мая 2024
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Сессия — последовательность взаимодействий клиента со смартапом, использующая единый контекст беседы.
Сессия стартует в момент первого обращения клиента к системе в случае, когда для данного пользователя нет другой активной сессии.
Причины завершения сессии:
  * истечение таймаута;
  * выключение/включение устройства;
  * решение вопроса пользователя, подтвержденное выставлением оценки в форме обратной связи, и пр.

Условия завершения сессии различны для каждого смартапа. Конфигурация условий находится на уровне сценария, который должен определять момент завершения старой сессии и начала новой. Это достигается при помощи использования реакции `newSession`.
Реакция `newSession` выбрасывает специальное исключение. При отлове такого исключения записывается лог и создается новая сессия.
## Параметры
  * `message` — стартовое сообщение, будет передано сценарию сразу после активации сессии. Если параметр не задан, будут выполнены только реакции корневой темы.

```
$reactions.newSession({message: $context.request.query,data: $context.request.data});  

```

  * `session` — данные для новой сессии. По умолчанию равен пустому объекту.

```
{timezone:"GMT+3"}  

```

  * `client` — данные клиента, можно модифицировать в новой сессии текущие или сбросить.

```
theme:/  
init:  
bind("postProcess",function($context){  
if($context.session.startNewSession){  
                $reactions.newSession({message:'newSessionMessage',client:{}});  
}  
});  
state:  
        q!: test  
script:  
            $session.startNewSession=true;  
            $context.client.clientCustomData='testClientQuery';  
a:Test answer  
state:  
        q!: newSessionMessage  
a:Messagefromnewsession request {{$client.clientCustomData}}  

```

  * `request` — исходный запрос можно модифицировать в новой сессии. Например поменяв/указав `event` или `query`: `{event: 'new event'}`.

```
theme:/  
init:  
bind("postProcess",function($context){  
if($context.session.startNewSession){  
var $request = $context.request;  
                $request.event='newSessionEvent';  
                $reactions.newSession({request: $request});  
}  
});  
state:  
        q!: test  
script:  
            $session.startNewSession=true;  
a:Test answer  
state:  
event: newSessionEvent  
script:  
a:Eventfromnewsession request  

```

## Примеры значений
  * Создание новой сессий по таймауту.

```
theme:/  
init:  
bind("postProcess",function($context){  
            $context.session.lastActiveTime= $jsapi.currentTime();  
log($context.session.lastActiveTime)  
});  
  
bind("preProcess",function($context){  
if($context.session.lastActiveTime){  
var interval = $jsapi.currentTime()- $context.session.lastActiveTime;  
if(interval >10000){  
                    $reactions.newSession({message:'test 6',session: $context.request.data});  
}  
}  
});  

```

  * Создание новой сессий по событию.

```
theme:/  
state:  
        q!: restart  
a:newsession request  
  
state:  
event: newSessionEvent  
script:  
            $reactions.newSession({message:'restart'});  
a:Test answer  

```

## Методы для управления сессией
Также вы можете использовать следующие методы для управления сессией:
  * [`$jsapi.newSession(object)` предназначен для создания новой сессии из скрипта](./services/jsapi/new-session.md);
  * [`$jsapi.startSession()` начинает новую сессию](./services/jsapi/start-session.md);
  * [`$jsapi.stopSession()` завершает сессию](./services/jsapi/stop-session.md).