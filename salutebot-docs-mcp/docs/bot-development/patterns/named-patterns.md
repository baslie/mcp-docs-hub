---
title: Именованные паттерны
source_url: https://developers.sber.ru/docs/ru/salutebot/bot-development/patterns/named-patterns
tags: [Code]
---

# Именованные паттерны

Именованный паттерн — часть паттерна, выделенная в отдельную сущность, которая может быть использована несколько раз.
Именованные паттерны выделяются по семантическому признаку. Например:
  * синонимы;
  * различные варианты написания выражений, объединенных одним смыслом и встречающихся в определенной позиции в однотипных предложениях.

Список именованных паттернов объявляется в теге `patterns` в [файле сценария](https://developers.sber.ru/docs/ru/salutebot/bot-steps/project-structure/sc):
```
patterns:  
        $<pattern name> = (pattern body | multiline body)  
        $<pattern name> = (pattern body) || converter=nameConverter  

```

Каждый вложенный элемент тега `patterns` задает новый именованный паттерн.
Для объявления и обращения к именованному паттерну используется символ `$`.
После знака `=` задается значение типа `multiline string`. С помощью необязательного атрибута `converter` (тип `string`) в значении можно указать [конвертер](https://developers.sber.ru/docs/ru/va/code/nlp/converters), который будет использоваться для интерпретации значений текста.
Как и паттерны, именованные паттерны могут быть заданы с помощью базовых и расширенных элементов:
```
patterns:  
        $mobilePhoneNumber = $regexp<(8|\+?7)-?\(?9\d{2}\)?-?\d{3}-?\d{2}-?\d{2}>  
        $mistake = (ошиб*|неверн*|некорректн*|неправиль*)  
        $roamingRegion = $entity<RoamingRegions>  

```