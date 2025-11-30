# Конвертеры в Code
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
[](https://public.oprosso.sberbank.ru/p/docs_csi_2025)
Конвертеры — скрипты, которые используются для интерпретации значений текста в каждом токене.
Конвертеры позволяют преобразовать данные токена, помещаемые в [`$parseTree`](../js-api/variables/parse-tree.md).
## Объявление
Объявление конвертера:
  * при объявлении паттерна;

```
patterns:  
        $four = четыре || converter = function() {return 4}  

```

  * в тегах [`init`](../sa-dsl/tags/declarative-tags.md#init2);

```
init:functionamountConverter(pt){  
var ret = pt.Number[0].value;  
return ret;  
}  

```

  * в файле `.js`-библиотек, например `converters.js`.

```
functionamountConverter(pt){  
var ret = pt.Number[0].value;  
return ret;  
}  

```

В функции конвертеров в качестве первого аргумента передается `$parseTree`.
Вы можете использовать внутри конвертера переменную, в которую передается `$parseTree`. Для этого задайте ее имя первым аргументом функции, вторым аргументом передается контекст.
### Применение
Применение конвертеров:
  * Формирование значения из текста.

Сценарий:
```
$Digit = $regexp<\d+> || converter = numberConverterDigit  

```

`.js`-файл:
```
functionnumberConverterDigit(parseTree){  
returnparseInt(parseTree.text);  
}  

```

  * Преобразование значения из маппинга.

Сценарий:
```
$Numeral = (один:1|...) || converter = valueToNumberConverter  

```

`.js`-файл:
```
functionvalueToNumberConverter(parseTree){  
returnparseInt(parseTree.value);  
}  

```

  * Формирование значения из вложенных токенов.

Сценарий:
```
$Numeral = (один:1|...)  
$Minutes = $Numeral || converter = minutesConverter  

```

`.js`-файл:
```
functionminutesConverter(parseTree){  
returnparseInt(parseTree.Numeral.value);  
}  

```

  * Формирование значения из справочников.

Сценарий:
```
$City = $entity<Cities> || converter = сityConverter  

```

`.js`-файл:
```
functionсityConverter(parseTree){  
var id = parseTree.City[0].value;  
returnCities[id].value;  
}  

```

Правило `$entity` записывает в `value` только идентификатор сущности. Список ассоциированных значений содержится в справочнике.