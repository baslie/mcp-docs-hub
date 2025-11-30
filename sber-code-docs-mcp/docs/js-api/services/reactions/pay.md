# function pay(arg)
Обновлено 15 декабря 2023
Чтобы ассистент запустил сценарий оплаты, в блоке **JS Код** вызовите функцию `$reactions.pay()` и передайте в параметрах идентификатор счета `invoice_id`:
```
$reactions.pay($session.invoice_id);  

```

Функцию можно вызвать как в текущем блоке **JS Код** , так и в новом, расположенном в сценарии после блока, который добавляет товар.
По результатам оплаты в сценарий приходит событие [`PAY_DIALOG_FINISHED`](https://developers.sber.ru/docs/ru/va/about/monetization/payments/processing/smartapp-api#format-rezultata-oplaty), которое необходимо обработать для возврата в сценарий оплаты.