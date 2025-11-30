# function currentDate()
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Возвращает объект `moment.js` с текущей датой.
Обратите внимание, что функция определена в системном модуле.
[Подробнее о системных модулях](../../project/sys-modules.md)
  

##### Примеры значений
```
script:  
            if (!$client.firstEntrance) {  
                $temp.startConversation = "/Main"  
            } else {  
                var interval = currentDate().valueOf() - $session.lastActiveTime.valueOf();  
                if (interval > 86400000) {  
                    $temp.startConversation = "/Menu"  
                }  
            }  

```