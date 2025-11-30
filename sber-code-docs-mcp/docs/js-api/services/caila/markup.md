# function markup(text)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
Выполняет разметку переданного текста.
  

#### Синтаксис
Метод принимает в качестве аргумента текст для разметки в виде строки `string`:
```
$caila.markup("markup text")  

```

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
        q!: markup text  
        script:  
            $reactions.answer(JSON.stringify($caila.markup("markup text")));  

```