# function entitiesLookupWithToken(text, token)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
Выполняет поиск сущностей в переданном тексте. Метод используется для обращения к стороннему обученному классификатору при помощи API-ключа.
  

#### Синтаксис
Метод принимает в качестве аргумента текст для разметки и API-ключ к стороннему обученному классификатору в виде строк `string`, флаг `show all`. При значении флага:
  * `true` — в ответе будут переданы все найденные гипотезы.
  * `false` — в ответе будут переданы наиболее вероятные гипотезы для кажажой из сущностей, найденных в тексте.

```
$caila.entitiesLookup("text@entities.ru",true,"token")  

```

[Подробнее о получении API-ключа](../../../nlp/api/overview.md#section/Autentifikaciya)
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
   q!: entitiesLookupWithToken  
   script:  
      $reactions.answer(JSON.stringify($caila.entitiesLookupWithToken("test@test.ru", true, "token")));  

```