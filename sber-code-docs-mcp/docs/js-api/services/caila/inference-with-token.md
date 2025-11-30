# function inferenceWithToken(text, settings, token)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
Выполняет классифкацию текста c дополнительными параметрами. Метод используется для обращения к стороннему обученному классификатору при помощи API-ключа.
  

#### Синтаксис
Метод принимает в качестве аргумента текст для разметки и API-ключ к стороннему обученному классификатору в виде строк `string`, а также дополнительные параметры:
```
$caila.inferenceWithToken({"phrase":{"text":"greetings"}, "nBest": 5, knownSlots: [{"name":"a", "value":"b"}]}, "token"))  

```

Здесь:
  * `phrase` — фразы для классификации.
  * `nBest` — количество возвращаемых гипотез.
  * `knownSlots` — известные слоты: 
    * `name` — название слота;
    * `value` — значение слота.

[Подробнее о получении API-ключа](../../../nlp/api/overview.md#section/Autentifikaciya)
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
        q!: inferenceWithToken  
        script:  
            $reactions.answer(JSON.stringify($caila.inferenceWithToken({"phrase":{"text":"greetings"}, "nBest": 5, knownSlots: [{"name":"a", "value":"b"}]}, "token")));  

```