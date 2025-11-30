---
title: Использование протоколов шифрования
source_url: https://developers.sber.ru/docs/ru/salutebot/bot-development/protocols
tags: [Graph, Code]
---

# Использование протоколов шифрования

Сервис поддерживают наборы алгоритмов (cipher suits) и версию сетевого протокола TLSv1.2, отвечающие требованиям стандартов безопасности.
Протокол позволяет обнаруживать следующие риски безопасности:
  * Незаконное изменение сообщений.
  * Перехват сообщений.
  * Подделка сообщений.

Добавьте ssl_ciphers в блок сервера в файле ssl.conf:
```
EECDH+ECDSA+AESGCM  
EECDH+aRSA+AESGCM  
EECDH+ECDSA+SHA384  
EECDH+ECDSA+SHA256  
EECDH+aRSA+SHA384  
EECDH+aRSA+SHA256  
EECDH+aRSA+RC4  
EECDHEDH+aRSA HIGH  

```

Исключения: `!RC4 !aNULL !eNULL !LOW !3DES !MD5 !EXP !PSK !SRP !DS`.
Шифрование на уровне данных
```
AES encrypt-algorithm:  
'AES/CBC/PKCS5Padding' key-algorithm:'AES'  
PBKDF2WithHmacSHA256  

```