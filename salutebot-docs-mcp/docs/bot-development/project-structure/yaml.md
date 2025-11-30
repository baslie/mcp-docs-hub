---
title: Справочники YAML
source_url: https://developers.sber.ru/docs/ru/salutebot/bot-development/project-structure/yaml
tags: [Code]
---

# Справочники YAML

* * *
YAML-cправочники используются для хранения различной информации одного проекта. Например в справочнике можно хранить тексты ответов бота, API-ключи, настройки громкости и другие параметры.
## Формат данных в справочнике
Данные хранятся в справочнике в формате:
```
ключ: значение  

```

Записи могут быть вложенными:
```
volumeControl:  
levels:100  
step:20  

```

В качестве значений можно указывать переменные, которые хранятся в объектах:
```
ifUserHasRightAnswers:  
a1:'Мы ответили правильно на {{$temp.right}} {{$temp.ru__answers}} на текущем уровне сложности!'  

```

## Работа со справочниками
Рассмотрим работу с YAML-справочниками на примере справочника `answers.yaml`, который содержит ответы чатбота:
```
botAnswers:  
a1:'Ваше число: {{ $parseTree._Number }}'  
a2:'Так держать! Вы назвали число {{ $parseTree._Number }}'  

```

Для подключения справочника используйте тег [`require`](https://developers.sber.ru/docs/ru/va/code/sa-dsl/tags/declarative-tags#require):
```
require: answers.yaml  
    var = answers  
  
patterns:  
    $Number = (1/2/3/4/5)  
  
theme: /  
  
    state: Number  
        q!: $Number  
        script:  
            $session.number = $parseTree._Number;  
        random:  
        a: Ваше число: {{ $parseTree._Number }}  
        a: {{$global.answers.botAnswers.a2}}  

```

К ответам из справочника можно обращаться как к обычным переменным (тег `a` в примере сценария).
О том как выбрать случайный вариант ответа из справочника, читайте в разделе [Встроенные сервисы](https://developers.sber.ru/docs/ru/va/code/js-api/services/reactions/answer#sluchaynyy-otvet-s-pomoshyu-yaml-spravochnika).