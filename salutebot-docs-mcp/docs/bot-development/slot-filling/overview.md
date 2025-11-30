---
title: Слот-филлинг
source_url: https://developers.sber.ru/docs/ru/salutebot/bot-development/slot-filling/overview
tags: [Code]
---

# Слот-филлинг

Слот-филлинг (англ. slot filling) — процесс дозапроса данных для выполнения запроса пользователя. Полученные при дозапросе данные доступны в сценарии.
Слоты (англ. slots) — данные, которые клиент передает с запросом или в процессе дозапроса. У каждого слота есть обязательные атрибуты: `Имя`, `Тип`.
Модуль слот-филлинга подключается в [файле основного сценария](https://developers.sber.ru/docs/ru/va/code/project/sc) с помощью тега [`require`](https://developers.sber.ru/docs/ru/va/code/sa-dsl/tags/declarative-tags#require2):
```
require: slotfilling/slotFilling.sc  
  module = sys.zb-common  

```