# $response
Обновлено 16 июля 2025
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/SmartAppAPI.png)SmartApp API ](https://developers.sber.ru/docs/ru/va/api/overview)
Объект для заполнения поля `$response` в ответах ассистента.
`$response.replies` — список ответов, выведенных в процессе обработки реакций.
`replies` — массив реплик ассистента, содержащий строго типизированные элементы. Предназначен для передачи ответов.
Массив `replies` может содержать следующие элементы:
  * [`text`](./response.md#text2);
  * [`buttons`](./response.md#buttons2);
  * [`image`](./response.md#image2);
  * [`card`](./response.md#card);
  * [`cardList`](./response.md#card-list);
  * [`raw`](./response.md#raw2).

## text
Текстовый ответ ассистента. Каждый ответ отображается в чате отдельным сообщением. Поддерживает поля:
  * `text` — текст ответа;
  * `tts` — реплика, которую произнесет ассистент. Без разметки для синтеза речи;
  * `ssml` — реплика из поля `tts` c [ssml-разметкой](https://developers.sber.ru/docs/ru/va/chat/voice-interface/speech-synthesis/ssml/overview) для синтеза речи;
  * `markdown` — текст ответа из поля `text`, отформатированный с помощью разметки markdown;
  * `auto_listening` — указывает будет ли смартап слушать ответ пользователя после ответа ассистента.

```
{  
"type":"text",  
"text":"....",  
"tts":"....",  
"ssml":".....",  
"markdown":".....",  
"auto_listening":true  
}  

```

Пример поля `items.bubble`, которое передается в [ответе ассистента](https://developers.sber.ru/docs/ru/va/api/smartapp-api-responses#answer-to-user):
Отображение в чате
Код
![Интерфейс Postman](https://cdn-app.sberdevices.ru/asset/q30/aHR0cHM6Ly9jZG4tYXBwLnNiZXJkZXZpY2VzLnJ1L21pc2MvMC4wLjAvYXNzZXRzL2JzbS1kb2NzL3RleHQtc2FtcGxlLnBuZw==)
```
{  
"text":"Пример сообщения ассистента в чате с пользователем.\n\nВ текстовых ответах можно использовать **markdown-разметку** и добавлять [ссылки](https://developers.sber.ru/)\n\nТекстовые ответы передаются в поле `buble`, в массиве `items` ответов ассистента.",  
"markdown":true  
}  

```

### Поддерживаемые markdown-теги
Доступны следующие элементы форматирования:
Форматирование | Пример кода  
---|---  
Жирный шрифт | ```
**Жирный** шрифт
```
  
Курсив |  ```
_Курсив_
```
или   
```
_Курсив_
```
  
Зачеркнутый шрифт | ```
~~Зачеркнутый~~ шрифт
```
  
Ссылка | ```
текст ссылки[ ](https://example.ru)
```
  
Маркированный список | 
  * Пункт 1  

  * Пункт 2  

  * Пункт 3  

или   

  * Пункт 1  

  * Пункт 2  

  * Пункт 3  

  
## buttons
Кнопки с подсказками в чате с ассистентом.
```
{  
"type":"buttons",  
"buttons":[  
{  
"text":"Переход по адресу",  
"url":"https://example.com"  
},  
{  
"text":"Подсказка"  
}  
]  
}  

```

Пример массива подсказок `suggestions.buttons`, который передается в [ответе ассистента](https://developers.sber.ru/docs/ru/va/api/smartapp-api-responses#answer-to-user):
Отображение в чате
Код
![Интерфейс Postman](https://cdn-app.sberdevices.ru/asset/q30/aHR0cHM6Ly9jZG4tYXBwLnNiZXJkZXZpY2VzLnJ1L21pc2MvMC4wLjAvYXNzZXRzL2JzbS1kb2NzL2J1dHRvbnMtc2FtcGxlLnBuZw==)
```
[  
{  
"title":"Подсказать",  
"action":{  
"text":"Подскажи",  
"type":"text"  
}  
},  
{  
"title":"Ссылка",  
"action":{  
"type":"deep_link",  
"deep_link":"https://developers.sber.ru/"  
}  
}  
]  

```

## image
Вывод изображения.
```
{  
"type":"image",  
"imageUrl":"http://...",  
"hash":"<hash картинки из раздела Контент>"  
}  

```

Изображения должны соответствовать требованиям:
  * Размер — менее 500 Кб;
  * Формат — jpg, png или bmp;
  * Рекомендуемое соотношение сторон — 3:2;
  * Рекомендуемое разрешение — больше 1024 × 682 пикселей.

Пример содержит код карточки типа `list_card`, с помощью которой можно передавать изображения в [ответах ассистента](https://developers.sber.ru/docs/ru/va/api/smartapp-api-responses#answer-to-user):
Отображение в чате
Код
![Пример картинки](https://cdn-app.sberdevices.ru/asset/q30/aHR0cHM6Ly9jZG4tYXBwLnNiZXJkZXZpY2VzLnJ1L21pc2MvMC4wLjAvYXNzZXRzL2JzbS1kb2NzL2ltYWdlLXNhbXBsZS5wbmc=)
```
[  
{  
"bubble":{  
"text":"А вот котенок",  
"markdown":true  
}  
},  
{  
"card":{  
"type":"list_card",  
"cells":[  
{  
"type":"image_cell_view",  
"content":{  
"url":"https://content.sberdevices.ru/smartmarket-smide-prod/1624/1625/D6xsDcXIevOkuW2w.jpg",  
"hash":"388e2adf4f1494c27d1289ec500965d9"  
}  
}  
]  
}  
}  
]  

```

## card
Формирует ответ в виде карточки, которая содержит: заголовок, описание, изображение и кнопку. Содержит обязательное поле поле `title`.
Параметр `auto_listening` указывает будет ли смартап слушать ответ пользователя после ответа ассистента.
```
{  
"type":"card",  
"title":"title",  
"description":"descr",  
"imageUrl":"<url на картинку из раздела Контент>",  
"hash":"<hash картинки из раздела Контент>",  
"button":{  
"text":"text",  
"url":"url"  
},  
"auto_listening":false  
}  

```

Пример карточки `list_card`, которую можно передать в поле `items.card` [ответа ассистента](https://developers.sber.ru/docs/ru/va/api/smartapp-api-responses#answer-to-user):
Отображение в чате
Код
![Интерфейс Postman](https://cdn-app.sberdevices.ru/asset/q30/aHR0cHM6Ly9jZG4tYXBwLnNiZXJkZXZpY2VzLnJ1L21pc2MvMC4wLjAvYXNzZXRzL2JzbS1kb2NzL2NhcmQtc2FtcGxlLnBuZw==)
```
{  
"type":"list_card",  
"paddings":{  
"bottom":"12x"  
},  
"cells":[  
{  
"type":"image_cell_view",  
"content":{  
"url":"https://content.sberdevices.ru/smartmarket-smide-prod/1624/1625/u0pzFUEqQHu5i7qQ.jpg",  
"hash":"e4ea2db5738ca59c627571736c65bcbf"  
}  
},  
{  
"type":"text_cell_view",  
"paddings":{  
"top":"6x",  
"left":"8x",  
"right":"8x"  
},  
"content":{  
"text":"Заголовок карточки",  
"typeface":"title1",  
"text_color":"default"  
}  
},  
{  
"type":"text_cell_view",  
"paddings":{  
"top":"4x",  
"left":"8x",  
"right":"8x"  
},  
"content":{  
"text":"Описание карточки",  
"typeface":"footnote1",  
"text_color":"secondary"  
}  
},  
{  
"type":"text_cell_view",  
"paddings":{  
"top":"12x",  
"left":"8x",  
"right":"8x"  
},  
"content":{  
"actions":[  
{  
"type":"deep_link",  
"deep_link":"https://developers.sber.ru/"  
}  
],  
"text":"Кнопка в карточке",  
"typeface":"button1",  
"text_color":"brand"  
}  
}  
]  
}  

```

## cardList
Формирует ответ в виде карточки со списком, которая содержит: заголовок, подзаголовок, кнопку и список ячеек. Карточка включает обязательный заголовок (`title`), подзаголовок (`subtitle`), а также обязательные массивы ячеек (`cells`) и кнопок (`buttons`). Если кнопки или ячейки не нужны, в полях `cells` и `buttons` указывайте пустые массивы.
При добавлении ячейки, нужно указать ее заголовок (`title`) и значение (`value`).
Параметр `auto_listening` указывает будет ли смартап слушать ответ пользователя после ответа ассистента.
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
{  
"title":"Заголовок ячейки 2",  
"subtitle":"Описание ячейки 2",  
"value":"Значение, которое отображается в правой части ячейки 2. Рекомендуемая длина менее 5 символов.",  
"iconUrl":"https://example.ru/images/image.png",  
"hash":"3a74d5abfc671f47e45d336ed4d41026",  
"action":{  
"text":"Текст, который отправится при нажатии ячейки"  
}  
}  
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

Пример списка в карточке `list_card`, которую можно передать в поле `items.card` [ответа ассистента](https://developers.sber.ru/docs/ru/va/api/smartapp-api-responses#answer-to-user):
Отображение в чате
Код
![Пример списка](https://cdn-app.sberdevices.ru/asset/q30/aHR0cHM6Ly9jZG4tYXBwLnNiZXJkZXZpY2VzLnJ1L21pc2MvMC4wLjAvYXNzZXRzL2JzbS1kb2NzL2NhcmRsaXN0LXNhbXBsZS5wbmc=)
```
{  
"type":"list_card",  
"paddings":{  
"top":"4x",  
"bottom":"4x"  
},  
"cells":[  
{  
"type":"text_cell_view",  
"paddings":{  
"top":"6x",  
"left":"8x",  
"right":"8x"  
},  
"content":{  
"text":"Название списка",  
"typeface":"title1",  
"text_color":"default"  
}  
},  
{  
"type":"text_cell_view",  
"paddings":{  
"top":"4x",  
"left":"8x",  
"right":"8x",  
"bottom":"6x"  
},  
"content":{  
"text":"Подзаголовок",  
"typeface":"footnote1",  
"text_color":"secondary"  
}  
},  
{  
"type":"left_right_cell_view",  
"paddings":{  
"top":"8x",  
"left":"8x",  
"right":"8x",  
"bottom":"8x"  
},  
"divider":{  
"style":"default",  
"size":"d5"  
},  
"left":{  
"type":"simple_left_view",  
"icon_vertical_gravity":"center",  
"texts":{  
"title":{  
"text":"Первый пункт",  
"typeface":"body1",  
"text_color":"default"  
},  
"subtitle":{  
"text":"Подзаголовок",  
"typeface":"footnote1",  
"text_color":"secondary",  
"margins":{  
"top":"1x"  
}  
}  
}  
},  
"right":{  
"type":"detail_right_view",  
"margins":{  
"left":"2x"  
},  
"detail":{  
"text":"Кнопка пункта",  
"typeface":"body1",  
"text_color":"brand"  
},  
"vertical_gravity":"top"  
},  
"actions":[  
{  
"text":"Первый пункт",  
"type":"text"  
}  
]  
},  
{  
"type":"left_right_cell_view",  
"paddings":{  
"top":"8x",  
"left":"8x",  
"right":"8x",  
"bottom":"8x"  
},  
"divider":{  
"style":"default",  
"size":"d5"  
},  
"left":{  
"type":"simple_left_view",  
"icon_vertical_gravity":"center",  
"texts":{  
"title":{  
"text":"Второй пункт",  
"typeface":"body1",  
"text_color":"default"  
},  
"subtitle":{  
"text":"Подзаголовок",  
"typeface":"footnote1",  
"text_color":"secondary",  
"margins":{  
"top":"1x"  
}  
}  
}  
},  
"right":{  
"type":"detail_right_view",  
"margins":{  
"left":"2x"  
},  
"detail":{  
"text":"Кнопка пункта",  
"typeface":"body1",  
"text_color":"brand"  
},  
"vertical_gravity":"top"  
},  
"actions":[  
{  
"text":"Второй пункт",  
"type":"text"  
}  
]  
},  
{  
"type":"button_cell_view",  
"paddings":{  
"top":"8x",  
"left":"8x",  
"right":"8x",  
"bottom":"8x"  
},  
"content":{  
"actions":[  
{  
"text":"Кнопка списка",  
"type":"text"  
}  
],  
"text":"Кнопка списка",  
"typeface":"button1",  
"margins":{  
"top":"5x",  
"left":"10x",  
"right":"10x",  
"bottom":"5x"  
},  
"style":"default",  
"type":"accept"  
}  
}  
]  
}  

```

## raw
Используется для передачи собранных вручную ответов. Обязательный параметр `body` тело ответа, содержание которого будет добавлено в поле `payload` [протоколе ассистента](https://developers.sber.ru/docs/ru/va/api/smartapp-api-responses#answer-to-user). Параметры, идентифицирующие пользователя будут подставлены автоматически.
При необходимости можно указать поле `messageName` и передать в нем необходимое сообщение. По умолчанию передается значение `ANSWER_TO_USER`. Описание тела сообщения `ANSWER_TO_USER` вы найдете в разделе [SmartApp API](https://developers.sber.ru/docs/ru/va/api/smartapp-api-responses#answer-to-user).
```
{  
"type":"raw",  
"body":{ ... },  
"messageName":"ANSWER_TO_USER"  
}  

```

Тестовый виджет не отображает ответы с типом `raw`, если они передаются с помощью `$context.response.replies`.
## Примеры значений
  * Вывод изображения.

```
script: $response.replies= $response.replies||[];  
$response.replies.push({  
type:'image',  
imageUrl:' https://testimageurl.jpg',  
hash:'<hash картинки из раздела Контент>',  
});  

```

  * Отправка текстового ответа с markdown-разметкой.

```
script: $response.replies= $response.replies||[];  
$response.replies.push({  
type:'raw',  
body:{  
items:[  
{  
bubble:{  
text:'*Привет всем!*',  
markdown:true,  
},  
},  
],  
},  
});  

```

  * Пример изменения ответа в post-процессе при третьей попытке ассистента ответить одинаково.

```
init:bind('postProcess',function(){  
var $session = $jsapi.context().session;  
var $response = $jsapi.context().response;  
var answer = $response.replies  
? $response.replies.reduce(function(answers, current){  
              answers +=' '+ current.text;  
return answers;  
},'')  
:'';  
if($session.lastAnswer&& answer == $session.lastAnswer){  
        $session.answerRepetition= $session.answerRepetition||0;  
        $session.answerRepetition+=1;  
}else{  
        $session.answerRepetition=0;  
}  
if($session.answerRepetition==2){  
        $response.replies=[  
{  
type:'text',  
text:'Похоже мы ходим кругами. Может спросишь о чем-нибудь другом?',  
},  
];  
}  
    $session.lastAnswer= answer;  
});  

```

  * Передача карточки типа `grid_card` в диалог с пользователем:

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