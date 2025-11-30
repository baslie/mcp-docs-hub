# function startSession()
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Метод `$jsapi.startSession()` начинает новую сессию.
При этом данные в [`$session`](../../variables/session.md) очищаются сразу при вызове метода. Текущий вопрос пользователя и ответ ассистента попадают сразу в новую сессию.
  

##### Примеры значений
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