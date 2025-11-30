# $session
Обновлено 16 июня 2025
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/SmartAppAPI.png)SmartApp API ](https://developers.sber.ru/docs/ru/va/api/overview)
Объект, который хранит данные о сессии пользователя. Данные перезаписываются в начале новой сессии.
Новая сессия создается в сценарии с помощью тега реакций [`newSession`](../../sa-dsl/tags/reaction-tags.md#teg-new-session3).
Объект `$session` хранит [ограниченное количество данных](../overflow-session-client-data.md). При превышении объема текущий сценарий прерывается, смартап перестает отвечать клиенту.
## Контекст диалога
Контекст диалога хранится в поле `contextPath`. Данные поля используются для восстановления контекста при следующем запросе пользователя.
## Примеры
Получение текста последнего запроса пользователя:
```
theme: /  
  
    state: Start  
        q!: $regex</start>  
        a: Начнем.  
  
    state: Приветствие  
        intent!: /привет  
        a: Вы сказали {{$session.rawRequest.textRequest.text}}  

```

Получение информации об имени из системной сущности:
```
require: zenflow.sc  
  module = sys.zfl-common  
  
 state: Hello  
        q!: * меня зовут $Name *  
        script:  
            $session.name = $parseTree._Name  
        a: Привет, {{ $session.name }}!  

```

Получение идентификатора пользователя:
```
require: zenflow.sc  
  module = sys.zfl-common  
  
theme: /  
  
    state: Fallback  
        event!: noMatch  
        a: Идентификатор пользователя: {{$session.userId}}  

```

Для получения идентификатора пользователя с помощью переменной `$session` в проект необходимо подключить библиотеку [`zfl-common`](https://developers.sber.ru/docs/ru/va/chat/script/project-export-import#sistemye-intenty4).
Идентификатор пользователя также можно получить из [запроса пользователя](./request.md).
Если клиент был неактивен в течение 12 месяцев, его контекстные данные будут очищены.