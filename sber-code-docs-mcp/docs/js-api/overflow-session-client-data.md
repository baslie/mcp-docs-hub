# Превышение лимита объектов $session и $client в Code
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Существует ограничение на объем хранящихся данных в объектах `$session` и `$client`. При превышении лимита текущий сценарий прерывается, смартап перестает отвечать клиенту.
  * [`$client` — объект для сохранения постоянных данных о клиенте](./variables/client.md).
  * [`$session` — объект для сохранения сессионных данных](./variables/session.md).

Для того, чтобы сценарий не прерывался, необходимо обрабатывать переполнение данных объектов `$session` и `$client` в сценарии.
## Лимиты
По умолчанию установлены лимиты:
  * `soft` 100 Кб;
  * `hard` 1000 Кб.

Обратите внимание, что лимиты установлены для каждого объекта. Таким образом для данных объекта `$client` по `soft` лимиту доступно 100 Кб, для данных объекта `$session` также доступно 100 Кб.
## Обработка переполнения
Если достигнут `soft` лимит, но при этом не превышен `hard` лимит, данные в объекты `$session` и `$client` будут сохраняться. При этом в сценарий приходят события о достижении `soft` лимита `event: sessionDataSoftLimitExceeded` и `event: clientDataSoftLimitExceeded`.
Если новые данные превышают `hard` лимит, то эти данные не сохраняются в объекты `$session` и `$client`. При этом в сценарий приходят события о достижении `hard` лимита `event: sessionDataHardLimitExceeded` и `event: clientDataHardLimitExceeded`.
Пример обработки переполнения данных в сценарии:
```
theme: /  
  
    state:  
        q: * *start  
        go!: /start  
  
    state: start  
        q!: *  
        script:  
            $session.text = $parseTree.text    // сохраняем данные сессии  
        a: Вы сказали: {{$parseTree.text}}.  
  
    state:  
        event: sessionDataSoftLimitExceeded    // обрабатываем событие о достижении soft лимита  
        script:  
            delete $session.text;               // при достижении soft лимита сессионные данные удаляются  

```