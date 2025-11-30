# $parseTree
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Представляет результат разбора входной фразы, в соответствии с именованными паттернами, и результаты работы конверторов значений.
`$parseTree` имеет древовидную структуру, где на каждом уровне представлены данные, относящиеся к определенному токену, начиная с корневого.
Формат одного уровня `$parseTree`:
```
$parseTree:{  
tag:  
pattern:  
text:  
words:  
value:  
TokenByName:<$parseTree>// вложенные токены  
...  
}  

```

Где:
  * `tag` — имя, под которым токен фигурирует в `$parseTree`;
  * `pattern` — имя именованного паттерна, в который попал текст;
  * `text` — текст в виде `string`;
  * `words` — токены;
  * `value` — элемент является активным при использовании маппинга, конвертеров или именованных сущностей.
  * `TokenByName` — именованный паттерн.

  

##### Примеры значений
  * Определим дерево разбора для фразы `Какая погода в Петербурге?`.

Именнованные паттерны для разбора фразы:
```
$Question = (какой|какая)  
$Weather = (погода|прогноз)  
$City = (~Петербург|~Москва)  
q: * [$Question] * $Weather * $City *  

```

Для фразы будет построено следующее дерево разбора:
```
$parseTree:{  
"tag":"root",  
"pattern":"root",  
"text":"Какая погода в Петербурге",  
"words":[  
"какая",  
"погода",  
"в",  
"Петербурге"  
],  
"Question":[  
{  
"tag":"Question",  
"pattern":"Question",  
"text":"Какая",  
"words":[  
"какая"  
]  
}  
],  
"Weather":[  
{  
"tag":"Weather",  
"pattern":"Weather",  
"text":"погода",  
"words":[  
"погода"  
]  
}  
],  
"City":[  
{  
"tag":"City",  
"pattern":"City",  
"text":"Питере",  
"words":[  
"Петербурге"  
]  
}  
]  
"_Question":"Какая",  
"_Weather":"погода",  
"_City":"Петербурге"  
}  

```

  * Определим дерево разбора для фразы `два плюс два`. Фраза будет разбита на фрагменты, в соответствии с использованными именованными паттернами. Структура рекурсивная и фрагменты могут быть вложенными на любую глубину, как в следующем примере:

```
$Digit = $regexp<\d+>  
$Numeral = (один:1|два:2)  
$Number = ($Digit|$Numeral)  
$Operation = (плюс:+|минус:-)  
q: * $Number::Number1 $Operation $Number::Number2 *  

```

Для фразы будет построено следующее дерево разбора:
```
$parseTree:{  
"tag":"root",  
"pattern":"root",  
"text":"два плюс два",  
"words":[  
"два",  
"плюс",  
"два"  
],  
"Number1":[  
{  
"tag":"Number1",  
"pattern":"Number",  
"text":"два",  
"words":[  
"два"  
],  
"Numeral":[  
{  
"tag":"Numeral",  
"pattern":"Numeral",  
"text":"два",  
"words":[  
"два"  
],  
"value":"2"  
}  
]  
}  
],  
"Operation":[  
{  
"tag":"Operation",  
"pattern":"Operation",  
"text":"плюс",  
"words":[  
"плюс"  
],  
"value":"+"  
}  
],  
"Number2":[  
{  
"tag":"Number2",  
"pattern":"Number",  
"text":"два",  
"words":[  
"два"  
],  
"Numeral":[  
{  
"tag":"Numeral",  
"pattern":"Numeral",  
"text":"два",  
"words":[  
"два"  
],  
"value":"2"  
}  
]  
}  
],  
"_Number1":"2",  
"_Operation":"+",  
"_Number2":"2"  
}  

```

[Подробнее о работе с паттернами](../../nlp/patterns/about-patterns.md)