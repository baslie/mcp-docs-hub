# function inference(text, settings)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
Выполняет классифкацию текста c дополнительными параметрами.
  

#### Синтаксис
Метод принимает в качестве аргумента текст для разметки в виде строки `string` и дополнительные параметры:
```
$caila.inference({"phrase":{"text":"greetings"}, "nBest": 5, knownSlots: [{"name":"a", "value":"b"}]})  

```

Здесь:
  * `phrase` — фразы для классификации.
  * `nBest` — количество возвращаемых гипотез.
  * `knownSlots` — известные слоты: 
    * `name` — название слота;
    * `value` — значение слота.

В качестве ответа передается JSON с результатом классифкации фразы.
Определим интент `hello` с тренировычными фразами: hello, hi. Результат классификации фразы `hello`:
```
{  
"phrase":{  
"text":"hello",  
"entities":[]  
},  
"variants":[  
{  
"intent":{  
"id":12174,// id интента  
"path":"/hello",// путь к интенту  
"slots":[  
// слоты  
]  
},  
"confidence":1,// степень уверенности  
"slots":[]  
}  
]  
}  

```

  

#### Использование в сценарии
```
    state:  
        q!: inference  
        script:  
            $reactions.answer(JSON.stringify($caila.inference({"phrase":{"text":"hello"}, "nBest": 5, knownSlots: [{"name":"a", "value":"b"}]})));  

```