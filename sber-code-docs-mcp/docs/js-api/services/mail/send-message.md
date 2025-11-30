# function sendMessage(address, subject, body)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Отправляет сообщение на указанный адрес с указанной темой и телом сообщения.
Параметры:
  * `address` — адрес электронной почты;
  * `subject` — тема письма;
  * `body` — тело сообщения.

Возвращает объект вида:
```
{"status":"OK"}  

```

Возможные значения поля `status`:
  * `OK` — письмо успешно отправлено;
  * `UNABLE_TO_CONNECT` — ошибка подключения;
  * `INCORRECT_ADDRESS` — указанный адрес не существует.

## Примеры значений
```
state:  
        q!: *  
        script:  
            $mail.sendMessage("coco@coco.com", "message subject", "message body");  
            $reactions.answer("Отправил почту", $context);  

```

Запрос на отправку письма отправляется с заголовком `contentType: "text/html"`. В тексте письма (содержание `body`) можно использовать html-теги.
Обратите внимание: отображение письма с форматированием html также зависит от почтового клиента, в котором будет открыто письмо и от того, какие теги он поддерживает.