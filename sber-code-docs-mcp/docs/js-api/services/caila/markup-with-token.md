# function markupWithToken(text, token)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
Выполняет разметку переданного текста. Метод используется для обращения к стороннему обученному классификатору при помощи API-ключа.
  

#### Синтаксис
Метод принимает в качестве аргумента текст для разметки и API-ключ к стороннему обученному классификатору в виде строк `string`:
```
$caila.markup("markup text", "token")  

```

[Подробнее о получении API-ключа](../../../nlp/api/overview.md#section/Autentifikaciya)
В качестве ответа передается размеченная фраза в формате JSON. Результат разметки фразы `markup text`:
```
{  
"source":"markup text",//фраза для разметки  
"words":[  
{  
"annotations":{  
"lemma":"markup",  
"pos":"X"//часть речи  
},  
"startPos":0,//позиция слова во фразе  
"endPos":6,  
"pattern":false,  
"punctuation":false,  
"source":"markup",  
"word":"markup"//нормализованная форма слова  
},  
{  
"annotations":{  
"lemma":"text",  
"pos":"X"//часть речи  
},  
"startPos":7,//позиция слова во фразе  
"endPos":11,  
"pattern":false,  
"punctuation":false,  
"source":"text",  
"word":"text"//нормализованная форма слова  
}  
]  
}  

```

  

#### Использование в сценарии
```
    state:  
        q!: markup text with token  
        script:  
            $reactions.answer(JSON.stringify($caila.markupWithToken("greetings", "API token")));  

```