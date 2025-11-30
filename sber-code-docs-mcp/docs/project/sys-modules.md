# Модули sys.modules в Code
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
`sys.modules` — модули, на которые можно ссылаться в сценарии и переиспользовать контент из них: файлы сценариев, JS-библиотек, справочников.
## Cинтаксис и использование
Файлы модуля подгружаются из внутренних ресурсов приложения или из папки `botserver-modules`.
Укажите путь к `botserver-modules` в файле `application.yml`:
```
systemModulesFolder: /folder/other-folder/botserver-modules  

```

Пример структуры папки `botserver-modules`:
```
/opt/sberdevices/botserver-modules  
  
  
├── common  
│   ├── chatbot.yaml  
│   ├── declarations.js  
│   ├── src  
│   └── test  
└── dictionaries  
    └── main_dictionary  

```

Для вызова модуля в сценарии укажите:
```
require: <вызываемый файл>  
  module = sys.<имя папки c вызываемым файлом>  

```

Здесь префикс `sys` соответствует указанному в `application.yml` пути. Таким образом, требуется указывать только конечную папку с файлом.
Вызовите модуль в сценарии, например:
```
require: common.js  
  module = sys.common  

```

Здесь:
  * `require: common.js` — вызываем скрипт, который будет использоваться в сценарии.
  * `module = sys.common` — указываем папку, в которой находится файл скрипта.

Теперь контент из вызванного файла модуля можно использовать в сценарии проекта.