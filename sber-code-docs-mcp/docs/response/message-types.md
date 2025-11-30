# Типы сообщений в Code
Обновлено 16 июля 2025
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/ChatApp.png)Chat App ](https://developers.sber.ru/docs/ru/va/chat/title-page)
## text
Простой текстовый ответ, каждый элемент выводится отдельным сообщением.
### Параметры
  * `text` — текст ответа, который будет показан в диалоге;
  * `tts` — задает голосовую реплику ассистента без разметки синтеза речи;
  * `ssml` — задает голосовую реплику ассистента c [разметкой ssml](https://developers.sber.ru/docs/ru/va/chat/voice-interface/speech-synthesis/ssml/overview) для синтеза речи;
  * `auto_listening` — указывает будет ли смартап слушать ответ пользователя после ответа ассистента.

Убедитесь, что в тексте для голосового ассистента нет символов, предназначенных для визуального оформления текста, которые могут помешать корректному синтезу текста. Подробнее о проектировании сценария смартапа читайте в разделе [Проектирование интерфейса](https://developers.sber.ru/docs/ru/va/about/app-design/concepts).
### Синтаксис
```
{  
"type":"text",  
"text":"string",  
"tts":"string",  
"ssml":"string",  
"auto_listening": boolean  
}  

```

В тексте ответа можно использовать подстановки и функции, в рамках тега `a:` и в `$reaction.answer`. Внутри скобок `{{ }}` может находиться любое валидное выражение на JavaScript, можно использовать те же переменные и функции, что и в скриптах.
### Использование в сценарии
Добавление ответа в `$response`:
```
script:var reply ={  
type:'text',  
text:'мой ответ',  
};  
$response.replies= $response.replies||[];  
$response.replies.push(reply);  

```

Модификация ответов. В примере используется [`postProcess`](../js-api/pre-post-process.md). Если ответ повторяется, чат-бот заменит его на фразу «Что-то я повторяюсь».
```
init:  
bind("postProcess",function($context){  
var currentAnswer = $context.response.replies.reduce(function(allAnswers, reply){  
            allAnswers += reply.type==="text"? reply.text:"";  
return allAnswers;  
},"");  
  
if($context.session.lastAnswer=== currentAnswer){  
            $context.response.replies=[  
{  
"type":"text",  
"text":"Что-то я повторяюсь"  
}  
];  
}  
        $context.session.lastAnswer= currentAnswer;  
});  
  
theme:/  
state:  
        q!: как твои дела  
a: У меня все хорошо!  
a: А у тебя как?  

```

## buttons
Тип ответа `buttons` добавляет кнопки в диалоге с пользователем.
Кнопки могут содержать ссылки на внешние адреса или на [состояния сценария](../sa-dsl/tags/declarative-tags.md#state2).
### Параметры
  * `text` — название кнопки.
  * `url` — ссылка.
  * `force_reply` — отключает ввод текста.

### Синтаксис
```
{  
"type":"buttons",  
"buttons":[  
{  
"text":"Переход по адресу",  
"url":"https://example.com",  
"force_reply":true  
},  
{  
"text":"Другая кнопка"  
}  
]  
}  

```

Чтобы добавить переход к состоянию, данные тега `buttons` должны соответствовать шаблону `<json-node> -> <string>`. В левой части валидный JsonNode — строка или объект, определяющие название подсказки. В правой части — строка, определяющая путь до [состояния](../sa-dsl/tags/declarative-tags.md#state2), в которое перейдет смартап по нажатию кнопки.
```
state:Buttons  
        q!:* start  
a: Подсказка внизу экрана  
buttons:  
"Название подсказки"->/NormalButtons/2//после стрелки указывается путь до состояния, в которое будет совершен переход  

```

Кнопки могут содержать подстановку параметров в имени и указанном пути для перехода.
```
state:Buttons  
        q!:* start  
a: Подстановка параметров в подсказках:  
buttons:  
"Имя кнопки"->/NormalButtons/2  
"подстановка параметров как в {{ 'имени' }} так и в пути для перехода"->{{'./3'}}  

```

Переход на внешний адрес задается в подсказке следующим образом:
```
state:  
a: Нажмите подсказку, чтобы перейти на адрес  
buttons:  
{text:"Перейти","url":"https://example.com"}  

```

Отключение ввода текста в чате с пользователем:
```
state:  
a: Нажмите кнопку.Сейчас вы не можете писать в чате.  
buttons:  
{text:"Перейти","url":"https://example.com","force_reply":"true"}  

```

### Использование в сценарии
Две подсказки с переходом к [состоянию смартапа](../sa-dsl/tags/declarative-tags.md#state2) и переходом на внешний адрес (ввод текста отключен):
```
state:  
a: Текст сообщения  
buttons:  
"Привет"->../Hello  
{"text":"Отправить контакты","url":"https://example.com"}  
{"text":"Продолжить","force_reply":"true"}  

```

Подсказки заданные с помощью тега `script`:
```
script:var reply ={  
type:'buttons',  
buttons:[  
{  
text:'Переход по адресу',  
url:'https://example.com',  
force_reply:true//отключение ввода текста в чате с пользователем  
},  
{  
text:'Переход к стейту',  
},  
],  
};  
$response.replies= $response.replies||[];  
$response.replies.push(reply);  

```

## image
Вывод изображения.
### Параметры
  * `imageUrl` — веб-адрес изображения из раздела **Контент**.
  * `hash` — хэш изображения из раздела **Контент**.

### Синтаксис
```
{  
"type":"image",  
"imageUrl":"веб-адрес изображения из раздела Контент",  
"hash":"хэш изображения из раздела Контент"  
}  

```

### Использование в сценарии
```
script: $response.replies= $response.replies||[];  
$response.replies.push({  
type:'image',  
imageUrl:'https://testimageurl.jpg',  
hash:'5debe321a4cc700c9ba138edd5e98f71',  
});  

```

## card
Ответ ассистента в виде карточки.
Карточки недоступны в проектах SaluteBot.
### Параметры
  * `title` — обязательное поле, которое содержит текст заголовка карточки. Позволяет использовать переменные сценария;
  * `description` — описания карточки, которое отображается под заголовком. Рекомендуемая длина описания — менее 50 символов. Позволяет использовать переменные сценария;
  * `imageUrl` — ссылка на изображение из раздела **Контент** ;
  * `hash` — хэш изображения из раздела **Контент** ;
  * `button` — кнопка, которая отображается в карточке;
  * `button.text` — текст кнопки.
  * `button.url` — url, на который выполняется переход по нажатию кнопки.
  * `auto_listening` — указывает будет ли смартап слушать ответ пользователя после ответа ассистента.

### Синтаксис
```
{  
"type":"card",  
"title":"title",  
"description":"descr",  
"imageUrl":"веб-адрес изображения из раздела Контент",  
"hash":"хэш картинки из раздела Контент",  
"button":{  
"text":"text",  
"url":"url"  
},  
"auto_listening":false  
}  

```

### Использование в сценарии
```
script:var reply ={  
type:'card',  
title:'title',  
description:'descr',  
imageUrl:'<url на картинку из раздела Контент>',  
hash:'<hash картинки из раздела Контент>',  
button:{  
text:'text',  
url:'url',  
},  
auto_listening:false,  
};  
$response.replies= $response.replies||[];  
$response.replies.push(reply);  

```

## cardList
Ответ ассистента в виде карточки со списком ячеек.
![Ответ](https://developers.sber.ru/docs/assets/images/list-card-left-right-cell-view-1-26325dbf87e277dd1ae7189680bcd65c.png)
![Ответ](https://developers.sber.ru/docs/assets/images/list-card-left-right-cell-view-2-7549d88f211e8a88af0aeb9139980fef.png)
Списки недоступны в проектах SaluteBot.
### Параметры
Параметры карточки:
  * `title` — обязательное поле, которое содержит текст заголовка карточки. Позволяет использовать переменные сценария;
  * `subtitle` — описание карточки, которое отображается под заголовком. Рекомендуемая длина описания — менее 50 символов. Позволяет использовать переменные сценария;
  * `cells` — массив с объектами, описывающими ячейки карточки;
  * `buttons` — массив кнопок карточки;
  * `auto_listening` — указывает будет ли смартап слушать ответ пользователя после ответа ассистента.

Параметры ячейки:
  * `title` — обязательное поле, которое содержит текст заголовка ячейки;
  * `subtitle` — поле с текстом, который отображается под заголовком ячейки;
  * `value` — обязательное поле, которое содержит текст правой части ячейки. Может содержать переменные сценария.;
  * `iconUrl` — веб-адрес изображения, которое отображается в ячейке;
  * `hash` — хэш изображения ячейки;
  * `action` — действие, которое произойдет при нажатии ячейки;
  * `action.url` — веб-адрес, который откроется при нажатии ячейки;
  * `action.text` — текст, который отправится при нажатии ячейки;
  * `action.then` — путь к [состоянию](../sa-dsl/tags/declarative-tags.md#state2), в которое перейдет смартап при нажатии ячейки.
Имя состояния надо указывать без символа `/`.

### Синтаксис
```
{  
"type":"cardList",  
"title":"Заголовок карточки",  
"subtitle":"Описание",  
"cells":[  
{  
"title":"Заголовок ячейки 1",  
"subtitle":"Описание ячейки 1",  
"value":"Значение, которое отображается в правой части ячейки 1. Рекомендуемая длина менее 5 символов.",  
"iconUrl":"https://example.ru/images/image.png",  
"hash":"3a74d5abfc671f47e45d336ed4d41026",  
"action":{  
"url":"Веб-адрес, который откроется при нажатии ячейки"  
}  
},  
],  
"buttons":[  
{  
"text":"Название кнопки карточки",  
"url":"Веб-адрес, который откроется при нажатии кнопки"  
}  
],  
"auto_listening":false  
}  

```

### Использование в сценарии
```
script:var reply ={  
type:'cardList',  
title:'Заголовок карточки',  
subtitle:'Описание',  
cells:[  
{  
title:'Заголовок ячейки 1',  
subtitle:'Описание ячейки 1',  
value:'Значение, которое отображается в правой части ячейки 1. Рекомендуемая длина менее 5 символов.',  
iconUrl:'https://example.ru/images/image.png',  
hash:'3a74d5abfc671f47e45d336ed4d41026',  
action:{  
url:'Веб-адрес, который откроется при нажатии ячейки',  
},  
},  
{  
title:'Заголовок ячейки 2',  
subtitle:'Описание ячейки 2',  
value:'Значение, которое отображается в правой части ячейки 2. Рекомендуемая длина менее 5 символов.',  
iconUrl:'https://example.ru/images/image.png',  
hash:'3a74d5abfc671f47e45d336ed4d41026',  
action:{  
text:'Текст, который отправится при нажатии ячейки',  
},  
},  
],  
buttons:[  
{  
text:'Название кнопки карточки',  
url:'Веб-адрес, который откроется при нажатии кнопки',  
},  
],  
auto_listening:false,  
};  
$response.replies= $response.replies||[];  
$response.replies.push(reply);  

```

## raw
Используется для передачи настраиваемого типа ответа.
Тестовый виджет не отображает ответы с типом `raw`, если они передаются с помощью `$context.response.replies`.
### Параметры
  * `body` — тело ответа, содержание которого будет добавлено в поле `payload` протокола ассистента. Параметры, идентифицирующие пользователя, подставляются автоматически.

Вы можете передать поле `messageName` и явно указать в нем тип сообщения. Поле `messageName` необязательное и по умолчанию содержит значение `ANSWER_TO_USER`. Примеры сообщений, которые можно использовать в `body` вы найдете в [SmartApp API](https://developers.sber.ru/docs/ru/va/api/smartapp-interface-elements).
### Синтаксис
```
{  
"type":"raw",//тип сообщения  
"body":{ ... },//тело ответа  
"messageName":"ANSWER_TO_USER"//опциональный параметр  
}  

```

### Отправка карточки
Передача карточки типа `grid_card` в диалог с пользователем.
Карточки недоступны в проектах SaluteBot.
```
var reply ={  
type:'raw',  
body:{  
emotion:null,  
items:[  
{  
card:{  
type:'grid_card',  
items:[  
{  
type:'greeting_grid_item',  
top_text:{  
type:'text_cell_view',  
text:'SBER Box',  
typeface:'caption',  
text_color:'default',  
max_lines:3,  
},  
bottom_text:{  
type:'text_cell_view',  
text:'Компактная ТВ-приставка SBER Box – интеллектуальный центр вашего дома',  
typeface:'body3',  
text_color:'default',  
max_lines:3,  
margins:{  
top:'4x',  
},  
},  
paddings:{  
top:'6x',  
left:'6x',  
right:'6x',  
bottom:'6x',  
},  
actions:[  
{  
text:'Подписка Okko в подарок.',  
},  
],  
},  
],  
columns:2,  
item_width:'small',  
},  
},  
],  
},  
messageName:'ANSWER_TO_USER',  
};  
$response.replies= $response.replies||[];  
$response.replies.push(reply);  

```

### Ответ на ошибочный запрос
Если смартап запущен по ошибке и не знает ответа на запрос, вы можете сообщить об этом ассистенту с помощью пустого сообщения [`NOTHING_FOUND`](https://developers.sber.ru/docs/ru/va/api/smartapp-api-responses#nothing-found).
```
$response.replies= $response.replies||[];  
$response.replies.push({  
type:'raw',  
messageName:'NOTHING_FOUND',  
body:{},  
});  

```

При получении такого сообщения ассистент передаст запрос следующему по приоритету смартапу.