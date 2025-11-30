# $mail
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Сервис используется для отправки e-mail сообщений из сценария смартапа.
Встроенный сервис `$mail` включает методы:
  * [`debug`](./debug.md);
  * [`send`](./send.md);
  * [`sendMessage`](./send-message.md).

Конфигурация SMTP-сервера задается в секции `injector` файла `chatbot.yaml`:
```
injector:  
smtp:  
host:# хост SMTP-сервера  
port:25000# порт SMTP-сервера  
from: example@sberdevices.ru # отправитель  
user: user # пользователь SMTP-сервера  
password: password # пароль SMTP-сервера  
hiddenCopy:["myaddres@sberdevices.ru"]# необязательный массив адресов, для отправки скрытой копии  

```

Доступные порты:
  * 80
  * 443
  * 465
  * 587
  * 2443
  * 6443
  * 8080
  * 8443
  * 9443

Также можно выполнить конфигурацию, используя функцию:
```
$mail.config(smtpHost, smtpPort, user, password,from, hiddenCopy)  

```