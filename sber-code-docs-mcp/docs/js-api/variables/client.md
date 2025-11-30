# $client
Обновлено 16 июня 2025
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Объект для сохранения постоянных данных о клиенте.
После завершения всех реакций, структура `$client` сохраняется во внутренней базе данных. Не имеет особых полей.
[Существует ограничение на объем хранящихся данных в объектe `$client`](../overflow-session-client-data.md). При превышении лимита текущий сценарий прерывается, смартап перестает отвечать клиенту.
  

##### Примеры значений
```
state: Welcome  
    script:  
      $context.session = {}  
      var $session = $context.session;  
      $client.welcome = true;  

```

```
if: !$client.registered  
            go!: /Registration/Start  
        else:  
            go!: /Welcome  

```

Если клиент был неактивен в течение 12 месяцев, его контекстные данные будут очищены.