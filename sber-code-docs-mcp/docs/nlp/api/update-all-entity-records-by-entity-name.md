# Обновить содержание сущности
Обновлено 31 октября 2025
[](https://public.oprosso.sberbank.ru/p/docs_csi_2025)
Production
PUT
```

https://smartapp-code.sberdevices.ru/cailapub//api/caila/p/{accessToken}/entities-by-name/{entityName}/records

```

Обновить содержание сущности
## Запрос
### Path Parameters
accessToken
string
required
Токен доступа, который можно найти в настройках проекта
entityName
string
required
Уникальное имя сущности

### Bodyrequired
application/json
Список новых записей для сущности
**data** NamedEntityRecordData[]required
  * Array [
id
int64
type
NamedEntityRecordType (string)
required
**Возможные значения:** [`pattern`, `synonyms`]
rule
string[]
required
value
string
required
Значение, связанное с сущностью. Как правило — строка, число или JSON-объект
clientId
string
  * ]
clientId
string

## Ответы
200
Список новых интентов
application/json
**Schema**
  * Array [
id
int64
type
NamedEntityRecordType (string)
required
**Возможные значения:** [`pattern`, `synonyms`]
rule
string[]
required
value
string
required
Значение, связанное с сущностью. Как правило — строка, число или JSON-объект
clientId
string
  * ]

Пример запроса
payload
application/json
```
{  
"data":[  
{  
"id":0,  
"type":"pattern",  
"rule":[  
"string"  
],  
"value":"string",  
"clientId":"string"  
}  
],  
"clientId":"string"  
}  

```

Пример ответа
200
application/json
```
[  
{  
"id":0,  
"type":"pattern",  
"rule":[  
"string"  
],  
"value":"string",  
"clientId":"string"  
}  
]  

```