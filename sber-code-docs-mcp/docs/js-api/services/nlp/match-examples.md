# function matchExamples(text, examples)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
Выполняет сопоставление текста с заданным набором примеров. Возвращает:
  * ближайший пример;
  * количество слов во фразе пользователя, для которых найдено соответствие в примерах;
  * вес соответствия.

  

##### Примеры значений
Пример вызова:
```
state: Common  
  q!: ...  
  script:  
    var res = $nlp.matchExamples("раз раз", ["раз", "два", "три"]);  
    log(res);  

```

Пример результата:
```
{  
example:"раз",  
weight:0.5,  
aligned:1  
}  

```