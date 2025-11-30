---
title: Widget API
source_url: https://www.jivo.ru/docs/widget/
---

# Widget API

## Callback-функции

Jivo вызывает перечисленные ниже функции на странице, чтобы сообщить о возникновении события. Вы можете объявить на странице любую из этих функций и выполнять в ней логику обработки возникшего события. Например, по событию jivo_onIntroduction вы можете получить введенные клиентом контактные данные.

### onLoadCallback

Вызывается при завершении инициализации виджета Jivo.

```js
function jivo_onLoadCallback() {
    console.log('Widget fully loaded');
    jivo_api.showProactiveInvitation("How can I help you?");
}
```

### onOpen

Вызывается при открытии окна диалога Jivo: как при автоматическом открытии, так и если виджет был открыт вручную.

```js
function jivo_onOpen() {
    console.log('Widget opened');
}
```

### onClose

Вызывается при сворачивании окна диалога Jivo.

```js
function jivo_onClose() {
    console.log('Widget closed');
}
```

### onChangeState

Вызывается при переключении виджета из одного состояния в другое.

| Название | Тип | Описание |
| --- | --- | --- |
| state | string | Состояние виджета |

```js
function jivo_onChangeState(state) {
    if (state == 'chat') {
        // widget is in the chat state
    }
    if (state == 'call' || state == 'chat/call') {
        // callback form is opened
    }
    if (state == 'label' || state == 'chat/min') {
        // widget is minimized
    }
}
```

### onMessageSent

Посетитель отправил первое сообщение в виджет, срабатывает только один раз, когда история сообщений пуста.

```js
function jivo_onMessageSent() {
    console.log('Client sent the first message');
}
```

### onClientStartChat

Пользователь инициировал диалог, отправив сообщение в чат. Сработает в случае, если ранее в чате не появлялось активное приглашение от лица оператора.

```js
function jivo_onClientStartChat() {
    console.log('Client started a new chat');
}
```

### onIntroduction

Посетитель отправил контактные данные в чате. Эту функцию можно использовать для отслеживания отправки контактов со стороны клиента для последующей передачи этих данных в другие формы на сайте.

```js
function jivo_onIntroduction() {
    console.log('Client entered contact details');
    let userContacts = jivo_api.getContactInfo();
    console.log(userContacts)
}
```

### jivo_onAccept

Оператор принял входящий чат или инициировал диалог с посетителем из раздела "Посетители"/"Все диалоги".

```js
function jivo_onAccept() {
	console.log('Agent joined the chat')
}
```

### jivo_onMessageReceived

От оператора поступило новое сообщение в чат. Можно использовать как при работе со стандартным ярлыком чата, так и для кастомизации своей иконки виджета. Пример: можно отображать счётчик непрочитанных сообщений от оператора пользователю, используя эту функцию.

```js
let i = 1;
function jivo_onMessageReceived() {
	console.log(`Check agents messages:  ${i++}`)
}
```

### jivo_onCallStart

Вызывается при начале звонка на клиентский номер. Звонок может заказать клиент через форму обратного звонка, также звонок можно инициировать программно при помощи метода jivo_api.startCall().

```js
function jivo_onCallStart() {
  console.log('Call is started')
}
```

### jivo_onCallEnd

Пример вызова функции с возвращаемым параметром. Вызывается при окончании звонка с результатом звонка:

| Название | Тип | Описание |
| --- | --- | --- |
| result `необязательный` | object | Результат вызова |

```js
function jivo_onCallEnd(res) {
    if (res.result == 'ok') {
        // call finished successfully
    }
    if (res.result == 'fail') {
        // call finished with errors or can not started
        console.log(res.reason); // reason for the unsuccessfull call
    }
}
```

### jivo_onResizeCallback

Функция срабатывает при изменении размеров виджета: его открытии, закрытии или перемещении по странице пользователем. Может использоваться для динамического добавления или скрытия других элементов на сайте.

```js
function jivo_onResizeCallback() {
   console.log("Widget is resized")
}
```

### jivo_onWidgetDestroy

Вызывается при полном удалении виджета со страницы. Срабатывает при вызове метода jivo_destroy().

```js
function jivo_onWidgetDestroy() {
  console.log('Widget is deleted')
}
```

## Методы

С помощью методов API можно кастомизировать виджет, получить или установить дополнительную информацию по клиентам. Вызов методов необходимо производить из коллбека [jivo_onLoadCallback](widget.md#onloadcallback), чтобы все проинициализировалось в правильном порядке.

### open

Метод позволяет открыть окно чата в различных состояниях.

| Название | Тип | Описание |
| --- | --- | --- |
| start `необязательный` | string | `call` - окно с формой обратного звонка, `menu` - мобильное меню с выбором канала связи, `chat` - Значение по умолчанию |

```js
let params = {start: 'call'};
let apiResult = jivo_api.open(params);

if (apiResult.result === 'fail') {
    console.log('Widget failed to open');
} else {
    console.log('Widget open successfully');
}
```

### close

Метод позволяет закрыть или свернуть окно диалога.

```js
let apiResult = jivo_api.close();

if (apiResult.result === 'fail') {
    console.log('Failed to close widget');
} else {
    console.log('Widget successfully close');
}
```

### showProactiveInvitation

С помощью этого метода вы можете вызвать окно активного приглашения в нужный момент. Это может быть полезно, например, если вы хотите показывать активное приглашение после того, как клиент добавил товар в корзину Интернет-магазина.

| Название | Тип | Описание |
| --- | --- | --- |
| invitation_text | string | Текст приглашения |
| department_id `необязательный` | number | Идентификатор отдела |

```js
jivo_api.showProactiveInvitation("How can I help you?", 3);
```

### setWidgetColor

Данный метод позволяет изменить цвет виджета.

| Название | Тип | Описание |
| --- | --- | --- |
| color | string | Шестнадцатеричный код цвета |
| color2 `необязательный` | string | Шестнадцатеричный код цвета, используется для создания градиента |

```js
jivo_api.setWidgetColor('#ffffff', '#000000');
```

### chatMode

С помощью этого метода можно получить текущий статус чата: онлайн/оффлайн.

| Название | Тип | Описание |
| --- | --- | --- |
| result | string | `online` - минимум один оператор в сети, `offline` - операторов нет в сети |

```js
function jivo_onLoadCallback() {
  let chatMode = jivo_api.chatMode();

  if (chatMode === 'offline') {
     console.log("Widget is offline");
  } else {
    console.log('Widget is online')
  }
}
```

### startCall

Метод позволяет начать звонок на определенный номер, если звонки доступны (Обратный звонок настроен и баланс звонков положителен).

| Название | Тип | Описание |
| --- | --- | --- |
| phone | string | Телефон |

```js
let phone = '+14084987855';
let apiResult = jivo_api.startCall(phone);

if (apiResult.result === 'ok') {
    console.log('Call started, phone: ', phone);
} else {
    console.log('Failed to start the call, reason: ', apiResult.reason);
}
```

### sendOfflineMessage

Данный метод позволяет отправить сообщение и предзаполнить форму контактов в офлайн-режиме чата (для отправки сообщения посетителю сайта необходимо вручную отправить форму контактов).

| Название | Тип | Описание |
| --- | --- | --- |
| name | string | Имя клиента |
| email | string | Email клиента |
| phone | string | Телефон клиента |
| description | string | Дополнительная информация о клиенте |
| message | string | Текст оффлайн-сообщения |

```js
let apiResult = jivo_api.sendOfflineMessage({
    "name": "John Smith",
    "email": "email@example.com",
    "phone": "+14084987855",
    "description": "Description text",
    "message": "Offline message"
});

if (apiResult.result === 'ok') {
    console.log('Message sent successfully');
} else {
    console.log('Error sending message, reason: ', apiResult.error);
}
```

### sendPageTitle

Обновляет в программе оператора заголовок и url страницы, на которой находится клиент, полезно для SPA-приложений.

| Название | Тип | Описание |
| --- | --- | --- |
| title | string | Идентификатор объявления |
| fromApi `необязательный` | string | Название кампании |
| url `необязательный` | string | Источник кампании |

```js
let title = 'This is custom page title';
let url = 'https://site.com/url_to_page?q=params';

jivo_api.sendPageTitle(title, true, url);
```

### setContactInfo

Устанавливает контактные данные посетителя. Данные отображаются оператору, как будто их ввел посетитель в форме контактов.

| Название | Тип | Описание |
| --- | --- | --- |
| name | string | Имя посетителя сайта |
| email | string | Email посетителя сайта |
| phone | string | Номер телефона посетителя сайта |
| description | string | Дополнительная информация по клиенту (отобразится в поле "Описание" - раздел "О клиенте") |

```js
jivo_api.setContactInfo({
    name: "John Smith",
    email: "email@example.com",
    phone: "+14084987855",
    description: "Description text"
});
```

### setClientAttributes

Устанавливает значения атрибутов, которые настроены в вашем аккаунте.
Для того чтобы задать значения, необходимо знать идентификаторы атрибутов, которые отображаются в приложении Jivo, в разделе "Управление" > "Настройки атрибутов".
Атрибуты будут отображаться в информационной панели диалога и обновляться в реальном времени.
**Важно: Метод может быть вызван не более 10 раз в течение часа для одного посетителя.**

| Название | Тип | Описание |
| --- | --- | --- |
| attributes | object | Список полей в формате ключ-значение |

```js
jivo_api.setClientAttributes({
  "Nazvanie_kompanii": "Компания",
  "Sajt_kompanii": "https://company-site.com",
  "Telegram_kanal": "https://t.me/telegram-channel",
  "Vozrast": 42
})
```

**Обратите внимание: для атрибута типа “Текст”, его значение - это строка (в кавычках), а для атрибута с типом “Число” - соответственно число (без кавычек).**

### setCustomData

С помощью этой функции можно передать произвольную дополнительную информацию о клиенте оператору. Информация отображается в информационной панели справа в приложении оператора.

Метод может быть вызван любое число раз - если диалог с оператором уже установлен, то данные в приложении оператора будут обновлены в реальном времени. Поля выводятся в порядке их следования в массиве fields. В запросе может быть не больше 10 полей.

**Важно: Для корректной передачи URL этим методом необходимо заполнить поле "Безопасный URL" в разделе "Управление" > "Каналы связи" > "Настроить" > "Настройки интеграции для разработчиков".**

| Название | Тип | Описание |
| --- | --- | --- |
| fields | array | Список полей диалога |
| fields.content | string | Содержимое поля данных. Теги экранируются |
| fields.title | string | Заголовок, добавляемый сверху поля данных |
| fields.link | string | URL, открываемый при клике на поле данных |
| fields.key | string | Описание поля данных, добавляемое жирным шрифтом перед содержимым поля через двоеточие |

```js
jivo_api.setCustomData([
    {
        "content": "User balance: $56"
    },
    {
        "content": "Open customer profile",
        "link": "..."
    },
    {
        "title": "Actions",
        "content": "Add contact",
        "link": "..."
    }
 ]);
```

### setUserToken

Устанавливает идентификатор посетителя. Jivo никак не обрабатывает этот идентификатор и не отображает его в приложении оператора, но передаёт его в каждом событии Webhooks. Таким образом можно идентифицировать посетителя сайта при обработке Webhooks. Рекомендуем использовать сложно-угадываемый идентификатор для исключения возможности спуфинга.

| Название | Тип | Описание |
| --- | --- | --- |
| token | string | Идентификатор посетителя |

```js
jivo_api.setUserToken(token);
```

### setRules

С помощью этого метода можно заменить автоматические действия на переданный объект. Пример объекта можно сформировать в панели управления Jivo, открыв раздел Автоматические действия и нажав кнопку JSON структура.

| Название | Тип | Описание |
| --- | --- | --- |
| rules | object | Описание правил активных приглашений на языке JSON |

```js
jivo_api.setRules(rules);
```

### getContactInfo

Возвращает данные посетителя, которые посетитель ввел в форме представления. Если посетитель не заполнил какие-либо поля, их значении будут равны null.

| Название | Тип | Описание |
| --- | --- | --- |
| client_name | string | Имя посетителя сайта |
| email | string | Email посетителя сайта |
| phone | string | Номер телефона посетителя сайта |
| description | string | Дополнительная информация по клиенту, установленная в setContactInfo |

```js
let apiResult = jivo_api.getContactInfo();
console.log('Name: ', apiResult.client_name);
console.log('Email: ', apiResult.email);
console.log('Phone: ', apiResult.phone);
console.log('Description: ', apiResult.description);
```

### getVisitorNumber

Асинхронная функция для получения уникального номера посетителя в Jivo. Посетители нумеруются последовательно, начиная с 1, число постоянно растет. Номер посетителя отображается в программе оператора и в журнала и может использоваться для связи данных Jivo с данными CRM.

| Название | Тип | Описание |
| --- | --- | --- |
| err | string | Строка с ошибкой |
| visitorNumber | integer | Номер посетителя |

```js
jivo_api.getVisitorNumber(function(error, visitorNumber) {
    if (error) {
        console.log('Error: ', error);
        return;
    }  
    console.log('Visitor number: ', visitorNumber);
});
```

### getUnreadMessagesCount

Данный метод позволяет получить количество непрочитанных сообщений от оператора.

```js
let count = jivo_api.getUnreadMessagesCount();
console.log('Unread messages count:', count);
```

### getUtm

Данный метод позволяет получить utm-метки, если они были при первом переходе клиента на сайт.

| Название | Тип | Описание |
| --- | --- | --- |
| content | string | Идентификатор объявления |
| campaign | string | Название кампании |
| source | string | Источник кампании |
| medium | string | Тип трафика |
| term | string | Ключевое слово |

```js
let utm = jivo_api.getUtm();

console.log('Utm content: ', utm.content);
console.log('Utm campaign: ', utm.campaign);
console.log('Utm source: ', utm.source);
console.log('Utm medium: ', utm.medium);
console.log('Utm term: ', utm.term);
```

### isCallbackEnabled

Данный метод проверяет, доступны ли звонки.

```js
jivo_api.isCallbackEnabled(function(apiResult) {
    if (apiResult.result === 'ok') {
        jivo_api.open({start: 'call'});
    } else {
        console.log('Callback is not available, reason: ', apiResult.reason);
    }
});
```

### clearHistory

Метод jivo_api.clearHistory() позволяет удалить историю чата и данные пользователя из локального хранилища браузера пользователя. Применимо в случае, если необходимо очищать данные сессии при деавторизации из кабинета на сайте.

```js
function jivo_onLoadCallback() {
   let clearHistory = () => {
    jivo_api.clearHistory();
    console.log('Client data is deleted')
  };

  clearHistory();
};
```

### jivo_init, jivo_destroy

Указанные методы можно использовать для отображения виджета Jivo (jivo_init) или его удаления со страницы (jivo_destroy). Например, в SPA-приложениях, если необходимо динамически скрывать или отображать чат на странице.

```js
function jivo_onLoadCallback() {
  jivo_destroy();
  console.log('Widget is deleted')
}
```