---
title: Файлы JavaScript библиотек
source_url: https://developers.sber.ru/docs/ru/salutebot/bot-development/project-structure/js
tags: [Code]
---

# Файлы JavaScript библиотек

* * *
`.js` — файлы js-библиотек.
Содержат JavaScript-код, который можно использовать в файлах сценариев. Содержат функции, логику обработки запросов, вызовы внешних систем, работу с памятью и пр.
`.js`-файлы подгружаются в начале сценария при помощи тега `require`:
```
require: scripts/functions.js  

```

[Подробнее о работе с тегом `require`](https://developers.sber.ru/docs/ru/va/code/sa-dsl/tags/declarative-tags#require)