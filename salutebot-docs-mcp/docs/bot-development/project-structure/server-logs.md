---
title: Логи сервера
source_url: https://developers.sber.ru/docs/ru/salutebot/bot-development/project-structure/server-logs
tags: [Code]
---

# Логи сервера

В логи сервера автоматически попадают сообщения, которые принимает и передает чат-бот, запущенный в канале распространения или в [тестовом виджете](../../testing/testing-debugging.md).
## Просмотр логов
Чтобы открыть панель с логами, нажмите кнопку **Логи** в левом нижнем углу рабочей области Code.
Логи сервера доступны на любой вкладке, внутри вкладки **Разработка**.
![Логи сервера в редакторе сценариев](https://developers.sber.ru/docs/assets/images/server-logs-2d13e0fe79bf7865ac2dd8c2a0c2ff47.png)
Используйте функцию [`log(message)`](https://developers.sber.ru/docs/ru/va/code/js-api/functions/log-message), чтобы выводить в логи произвольные сообщения. Произвольные сообщения помогают при отладке скриптов, встроенных в файлы сценариев.
## Фильтрация и очистка логов
Используйте фильтр **Все логгеры** , чтобы отфильтровать логи по источнику.
Используйте фильтр **Все события** , чтобы отфильтровать логи по уровню детализации (от `info` до `critical`).
Чтобы очистить префиксы записей, нажмите кнопку 
![Очищать префиксы](https://developers.sber.ru/docs/ru/salutebot/bot-development/project-structure/server-logs)
.
Чтобы полностью очистить окно вывода логов, нажмите кнопку 
![Очистить](https://developers.sber.ru/docs/ru/salutebot/bot-development/project-structure/server-logs)
.