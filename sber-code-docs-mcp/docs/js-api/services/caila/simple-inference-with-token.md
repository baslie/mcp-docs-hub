# function simpleInferenceWithToken(text, token)
Обновлено 18 июля 2024
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
Выполняет классификацию текста без дополнительных параметров. Метод используется для обращения к стороннему обученному классификатору при помощи API-ключа.
  

#### Синтаксис
Метод принимает в качестве аргумента текст для разметки и API-ключ к стороннему обученному классификатору в виде строк `string`:
```
$caila.simpleInferenceWithToken("text", "token")  

```

[Подробнее о получении API-ключа](../../../nlp/api/overview.md#section/Autentifikaciya)
В качестве ответа передается JSON с результатом классифкации фразы.
Определим интент `hello` с тренировочными фразами: hello, hi. Результат классификации фразы `hello`:
```
{  
"intent":{  
"id":12174,// id интента  
"path":"/hello",// путь к интенту  
"slots":[]  
},  
"confidence":1,// степень уверенности  
"slots":[  
// слоты  
]  
}  

```

  

#### Использование в сценарии
```
    state:  
        q!: simpleInferenceWithToken  
        script:  
            $reactions.answer(JSON.stringify($caila.simpleInferenceWithToken("hello", "token")));  

```