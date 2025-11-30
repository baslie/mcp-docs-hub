# function stopSession()
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Метод `$jsapi.stopSession()` завершает сессию.
Данные в [`$session`](../../variables/session.md) очищаются сразу при вызове метода. Текущий вопрос пользователя и ответ ассистента попадают в предыдущую сессию. Последующие запросы записываются в новую сессию.
Метод [не закрывает окно смартапа](https://developers.sber.ru/docs/ru/va/chat/script/start-stop/close-app).
## Примеры значений
```
theme: /  
  
    state: Приветствие  
        q!: * *start  
        q!: (привет|hello) *  
        script:  
            $jsapi.startSession();  
        a: Здравствуйте! Чем я могу Вам помочь?  
  
    state: Прощание  
        q!: (пока|до свидания|bye) *  
        script:  
            $jsapi.stopSession();  
        random:  
            a: Всего доброго.  
            a: До свидания!  

```