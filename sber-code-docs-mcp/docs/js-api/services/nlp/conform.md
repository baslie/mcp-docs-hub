# function conform(word, number)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
Согласование слова с числительным.
Согласование выполняется с помощью [библиотеки PyMorphy ](https://pymorphy2.readthedocs.io/en/latest/user/guide.html#id8).
  

##### Примеры значений
```
# будет выведено 5 яблок  
a: Русский текст может быть согласован с числительным: 5 {{ $nlp.conform("яблоко", 5) }}  

```

```
script:  
         $session.points = $nlp.conform("правильный", $session.myPoints) + " " + $nlp.conform("ответ", $session.myPoints);  
a: У тебя {{$session.myPoints}} {{$session.points}}.  

```