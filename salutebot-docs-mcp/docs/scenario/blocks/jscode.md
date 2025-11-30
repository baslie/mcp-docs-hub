---
title: Используем код на JavaScript
source_url: https://developers.sber.ru/docs/ru/salutebot/scenario/blocks/jscode
tags: [Graph, Code]
---

# Используем код на JavaScript

Блок **JS код** предназначен для выполнения в сценарии произвольного кода на JavaScript.
Код требуется указывать в поле **JS Код**.
В отличие от других блоков при обращении к переменным в JavaScript-коде блока **JS Код** необходимо указывать полный путь переменной:
```
$session.<название переменной>  

```

Логику, заданную с помощью блока **Код** , также можно реализовать с помощью тега [`script`](https://developers.sber.ru/docs/ru/va/code/sa-dsl/tags/reaction-tags#teg-script) Code.