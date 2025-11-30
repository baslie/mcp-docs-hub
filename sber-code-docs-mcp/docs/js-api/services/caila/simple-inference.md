# function simpleInference(text)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
Выполняет классифкацию текста без дополнительных параметров.
  

#### Синтаксис
Метод принимает в качестве аргумента текст для разметки в виде строки `string`:
```
$caila.simpleInference("hello")  

```

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
        q!: simpleInference  
        script:  
            $reactions.answer(JSON.stringify($caila.simpleInference("hello")));  

```