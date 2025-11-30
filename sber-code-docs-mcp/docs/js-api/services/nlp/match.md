# function match(text, state)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
[](https://public.oprosso.sberbank.ru/p/docs_csi_2025)
Выполняет сопоставление паттернов для заданного текста. Возвращает объект `NLPResult`: содержит указание какой паттерн в каком состоянии сработал и объект `parseTree`.
  

##### Примеры значений
Пример вызова:
```
state: A  
  q!: ...  
  script:  
    var res = $nlp.match("test 1", "/");  
    log(res);  
    $reactions.transition(res.targetState);  

```

Пример результата:
```
{  
"targetState":"/1",  
"patternId":"main.sc:12",  
"pattern":"* test 1 *",  
"effectivePattern":"* test 1 *",  
"score":1,  
"parseTree":{  
"tag":"root",  
"pattern":"root",  
"text":"test 1",  
"words":[  
"test",  
"1"  
]  
}  
}  

```

Параметр `onlyThisState` в `$nlp.match()` не поддерживается. Если есть необходимость использовать флаг `onlyThisState = true`, используйте модификатор `modal = true` в стейте.