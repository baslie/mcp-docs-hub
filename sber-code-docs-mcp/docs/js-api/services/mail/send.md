# function send(mailRequest)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Более гибкий метод отправки сообщения, чем `sendMessage(address, subject, body)`. Метод не требует конфигурирования — все параметры передаются в `mailRequest` в следующем виде:
```
{  
    from:"test@test.com",  
    hiddenCopy:["hidden@test.com"],  
    to:["recipient@test.com"],  
    subject:"any subject",  
    content:"any body",  
    smtpHost:"...",  
    smtpPort:"...",  
    user:"...",  
    password:"..."  
}  

```

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
            $mail.send({  
                from: "asd@asd.com",  
                hiddenCopy: [],  
                to: ["recipient@cscs.com"],  
                subject: "Subject",  
                content: "Message",  
                smtpHost: "localhost",  
                smtpPort: "25000",  
                user: "user",  
                password: "password"  
            });  

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