# $fetch.delete(url, settings)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Удаляет данные на внешнем сервере.
Эквивалентен вызову `$fetch.query(url, settings)`, при условии, что `settings.method == 'DELETE'`.