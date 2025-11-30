---
title: Подключаем библиотеки и скрипты
source_url: https://developers.sber.ru/docs/ru/salutebot/scenario/scenario-management/preload-js-scripts
tags: [Code]
---

# Подключаем библиотеки и скрипты

Вы можете подключать собственные скрипты и JavaScript-библиотеки, со вспомогательными функциями, в файле конфигурации [`chatbot.yaml`](https://developers.sber.ru/docs/ru/salutebot/bot-steps/project-structure/configuration_file). Подключение скриптов с помощью конфигурационного файла сокращает время сборки чат-бота.
Подключение библиотек и сервисов позволяет использовать их функции в сценариях чат-бота. Так, для работы с [коллекциями ](https://underscorejs.ru/#collections) и [массивами ](https://underscorejs.ru/#arrays) вы можете использовать функции библиотеки Underscore.js, доступной по умолчанию. Для вызова функции библиотеки используйте нижнее подчеркивание `_`.
Вы также можете подключать скрипты и библиотеки внутри отдельных сценариев с помощью тега [`require`](https://developers.sber.ru/docs/ru/salutebot/bot-steps/project-structure/js). При этом подключать скрипт в файле конфигурации не надо.
## Синтаксис
Для подключения скрипта или библиотеки надо указать абсолютный путь до соответствующего файла в разделе `global` или `local`, в секции `scriptsPreLoad`:
  * Скрипты раздела `global` загружаются при первой сборке чат-бота и сохраняются на все последующие сборки.
  * Скрипты раздела `local` загружаются при каждой сборке чат-бота и сохраняются до его публикации. При этом файлы скриптов не надо паковать вместе с чат-ботом.

Оба раздела обязательны и не могут быть пустыми.
По умолчанию в `chatbot.yaml` любого проекта Code подключены библиотеки [Underscore.js ](http://underscorejs.ru/) и [moment.js ](https://momentjs.com/), а также некоторые [сервисы JavaScript API](https://developers.sber.ru/docs/ru/va/code/js-api/overview):
```
scriptsPreLoad:  
global:  
- /jslib/moment.min.js  
- /jslib/underscore.js  
- /jsapi/common.js  
- /jsapi/http.js  
local:  
- /jsapi/mail.js  
- /jsapi/reactions.js  

```