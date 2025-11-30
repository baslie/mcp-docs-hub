# Шаблоны приложений в Code
Обновлено 28 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/ChatApp.png)Chat App ](https://developers.sber.ru/docs/ru/va/chat/title-page)
[](https://public.oprosso.sberbank.ru/p/docs_csi_2025)
Шаблон смартапа — это образец сценария, который демонстрирует особенности разработки в редакторе Code. Например, подключение платежей или работа с карточками. Вы можете выбрать шаблон при [создании проекта Code](https://developers.sber.ru/docs/ru/va/chat/script/project-creation#sozdanie-proekta-code).
![Выбор шаблона Code](https://developers.sber.ru/docs/assets/images/code-template-0d276f780a27a9105caeed90631eaeea.png)
### Пример работы с карточками
Шаблон демонстрирует, как выглядят различные типы [карточек](https://developers.sber.ru/docs/ru/va/api/smartapp-interface-elements#card2) в смартапе: `grid_card`, `gallery_card`, `list_card` и др.
Некоторые типы карточек не отображаются в [тестовом виджете](../project/test-widget.md).
Карточки шаблона описаны в файле `/src/scripts/cards.js`. Для передачи карточек используется [тип ответа raw](../response/message-types.md#raw2).
### Пример работы с ассистентом
Шаблон демонстрирует [эмоции ассистента](https://developers.sber.ru/docs/ru/va/api/assistant-emotions) и показывает, как могут отличаться ответы для разных [голосов](https://developers.sber.ru/docs/ru/va/about/salute-apps/assistants). Получить эмоции можно с помощью идентификатора (поле `id`) из файла `/src/emotions.csv`. Ответы ассистента передаются с помощью [ответа типа raw](../response/message-types.md#raw2).
Ассистент демонстрирует эмоции с помощью анимации кнопки, поэтому тестируйте эту функциональность на устройстве или в [эмуляторе](https://developers.sber.ru/docs/ru/va/chat/testing).
### Пример подключения монетизации
Шаблон демонстрирует [подключение платежей](https://developers.sber.ru/docs/ru/va/about/monetization/payments/processing/code) в смартап. Чтобы подключить платежи, в разделе `injector` конфигурационного файла шаблона надо указать [serviceId и ключ API](https://developers.sber.ru/docs/ru/va/about/monetization/payments/access#ekspluatatsionnyy-token2).
```
injector:  
service_id:'27'  
pay_api_key:'ДОБАВЬТЕ ВАШ ТОКЕН SMARTPAY API'  

```

Ключ API можно передать в процессе [создания счета](https://developers.sber.ru/docs/ru/va/about/monetization/payments/processing/graph#sozdanie-scheta5). При этом ключ, заданный в `injector.pay_api_key`, будет проигнорирован.
### Монетизация для Native App
Шаблон для подключения монетизации к простым apk. Реализована встроенная разовая покупка. Подходит в том числе для игровых приложений. Подробнее о работе шаблона читайте в разделе [Подключение платежей](https://developers.sber.ru/docs/ru/va/native/monetization/payments).
### Пример работы со звуками
Шаблон демонстрирует работу с [загруженными звуками](../sa-dsl/tags/reaction-tags.md#teg-audio2), а также разницу в озвучивании текста с заданной [SSML-разметкой](https://developers.sber.ru/docs/ru/va/chat/voice-interface/speech-synthesis/ssml/overview) и без нее. Для демонстрации используются звуки из встроенной [библиотеки](https://developers.sber.ru/docs/ru/va/chat/voice-interface/speech-synthesis/sound-library). Звуки смартапа описаны в файле `/src/dicts/libSound.yaml`.
В тестовом виджете звуки не воспроизводятся.
### Проект для SmartApp Brain
Шаблон дает возможность работать с интентами и сущностями с помощью [SmartApp Brain](../nlp/overview.md).