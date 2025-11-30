# function entitiesLookup(text)
Обновлено 18 июля 2024
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
Выполняет поиск сущностей в переданном тексте.
  

#### Синтаксис
Метод принимает в качестве аргумента текст для разметки в виде строки `string`, а также флаг `show all`. При значении флага:
  * `true` — в ответе будут переданы все найденные гипотезы.
  * `false` — в ответе будут переданы наиболее вероятные гипотезы для каждой из сущностей, найденных в тексте.

```
$caila.entitiesLookup("text@entities.ru",true)  

```

В качестве ответа передается JSON с найденными сущностями во фразе. Результат поиска сущностей во фразе `text@entities.ru` с выводом всех гипотез:
```
{  
"text":"text@entities.ru",  
"entities":{  
"default":true,  
"entity":"duckling.email",//найденная сущность  
"startPos":0,//позиция слова во фразе  
"endPos":16,  
"text":"text@entities.ru",  
"value":"text@entities.ru",  
"system":true  
}  
}  

```

  

#### Использование в сценарии
```
    state:  
        q!: entitiesLookup  
        script:  
            $reactions.answer(JSON.stringify($caila.entitiesLookup("test@test.ru", true)));  

```