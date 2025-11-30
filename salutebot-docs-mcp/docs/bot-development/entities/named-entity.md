---
title: Именованные сущности
source_url: https://developers.sber.ru/docs/ru/salutebot/bot-development/entities/named-entity
tags: [Code]
---

# Именованные сущности

Именованная сущность — это слово или словосочетание, которое выделяет предмет или являение в ряде аналогичных предметов или явлений. Примерами именованных сущностей являются названия городов, стран, валют.
В сценарии чат-бота именованная сущность представляет собой [именованный паттерн](https://developers.sber.ru/docs/ru/va/code/nlp/patterns/named-patterns), заданный при помощи [справочника именованных сущностей](https://developers.sber.ru/docs/ru/va/code/project/csv).
## Элементы справочника именованных сущностей
Чтобы использовать элементы справочника именованных сущностей в именованном паттерне:
  1. Указать название справочника и путь к нему в файле сценария `.sc`. Для этого используйте тег [`require`](https://developers.sber.ru/docs/ru/va/code/sa-dsl/tags/declarative-tags#require):

```
require: common/common-cities.csv  
         name =RoamingRegions  
var=RoamingRegions  

```

  1. Задайте в файле `.js`-библиотек конвертер. Конвертер позволяет записывать информацию в поле `value` дерева разбора `parseTree` для паттерна. Например:

```
functionRoamingRegionTagConverter($parseTree){  
var id = $parseTree.RoamingRegions[0].value;  
returnRoamingRegions[id].value;  
}  

```

Здесь:
  * `RoamingRegionTagConverter` — название конвертера;
  * `RoamingRegions` — название справочника именованных сущностей.

Возвращаемое значение записывается в поле `value`.
  1. Объявить именованный паттерн. Используйте `$entity<>`:

```
$roamingRegion = $entity<RoamingRegions>|| converter =RoamingRegionTagConverter  

```

Именованные сущности можно использовать и без объявления именованного паттерна.
При подобном объявлении именованной сущности в `$parseTree` появляется элемент `value`, куда записывается id.