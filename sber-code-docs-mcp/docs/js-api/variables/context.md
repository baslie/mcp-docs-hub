# $context
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Представляет собой текущий контекст выполнения запроса и содержит в себе ссылки на все другие JS-объекты, передаваемые при вызове скрипта, а также несколько специальных полей.
Переменные в объекте `$context` содержатся с таким же именем, но без префикса `$`.
```
$context.parseTree= $parseTree;  
$context.client= $client;  

```

  

##### Дополнительные поля
  * `currentState` — путь текущего состояния, в котором выполняется скрипт. Изменение значения `currentState` не повлияет на текущий стейт. Если нужно повлиять на стейт используйте обработчик [`preProcess`](../pre-post-process.md).
  * `contextPath` — текущий путь контекста, может отличаться от `currentState`, в случае, когда используется флаг `noContext`.
  * `contextHistory` — данные прошлого стейта.
  * `testContext` — контекст выполнения тестов. Объект определен только в режиме тестов и не подлежит модификации из кода скриптов.

  

##### Примеры значений
```
state: Welcome  
        	q!: * *start  
        	a: Привет! Я электронный помощник.  
        	script:  
            	$context.session = {}  
            	$context.client = {}  
            	$context.temp = {}  
            	$context.response = {}  
        	go!: /ChooseCity  

```

```
init:  
    $global.newSession = function($context) {  
        $context.request.data.newSession = true;  
        $context.request.data.client = $context.client;  
        $reactions.newSession({message: $context.request.query, data: $context.request.data});  
    }  

```

  

##### NLU-ядро Brain
Для [NLU-ядра Brain](https://developers.sber.ru/docs/ru/va/chat/voice-interface/command-recognition/nlu_core) доступны также переменны:
  * `$context.intent` — [интент](../../sa-dsl/tags/intents-tags.md), активированный в стейте.
  * `$context.entities` — [сущности](../../nlp/entities/overview.md), найденные во фразе.
  * `$context.nluResults` — массив результатов NLU-ядра .