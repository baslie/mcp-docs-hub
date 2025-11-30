# Слот-филлинг в Code и Brain
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
Слот-филлинг (англ. slot filling) — процесс дозапроса данных для выполнения запроса пользователя. Полученные при дозапросе данные доступны в сценарии.
Слоты (англ. slots) — данные, которые клиент передает с запросом или в процессе дозапроса. У каждого слота есть обязательные атрибуты: `Имя`, `Тип`.
Модуль слот-филлинга подключается в [файле основного сценария](../../project/sc.md) с помощью тега [`require`](../../sa-dsl/tags/declarative-tags.md#require2):
```
require: slotfilling/slotFilling.sc  
  module = sys.zb-common  

```