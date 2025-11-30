# function checkPayment()
Обновлено 11 апреля 2025
Для получения статуса платежа используется встроенная функция `$payment.checkPayment`, которая вызывает метод [`GET ​/invoices​/{invoice_id}`](https://developers.sber.ru/docs/ru/va/about/monetization/payments/reference/get-invoice). Входным параметром для функции `$payment.checkPayment` является `invoice_id`.
Сохраните ответ с результатом статуса оплаты в отдельную переменную:
```
script:var response = $payment.checkPayment($session.invoice_id);  
$session.invoice_status= response.invoice_status;  
$reactions.answer($session.invoice_status);  

```

В приведенном примере переменная `response` содержит весь ответ на запрос [`GET ​/invoices​/{invoice_id}`](https://developers.sber.ru/docs/ru/va/about/monetization/payments/reference/get-invoice) со статусом платежа `invoice_status` и ошибкой `error`.
  

**Параметры ответа**
Параметр | Описание  
---|---  
Code | Код ответа  
Error | Блок с описанием ошибки или ответа  
user_message | Описание кода ошибки или ответа  
error_description | Техническое описание кода ошибки или ответа  
error_code | Код ответа  
invoice_id | Идентификатор счета, по которому был направлен запрос  
invoice_date | Дата и время создания счета  
invoice_status | Текущий статус счета. Возможные значения смотрите в разделе [Статусы платежа](https://developers.sber.ru/docs/ru/va/about/monetization/payments/statuses)  
invoice | Блок с информацией по заказу. Передается только при коде ответа 200  
payment_info | Блок с информацией о платеже  
payment_id | Идентификатор проведенной оплаты  
  
card_id | Токен карты, с которой была проведена оплата. Параметр возвращается, если использовалась сохраненная карта  
name | Имя владельца карты, с которой была проведена оплата. Параметр возвращается, если использовалась сохраненная карта  
masked_pan | Маскированный номер карты, с которой была проведена оплата  
expiry_date | Срок действия карты, с которой была проведена оплата  
cardholder | Имя владельца карты, с которой была проведена оплата  
payment_system | Платежная система, в которой зарегистрирована карта  
payment_system_image. | Ссылка на логотип платежной системы  
image | Ссылка на логотип карты в интерфейсе платежного устройства  
paysys | Название платежного сервиса, через который был проведен платеж  
paysys_image | Ссылка на логотип платежного сервиса  
  
bank_info | Блок информации о банке плательщика  
bank_name | Название банка, выпустившего карту  
bank_country_code | Код страны банка, выпустившего карту  
bank_country_name | Название страны банка, выпустившего карту  
bank_image | Ссылка на логотип банка, выпустившего карту