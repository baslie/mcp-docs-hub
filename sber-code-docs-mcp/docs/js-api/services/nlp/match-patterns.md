# function matchPatterns(text, patterns)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
Выполняет сопоставление паттернов для заданного текста. Возвращает объект `NLPResult`: содержит указание какой паттерн сработал и объект `ParseTree`.
  

##### Примеры значений
Пример вызова:
```
state: Common  
  q!: ...  
  script:  
    var res = $nlp.matchPatterns("test 1", ["test 1", "test 2"]);  
    log(res);  

```

Пример результата:
```
{  
"patternId":"test 1",  
"pattern":"test 1",  
"effectivePattern":"test 1",  
"score":0.5,  
"parseTree":{  
"tag":"root",  
"pattern":"root",  
"text":"test 1",  
"words":[  
"test",  
"1"  
],  
"_Root":"test 1"  
},  
"weight":1  
}  

```