# function buttons(arg)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/ChatApp.png)Chat App ](https://developers.sber.ru/docs/ru/va/chat/title-page)
Функция позволяет добавлять в ответ кнопки. Функция принимает объект, который состоит из следующих параметров:
  * `text` — название кнопки;
  * `transition`, `url` — путь перехода при клике на кнопку.

  

##### Примеры значений
```
script: $reactions.buttons('Одна кнопка');  
$reactions.buttons(['Одна кнопка','И другая в том же ряду']);  
$reactions.buttons({button:{text:'Отправить контактные данные',request_contact:true}});  
$reactions.buttons({text:'Кнопка с переходом',transition:'/state'});  
$reactions.buttons([{text:'Кнопка 1'},{text:'Кнопка 2',request_contact:true}]);  

```