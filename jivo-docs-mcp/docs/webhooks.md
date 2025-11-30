---
title: Webhooks API
source_url: https://www.jivo.ru/docs/webhooks/
---

# Webhooks API

Используйте **Webhooks** для того, чтобы получать уведомления при возникновении различных событий, связанных с обращениями клиентов из разных каналов связи **Jivo**.

В настройках канала связи можно настроить HTTP(S) URL, на который будет отправляться запрос при возникновении того или иного события. Событие передается по указанному URL POST-запросом. Тело запроса представляет собой JSON-объект с информацией о событии.

Тип события определяется строковым полем **event_name**, который всегда присутствует в структуре **event**. Остальные поля зависят от конкретного события. В ответ на HTTP-запрос для некоторых типов событий вы можете вернуть данные, которые будут отображены оператору, принявшему диалог.

## call_event

Событие отправляется когда операторы получают новый звонок или изменяется статус текущего звонка.

Пример:

```json
{
    "event_name": "call_event",
    "chat_id": 4398,
    "topic": {
       "topic_id": 3,
       "title": "Topic_1",
       "parent_id": 1
 },
    "widget_id": "2853",
    "visitor": {
        "name": "John Smith",
        "email": "email@example.com",
        "phone": "+14084987855",
        "number": "2746",
        "description": "Description text",
        "social": {},
        "chats_count": 8
    },
    "agent": {
        "id": "3599",
        "name": "Thomas Anderson",
        "email": "agent@jivosite.com",
        "phone": "+14083682346"
    },
    "department": {
        "id": 181,
        "name": "Sales"
    },
    "session": {
        "geoip": {
            "region_code": "CA",
            "country": "United States",
            "country_code": "US",
            "region": "California",
            "city": "San Francisco",
            "latitude": "37.7898",
            "longitude": "-122.3942",
            "organization": "Wikimedia Foundation"
        },
        "utm": "source=google|medium=cpc|content=banner|campaign=campaign_name",
        "utm_json": {
            "source": "google",
            "campaign": "campaign_name",
            "content": "banner",
            "medium": "cpc",
            "term": "..."
        },
        "ip_addr": "208.80.152.201",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
    },
    "page": {
        "url": "http://example.com/",
        "title": "Page title"
    },
    "call": {
        "type": "callback",
        "phone": "+14084987855",
        "status": "end",
        "record_url": "http://example.com/record.mp3"
    },
    "analytics": {}
}
```

## chat_accepted

Событие возникает в момент приема диалога оператором. В параметрах запроса передаются все известные данные о посетителе, а также данные оператора, принявшего диалог. Кроме того, в параметрах присутствует идентификатор пользователя, если он был передан в виджет путем вызова [setUserToken](widget.md#set-user-token/).

При возврате в ответе на **chat_accepted** объекта **contact_info**, все поля из него будут показаны оператору так, как будто их ввёл посетитель. Они же сохранятся в журнале диалога и письме.

**Пример**

```json
{
    "event_name": "chat_accepted",
    "widget_id": "3948",
    "user_token": null,
    "visitor": {
        "name": "John Smith",
        "email": "email@example.com",
        "phone": "+14084987855",
        "description": "Description text",
        "number": "2198",
        "social": {},
        "chats_count": 1
    },
    "organization": {
      "id": "1",
      "name": "Company name"
    },
    "status": {
      "id": "4",
      "title": "contact_later"
    },
    "assigned_agent": {
      "id": 1,
      "email": "agent1@gmail.com",
      "name": "Agent"
    },
    "tags": [
    {
      "id": "17",
      "title": "Tag example"
    }
  ],
    "chat_id": 7636,
    "topic": {
       "topic_id": 3,
       "title": "Topic_1",
       "parent_id": 1
 },
    "department": {
        "id": 281,
        "name": "Sales"
    },
    "session": {
        "geoip": {
            "region_code": "CA",
            "country": "United States",
            "country_code": "US",
            "region": "California",
            "city": "San Francisco",
            "latitude": "37.7898",
            "longitude": "-122.3942",
            "organization": "Wikimedia Foundation"
        },
        "utm": "source=google|medium=cpc|content=banner|campaign=campaign_name",
        "utm_json": {
            "source": "google",
            "campaign": "campaign_name",
            "content": "banner",
            "medium": "cpc",
            "term": "..."
        },
        "ip_addr": "208.80.152.201",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
    },
    "page": {
        "url": "http://example.com/",
        "title": "Page title"
    },
    "analytics": {},
    "agent": {
        "id": "2016",
        "name": "Thomas Anderson",
        "email": "agent@jivosite.com",
        "phone": "+14083682346"
    }
}
```

**Параметры ответа**

| Название | Тип | Описание |
| --- | --- | --- |
| result | string | Строка результата обработки. Если значение не равно "ok", данные не будут переданы оператору |
| custom_data | array | Поля дополнительных данных, аналогично [setCustomData](widget.md#set-custom-data/) |
| contact_info | object | Поля контактных данных, аналогично [setContactInfo](widget.md#set-contact-info/) |
| enable_assign | boolean | Флаг, определяющий отображению оператору кнопки привязки посетителя к карточке в CRM. Кнопка отображается в шапке диалога, между кнопками "В спам" и "Выйти из диалога" |
| crm_link | string | Ссылка на карточку клиента в CRM. Кнопка "Открыть в CRM" отображается оператору в информационной панели диалога в разделе "Подробнее о визите" |
| page | object | Информация о странице |

**custom_data**

| Название | Тип | Описание |
| --- | --- | --- |
| title | string | Название пользовательского поля |
| content | string | Содержимое |

**contact_info**

| Название | Тип | Описание |
| --- | --- | --- |
| name | string | Имя посетителя |
| phone `необязательный` | string | Телефон посетителя |
| email `необязательный` | string | E-mail посетителя |

**page**

| Название | Тип | Описание |
| --- | --- | --- |
| url | string | URL текущей страницы |
| title `необязательный` | string | Заголовок страницы |

**Пример**

```json
 {
    "result": "ok",
    "custom_data": [
        {
            "title": "Title",
            "content": "Content text"
        }
    ],
    "contact_info": {
        "name": "John Smith",
        "phone": "+14084987855",
        "email": "email@example.com"
    },
   "crm_link": "https://example.com"
}
```

## chat_updated

Событие будет отправлено в случае, если информация о посетителе была обновлена во время активного диалога - например, были введены контакты в форме чата. В параметрах запроса передаются все известные данные о посетителе, а также данные оператора, принявшего диалог. Кроме того, в параметрах присутствует идентификатор пользователя, если он был передан в виджет путем вызова [setUserToken](widget.md#setusertoken/).

**Пример**

```json
{
    "event_name": "chat_updated",
    "widget_id": "3948",
    "user_token": null,
    "visitor": {
        "name": "John Smith",
        "email": "email@example.com",
        "phone": "+14084987855",
        "description": "Description text",
        "number": "2198",
        "chats_count": 1
    },
    "organization": {
      "id": "2",
      "name": "Company name"
    },
    "status": {
      "id": "4",
      "title": "contact_later"
    },
    "assigned_agent": null,
    "tags": [
      {
        "id": "7",
        "title": "Discount"
      }
    ],
    "chat_id": 7507,
    "topic": {
       "topic_id": 3,
       "title": "Topic_1",
       "parent_id": 1
 },
    "department": {
        "id": 281,
        "name": "Sales"
    },
    "session": {
        "geoip": {
            "region_code": "CA",
            "country": "United States",
            "country_code": "US",
            "region": "California",
            "city": "San Francisco",
            "latitude": "37.7898",
            "longitude": "-122.3942",
            "organization": "Wikimedia Foundation"
        },
        "utm": "source=google|medium=cpc|content=banner|campaign=campaign_name",
        "utm_json": {
            "source": "google",
            "campaign": "campaign_name",
            "content": "banner",
            "medium": "cpc",
            "term": "..."
        },
        "ip_addr": "208.80.152.201",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
    },
    "page": {
        "url": "http://example.com/",
        "title": "Page title"
    },
    "analytics": {},
    "agent": {
        "id": "2016",
        "name": "Thomas Anderson",
        "email": "agent@jivosite.com",
        "phone": "+14083682346"
    }
}
```

**Параметры ответа**

| Название | Тип | Описание |
| --- | --- | --- |
| result | string | Строка результата обработки. Если значение не равно "ок", данные не будут переданы оператору |
| custom_data | array | Поля дополнительных данных, аналогично [setCustomData](widget.md#set-custom-data/) |
| contact_info | object | Поля контактных данных, аналогично [setContactInfo](widget.md#set-contact-info/) |
| enable_assign | boolean | Флаг, определяющий отображению оператору кнопки привязки посетителя к карточке в CRM. Кнопка отображается перед всеми полями custom_data |
| crm_link | string | Ссылка на карточку клиента в CRM. Отображается оператору отдельной кнопкой под всеми полями custom_data |
| page | object | Информация о странице |

## client_updated

Отправку события инициирует обновление данных клиента.

Например:

- В карточке клиента был обновлен ответственный сотрудник или организация, к которой относится клиент.
- Изменены контактные данные клиента вне принятого диалога с ним (в разделе "CRM" - "Клиенты").
- Посетитель указал свои контакты во [всплывающем окне](https://www.jivo.ru/help/marketing/pop-up-windows.html) на сайте.

**Пример**

```json
{
  "event_name": "client_updated",
  "widget_id": "12345678",
  "user_token": null,
  "visitor": {
    "name": "Thomas",
    "email": "thomas@gmail.com",
    "phone": "+458745457845",
    "description": "Description text",
    "number": 1217,
    "chats_count": 1
  },
  "organization": {
    "id": "1",
    "name": "Company name"
  },
  "status": {
    "id": "4",
    "title": "contact_later"
  },
  "assigned_agent": {
    "id": 3,
    "email": "agent3@gmail.com",
    "name": "Agent3"
  },
  "tags": [
    {
      "id": "17",
      "title": "Sales"
    }
  ],
  "client_id": "1217"
}
```

**Параметры ответа**

В качестве ответа ожидается только JSON {"result": "ok"} или текст ошибки.

**Пример**

```json
{
    "result": "ok"
}
```

## client_attribute_updated

Событие отправляется когда изменяются атрибуты клиента: их обновил оператор в приложении или клиент заполнил поле с атрибутом в форме контактов.

**Пример**

```json
{
  "event_name": "client_attribute_updated",
  "widget_id": "12345678",
  "user_token": null,
  "client_id": 1217,
  "attributes": [
    "some_number_attribute_name": 1234,
    "some_string_attribute_name": "Some string",
    ...
    <attribute_name: string>: <attribute_value: mixed>,
  ]
}
```

## chat_finished

Событие отправляется при завершении чата в приложении оператора. В параметрах запроса передаются все известные данные о посетителе, массив с сообщениями чата, а также данные операторов, принимавших участие в диалоге. Кроме того, в параметрах присутствует идентификатор пользователя, если он был передан в виджет путем вызова [setUserToken](widget.md#setusertoken/).

**Пример**

```json
{
    "event_name": "chat_finished",
    "widget_id": "3948",
    "visitor": {
        "name": "John Smith",
        "email": "email@example.com",
        "phone": "+14084987855",
        "description": "Description text",
        "number": "2198",
        "chats_count": 2
    },
    "organization": null,
    "status": null,
    "assigned_agent": null,
    "tags": [],
    "chat_id": 7607,
    "topic": {
       "topic_id": 3,
       "title": "Topic_1",
       "parent_id": 1
 },
    "session": {
        "geoip": {
            "region_code": "CA",
            "country": "United States",
            "country_code": "US",
            "region": "California",
            "city": "San Francisco",
            "latitude": "37.7898",
            "longitude": "-122.3942",
            "organization": "Wikimedia Foundation"
        },
        "utm": "source=google|medium=cpc|content=banner|campaign=campaign_name",
        "utm_json": {
            "source": "google",
            "campaign": "campaign_name",
            "content": "banner",
            "medium": "cpc",
            "term": "..."
        },
        "ip_addr": "208.80.152.201",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
    },
    "page": {
        "url": "http://example.com/",
        "title": "Page title"
    },
    "analytics": null,
    "agents": [
        {
            "id": "1",
            "name": "Thomas Anderson",
            "email": "agent@jivosite.com",
            "phone": "+14083682346"
        }
    ],
    "chat": {
      "messages": [
        {
          "message": "<Message text is not displayed here>",
          "timestamp": 1665396476,
          "type": "visitor"
        },
        {
          "message": "<Message text is not displayed here>",
          "timestamp": 1665396483,
          "type": "agent",
          "agent_id": 1
        }
      ],
        "blacklisted": false,
        "rate": null
    },
    "plain_messages": "",
    "html_messages": ""
}
```

**Параметры ответа**

В качестве ответа ожидается только JSON {"result": "ok или текст ошибки"}

**Пример**

```json
{
    "result": "ok"
}
```

## offline_message

Событие будет отправлено в момент отправки сообщения через оффлайн-форму. В параметрах запроса передаются все известные данные о посетителе, а также текст оффлайн сообщения. Кроме того, в параметрах присутствует идентификатор пользователя, если он был передан в виджет путем вызова [setUserToken](widget.md#setusertoken/).

**Пример**

```json
{
    "event_name": "offline_message",
    "widget_id": "3948",
    "user_token": null,
    "visitor": {
        "name": "John Smith",
        "email": "email@example.com",
        "phone": "+14084987855",
        "description": "Description text",
        "number": "2198",
        "chats_count": 1
    },
    "organization": null,
    "status": null,
    "assigned_agent": null,
    "tags": [],
    "chat_id": 2026,
    "topic": {
       "topic_id": 3,
       "title": "Topic_1",
       "parent_id": 1
 },
    "session": {
        "geoip": {
            "region_code": "CA",
            "country": "United States",
            "country_code": "US",
            "region": "California",
            "city": "San Francisco",
            "latitude": "37.7898",
            "longitude": "-122.3942",
            "organization": "Wikimedia Foundation"
        },
        "utm": "source=google|medium=cpc|content=banner|campaign=campaign_name",
        "utm_json": {
            "source": "google",
            "campaign": "campaign_name",
            "content": "banner",
            "medium": "cpc",
            "term": "..."
        },
        "ip_addr": "208.80.152.201",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36"
    },
    "page": {
        "url": "http://example.com/",
        "title": "Page title"
    },
    "analytics": {},
    "message": "Message text",
    "offline_message_id": 1665399500726
}
```

**Параметры ответа**

В качестве ответа ожидается только JSON {"result": "ok} или текст ошибки.

**Пример**

```json
{
    "result": "ok"
}
```

## Параметры события

**event**

| Название | Тип | Описание |
| --- | --- | --- |
| event_name | string | Тип события |
| widget_id | string | Идентификатор канала связи |
| user_token | string | Токен пользователя |
| visitor | object | Объект с информацией о посетителе |
| organization | object | Объект с информацией о компании, к которой принадлежит клиент |
| status | object | Категория клиента |
| assigned_agent | object | Данные об ответственном сотруднике |
| tags | object | Теги, присвоенные клиенту |
| chat_id | number | Идентификатор чата |
| department `необязательный` | object | Объект с информацией об отделе, который посетитель выбрал перед началом чата |
| session | object | Данные о сессии пользователя |
| page | object | Информация о странице |
| call | object | Информация о звонке |
| analytics `необязательный` | object | Аналитика |
| agent | object | Объект с информацией об операторе |
| chat | object | Сообщения чата |
| topic | object | Объект с информацией о теме диалога, которую выбрал оператор |
| topic_id | number | Идентификатор темы |
| title | string | Название темы |
| parent_id | number | Идентификатор родительской темы |

**visitor**

| Название | Тип | Описание |
| --- | --- | --- |
| name `необязательный` | string | Имя посетителя |
| email `необязательный` | string | Email посетителя |
| phone `необязательный` | string | Телефон посетителя |
| description | string | Дополнительная информация (описание) по клиенту |
| number | string | Номер посетителя |
| social `необязательный` | object | Данные о социальных сетях пользователя |
| chats_count | number | Количество обращений |

**organization**

| Название | Тип | Описание |
| --- | --- | --- |
| id | number | Идентификатор компании |
| name | string | Название компании |

**status**

| Название | Тип | Описание |
| --- | --- | --- |
| id | number | Идентификатор категории клиента |
| title | string | Название категории |

**assigned_agent**

| Название | Тип | Описание |
| --- | --- | --- |
| id | number | Идентификатор ответственного по клиенту сотрудника |
| email | string | Email сотрудника |
| name | string | Имя сотрудника |

**tags**

| Название | Тип | Описание |
| --- | --- | --- |
| id | number | Идентификатор тега |
| title | string | Наименование тега |

**department**

| Название | Тип | Описание |
| --- | --- | --- |
| id | number | Идентификатор отдела |
| name | string | Название отдела |

**session**

| Название | Тип | Описание |
| --- | --- | --- |
| geoip | object | Данные из geoip клиента |
| utm | string | UTM-метки в строковом формате |
| utm_json | object | Объект, содержащий UTM-метки |
| ip_addr | string | IP-адрес активной сессии |
| user_agent | string | Описание user_agent |

**page**

| Название | Тип | Описание |
| --- | --- | --- |
| url | string | URL текущей страницы |
| title `необязательный` | string | Заголовок страницы |

**agent**

| Название | Тип | Описание |
| --- | --- | --- |
| id | number | Идентификатор оператора |
| email | string | Email оператора |
| name | string | Имя оператора |
| phone `необязательный` | string | Телефон оператора |

**call**

| Название | Тип | Описание |
| --- | --- | --- |
| type | string | Tип звонка (callback, incoming, outgoing) |
| phone | string | Номер телефона клиента |
| status | string | Статус звонка (start, end, agent_connected, client_connected, error) |
| reason `необязательный` | string | Причина ошибки (доступна, когда звонок завершился с ошибкой) |
| record_url `необязательный` | string | Ссылка на запись звонка в формате mp3 (доступна после завершения звонка) |

**chat**

| Название | Тип | Описание |
| --- | --- | --- |
| messages | object | Объект с сообщениями чата |
| blacklisted | boolean | Информация о блокировке пользователя |
| rate `необязательный` | string | Оценка состоявшегося чата |
| invitation `необязательный` | string | Текст активного приглашения |

**messages**

| Название | Тип | Описание |
| --- | --- | --- |
| message | string | Текст сообщения |
| timestamp | int | Метка времени |
| type | string | Тип пользователя (оператор или клиент) |
| agent_id | number | Идентификатор оператора, который отправил сообщение |

**geoip**

| Название | Тип | Описание |
| --- | --- | --- |
| region_code | string | Код региона |
| country_code | string | ISO код страны |
| country | string | Название страны |
| region | string | Регион |
| city | string | Город |
| latitude | string | Широта |
| longitude | string | Долгота |
| organization | string | Название Интернет-провайдера |

**utm_json**

| Название | Тип | Описание |
| --- | --- | --- |
| source `необязательный` | string | Значение utm_source |
| campaign `необязательный` | string | Значение utm_campaign |
| content `необязательный` | string | Значение utm_content |
| medium `необязательный` | string | Значение utm_medium |
| term `необязательный` | string | Значение utm_term |

# CRM Webhooks

В Webhooks API теперь добавлены события по добавлению и изменению сущностей в CRM Jivo.

Адрес сервера, на который будут отправляться запросы с данными о событии, настраивается в разделе "Настройки CRM" - "CRM Webhooks".
Запрос отправляется с использованием метода POST, тело запроса передаётся в формате JSON.

Категория события (сущность СRM, c которой происходили изменения) определяется полем **event_type**. Тип действия _(добавление, изменение, удаление)_ можно определить по значению поля **event_name**.

## Воронки (crm_pipeline)

Событие отправляется при добавлении воронки в разделе "Настройки CRM" - "Воронки" или изменении её настроек.

Возможные типы событий:

- **created_pipeline** - добавление новой воронки
- **updated_pipeline** - обновление настроек существующей воронки (редактирование этапов, причин отказа, валюты)
- **deleted_pipeline** - удаление воронки

Пример:

```json
{
		{
            "event_name": "created_pipeline",
			"pipeline_id": 6,
			"title": "Gruzly",
			"currency": "RUB",
			"pipeline_statuses": [{
				"pipeline_status_id": 19,
				"title": "finished",
				"position": 0,
				"color": "0ed16a",
				"type": "system",
				"final_status": "successful"
			}, {
				"pipeline_status_id": 20,
				"title": "unsuccessful",
				"position": 0,
				"color": "76869d",
				"type": "system",
				"final_status": "unsuccessful"
			}, {
				"pipeline_status_id": 21,
				"title": "Новая",
				"position": 1,
				"color": "1fb6fd",
				"type": "user",
				"final_status": null
			}],
			"pipeline_reject_reasons": [{
				"pipeline_reject_reason_id": 21,
				"title": "Слишком дорого",
				"position": 0
			}, {
				"pipeline_reject_reason_id": 22,
				"title": "Пропала потребность",
				"position": 1
			}, {
				"pipeline_reject_reason_id": 23,
				"title": "Не устроили условия",
				"position": 2
			}, {
				"pipeline_reject_reason_id": 24,
				"title": "Выбрали других",
				"position": 3
			}]
		}
```

#### Параметры события

| Название | Тип | Описание |
| --- | --- | --- |
| event_name | string | Тип события |
| pipeline_id | number | Идентификатор воронки |
| title | string | Название воронки |
| currency | string | Международный код валюты |
| pipeline_statuses | array | Массив с данными о этапах (статусах) воронки |
| pipeline_status_id | number | ID этапа |
| title | string | Название этапа |
| position | number | Порядковый номер (положение значения этапа в списке) |
| color | string | Цвет элемента (указывается в формате HEX) |
| type | string | Информация, кем был добавлен этап (системой или пользователем) |
| final_status | string | Статус успешного или неуспешного завершения сделки |
| pipeline_reject_reasons | array | Массив с информацией о причинах отказа. Содержит поля pipeline_reject_reason_id, title и position |

## Категории (сrm_status)

Отправка события с "event_type": "crm_status" срабатывает, когда редактируются настройки категорий клиентов в разделе "Настройки CRM" - "Категории".

Типы события:

- created_status - добавление новой категории
- updated_status - обновление текущей категории
- deleted_status - удаление категории
- reordered_status - изменение положения категории в списке
- assigned_status - назначение категории клиенту
- changed_require_update_of_status - переключение настройки "Требовать обновление категории при завершении диалога"

Пример:

```json
{
		{
			"event_name": "assigned_status",
			"status": {
				"title": "unsuccessful",
				"color": "76869d",
				"position": 3,
				"status_id": 5,
				"new_status_id": null
			},
			"client": {
				"client_id": 1,
				"widget": {
					"widget_id": 488651
				},
				"name": "John Smith",
				"avatar_url": null,
				"description": null,
				"social": null,
				"assigned_agent": {
					"assigned_agent_id": null
				},
				"crm_link": null,
				"chats_count": 0,
				"visits_count": 0,
				"custom_data": null,
				"status": {
					"title": "unsuccessful",
					"color": "76869d",
					"position": 3,
					"status_id": 5,
					"new_status_id": null
				},
				"organization": null,
				"tags": [],
				"has_deal": 1,
				"contacts": [{
					"contact_type": "email",
					"contact": "johnsmith@mail.com",
					"channel_type": "agent_app"
				}],
				"blacklist": null
			}
		}
	}
```

Описание параметров объекта **client** доступно в [Webhooks API.](webhooks.md#parametry-sobytiya)

Пример:

```
{
		{
			"event_name": "created_status"/"updated_status"/"deleted_status";
			"title": "Vno",
			"color": "0363f6",
			"position": 6,
			"status_id": 6,
			"new_status_id": null
		}
}
```

Параметры события

| Название | Тип | Описание |
| --- | --- | --- |
| event_name | string | Тип события |
| title | string | Название категории |
| color | string | Цвет элемента (указывается в формате HEX) |
| position | number | Порядковый номер (положение категории в списке) |
| position | number | Порядковый номер (положение категории в списке) |
| status_id | number | ID категории |
| new_status_id | number | ID категории, на который будут переведены после удаления текущего категории |

Пример:

```json
{
		 {
			"event_name": "assigned_status",
			"status": {
				"title": "unsuccessful",
				"color": "76869d",
				"position": 3,
				"status_id": 5,
				"new_status_id": null
			},
			"client": {
				"client_id": 1,
				"widget": {
					"widget_id": 488651
				},
				"name": "John Smith",
				"avatar_url": null,
				"description": null,
				"social": null,
				"assigned_agent": {
					"assigned_agent_id": null
				},
				"crm_link": null,
				"chats_count": 0,
				"visits_count": 0,
				"custom_data": null,
				"status": {
					"title": "unsuccessful",
					"color": "76869d",
					"position": 3,
					"status_id": 5,
					"new_status_id": null
				},
				"organization": null,
				"tags": [],
				"has_deal": 1,
				"contacts": [{
					"contact_type": "email",
					"contact": "johnsmith@mail.com",
					"channel_type": "agent_app"
				}],
				"blacklist": null
			}
		}
	}
```

Описание параметров объекта **client** доступно ниже.

## Теги (crm_client_tag)

Отправку этого события инициирует управление тегами, которые используются для обозначения сегмента в карточке клиента. В разделе "Настройки CRM" - "Теги" можно добавлять, удалять или объединять теги.

Типы событий:

- **сreated_client_tag** - добавление нового тега
- **updated_client_tag** - обновление существующего тега
- **deleted_client_tag** - удаление тега
- **merged_client_tag** - объединениe текущих тегов в один
- **changed_administrator_only_client_tag** - управление настройкой "Добавлять теги могут только администраторы"

Примеры:

```json
{
		{
			"event_name": "created_client_tag",
			"tag_id": 1,
			"title": "Test_tag"
		}
}
```

```
{
		{
			"event_name": "merged_tag",
			"tag": {
				"tag_id": 6,
				"title": "NewOne"
			},
			"merged_tags": [{
				"tag_id": 9,
				"title": "SecondOne"
			}, {
				"tag_id": 10,
				"title": "ThirdOne"
			}]
		}
}
```

```
 {
		{
			"event_name": "changed_administrator_only_client_tag",
			"enabled": 1
		}
}
```

Параметры событий

| Название | Тип | Описание |
| --- | --- | --- |
| event_name | string | Тип события |
| tag_id | number | Идентификатор тега |
| title | string | Название тега |
| merged_tags | array | Массив с данными об объединенных тегах |
| enabled | boolean | Были ли изменены настройки управления тегами 1 - создавать теги могут только администраторы; 0 - создавать теги могут все сотрудники |

## Cделки (crm_deal)

Запрос с такой категорией события отправляется каждый раз, когда добавляется сделка или изменяются данные в ней.

Типы событий:

- created_deal - добавление новой сделки
- updated_deal - редактирование текущей сделки
- deleted_deal - удаление сделки

Пример:

```json
{
		{
			"event_name": "created_deal"/"updated_deal"/"deleted_deal",
			"deal_id": 3,
			"client": {
				"client_id": 1
			},
			"title": "Сделка",
			"text": "Описание сделки",
			"amount": null,
			"pipeline": {
				"pipeline_id": 1,
				"pipeline_status": {
					"pipeline_status_id": 1
				},
				"pipeline_reject_reason": {
					"pipeline_reject_reason_id": null
				}
			},
			"assigned_agent": {
				"assigned_agent_id": 1
			},
			"created_ts": 1677837220,
			"closed_ts": null,
			"creator_agent": {
				"creator_agent_id": 1
			}
		}
	}
```

Параметры событий

| Название | Тип | Описание |
| --- | --- | --- |
| event_name | string | Тип события |
| deal_id | number | Идентификатор сделки |
| client | object | Объект с данными о клиенте, на которого была добавлена сделка |
| title | string | Название сделки |
| text | string | Описание сделки |
| amount | number | Cумма сделки |
| pipeline | object | Объект с указанием воронки и статуса сделки |
| assigned_agent | object | Данные о назначенном на сделку операторе |
| created_ts | int | Временная метка |
| created_ts | int | Время создания сделки в формате timestamp |
| closed_ts | int | Время закрытия сделки в формате timestamp |
| creator_agent | object | Объект с информацией о создателе сделки |

## Задачи (crm_task)

Отправку этого события вызывает работа с функционалом задач: добавление, удаление, редактирование и тд. В теле запроса передаются данные о самой задаче, а также информация о связанных с ней клиенте и сделке.

Типы событий:

- created_task - добавление новой задачи
- deleted_task - удаление задачи
- updated_task - изменение задачи
- completed_task - завершение задачи
- fired_task - срабатывание напоминания о задаче

Пример:

```json
{
		{
			"event_name": "created_task"/"deleted_task"/"updated_task"/"completed task"/"fired_task",
			"text": "Текст задачи",
			"status": "active",
			"task_id": 2,
			"agent": {
				"agent_id": 1
			},
			"client": {
				"client_id": 1
			},
			"notify_ts": 1677838380,
			"created_ts": 1677837822,
			"updated_ts": 1677837842,
			"show_notification": 1,
			"creator_agent": {
				"creator_agent_id": 1
			},
			"deal": {
				"deal_id": 3
			}
		}
	}
```

Параметры событий

| Название | Тип | Описание |
| --- | --- | --- |
| event_name | string | Тип события |
| text | string | Описание задачи |
| task_id | number | Идентификатор задачи |
| agent | object | Данные о сотруднике, на которого назначена задача |
| client | object | Информация о клиенте, к которому была привязана задача |
| notify_ts | int | Время, когда сработает напоминание о задаче. Указывается в формате timestamp |
| created_ts | int | Время создания задачи в формате timestamp |
| updated_ts | int | Время обновления задачи в формате timestamp |
| show_notification | boolean | Будет ли показано напоминание о задаче 1 - напоминание включено 0 - не будет показано |
| creator_agent | object | Информация о сотруднике, который создал задачу |
| deal | object | Данные о сделке, к которой связана задача |

## Организации (crm_organization)

Событие отправляется в момент создания организации (компании), за которой может быть закреплен клиент. В данной категории предусмотрен только один тип события - **created_organization**, т.к. другие действия с организациями не доступны. Тело запроса содержит только 2 параметра: event_name    и organization_id.

Пример:

```json
{
  {
    "event_name": 
		"created_organization",
		"organization_id": 3,
  }
}
```

## Клиенты (сrm_client)

Отправку события инициируют действия с карточкой клиента: её добавление, редактирование, удаление.

Типы событий:

- **assigned_agent_to_client** - назначение ответственного по клиенту оператора
- **created_client** - добавление клиента
- **deleted_client** - удаление клиента
- **updated_client** - обновление клиента
- **changed_client_company** - смена компании у клиента
- **changed_client_blacklist** - блокировка/разблокировка клиента
- **updated_client_contacts** - редактирование контактных данных клиента

Структура тела вебхука и его параметры идентичны для каждого из типа событий.

Пример:

```json
{
		{
			"event_name": "assigned_agent_to_client",
			"client_id": 1,
			"widget": {
				"widget_id": 488651
			},
			"name": "John Smith",
			"avatar_url": null,
			"description": null,
			"social": null,
			"assigned_agent": {
				"assigned_agent_id": 2
			},
			"crm_link": null,
			"chats_count": 0,
			"visits_count": 0,
			"custom_data": null,
			"status": {
				"title": "new",
				"color": "1fb6fd",
				"position": 0,
				"status_id": 1,
				"new_status_id": null
			},
			"organization": {
				"organization_id": 3,
				"name": "Company"
			},
			"tags": [],
			"has_deal": 1,
			"contacts": [{
				"contact_type": "email",
				"contact": "johnsmith@mail.com",
				"channel_type": "agent_app"
			}],
			"blacklist": {
				"agent": {
					"agent_id": 1
				},
				"block_datetime_ts": 1677838504,
				"unblock_datetime_ts": 1709460904,
				"ip_address": "109.252.14.36"
		}
	}
```

Параметры события

| Название | Тип | Описание |
| --- | --- | --- |
| event_name | string | Тип события |
| client_id | number | Идентификатор клиент |
| widget | object | Информация о канале связи, куда был добавлен клиента (включает в себя публичный id канала) |
| name | string | Имя клиента |
| client | object | Информация о клиенте, к которому была привязана задача |
| avatar_url | string | Ссылка на медиафайл с аватаром клиента (актуально для каналов соцсетей и сhat API, где предусмотрена передача подобной ссылки) |
| description | string | Описание к клиенту |
| social | object | Объект со ссылками на профиль клиента в соцсетях и мессенджерах |
| crm_link | string | Ссылка на карточку клиента в CRM |
| chats_count | number | Количество диалогов с клиентом |
| visits_count | number | Количество посещений |
| сustom_data | object | Дополнительная информация о клиенте, переданная с помощью метода [setCustom Data](widget.md#set-custom-data) |
| status | object | Данные о категории, назначенной клиенту |
| organization | object | Компания, к которой привязан клиент |
| tags | array | Теги, присвоенные клиенту |
| has_deal | boolean | Создана ли сделка с клиентом |
| сontacts | array | Контактные данные клиента |
| сontact_type | string | Тип контакта **phone/email** - номер телефона/электронная почта |
| contact | string | Номер телефона/адрес почты |
| сhannel_type | string | Где были добавлены контактные данные: **agent_app** - приложение оператора, **widget** - внешние контакты |
| blacklist | object | Данные о добавлении клиента в черный список или его разблокировке |
| agent | object | Информация об операторе, который блокировал клиента |
| block_datetime_ts | int | Время блокировки в формате timestamp |
| unblock_datetime_ts | int | Время разблокировки в формате timestamp |
| ip_address | string | IP-адрес клиента |