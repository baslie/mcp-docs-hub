---
title: Файлы с тестами
source_url: https://developers.sber.ru/docs/ru/salutebot/bot-development/project-structure/xml
tags: [Code]
---

# Файлы с тестами

* * *
`.xml` — файлы автоматических тестов, пишутся на языке XML.
Тесты имеют следующую структуру:
```
<test>  
<test-case>  
<q>Запрос пользователя</q>  
<a>Ответ ассистента</a>  
</test-case>  
  
<test-case>  
<q>Запрос пользователя</q>  
<a>Ответ ассистента</a>  
</test-case>  
</test>  

```

Тесты выполняются автоматически при деплое чат-бота, если присутствуют в папке проекта `test`. Это поведение можно переопределить в файле `chatbot.yaml` в секции `tests`.
Секция `tests` может содержать две подсекции `include` и `exclude`, каждая представляет собой список [ant-шаблонов ](https://ant.apache.org/manual/dirtasks.html#patterns) с именами файлов.
  * `include` — будут выполнены тесты только из тех файлов, которые попадают под шаблоны, перечисленные в этой подсекции.
  * `exclude` — из выполнения будут исключены все файлы, которые попадают под шаблоны, перечисленные в этой подсекции.

Например:
```
tests:  
include:  
- tests.xml  
- delivery.xml  
- order.xml  
- cart.xml  
- otherCities.xml  
- sauces.xml  
exclude:  
- time.xml  

```

Обратите внимание на [необходимость экранирования в xml ](https://stackoverflow.com/questions/1091945/what-characters-do-i-need-to-escape-in-xml-documents) таких символов, как `&`.