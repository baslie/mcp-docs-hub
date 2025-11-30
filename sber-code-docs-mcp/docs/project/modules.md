# Работа с модулями в Code
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
В конфигурационном файле `chatbot.yaml` в секции `dependencies` определяется список зависимостей проекта.
`module` — одна из возможных зависимостей. Это готовые модули, на которые вы можете ссылаться и переиспользовать контент из них: файлы сценариев, JS-библиотек, справочников.
[Подробнее о конфигурационном файле и зависимостях](./configuration-file.md)
#### Cинтаксис
Указываются модули в зависимостях `dependencies` конфигурационного файла `chatbot.yaml`.
Параметры `module`:
#### Работа с module
Рассмотрим пример подключения модуля. Зададим в конфигурационном файле имя и папку модуля в `dependencies`:
```
name: games-test  
  
entryPoint: main.sc  
  
dependencies:  
-name: common  
type: module  

```

Далее вызовем в сценарии файлы из модуля при помощи `require`:
```
require: text/text.sc  
    module = common  
  
require: number/number.sc  
    module = common  
  
require: common.js  
    module = common  
  
require: city/city.sc  
    module = common  
  
require: city/cities-ru.csv  
    name = Cities  
    var = $Cities  
    module = common  

```

[Подробнее об использовании тега `require`](../sa-dsl/tags/declarative-tags.md#require2)
Теперь контент из вызванных файлов модуля можно использовать в сценарии проекта. Например, сценарий `main.sc`:
```
require: number/number.sc  
    module = common  
  
require: common.js  
    module = common  
  
require: city/city.sc  
    module = common  
  
require: city/cities-ru.csv  
    name = Cities  
    var = $Cities  
    module = common  
  
theme: /  
  
    state: Text  
        q: $Text  
        a: Вы сказали: {{ $parseTree._Text }}  
  
    state: NumberPattern  
        q: * $Number *  
        a: Число: {{$parseTree._Number}}  
  
    state: CityPattern  
        q: * $City *  
        a: Город: {{$parseTree._City.name}}  
  
    state: NoMatch  
        q: *  
        a: Извините, я вас не понимаю.  

```

Зависимости скачиваются в папку `modules` при деплое через веб-интерфейс.