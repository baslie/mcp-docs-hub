# function inflect(text, declension)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
Склоняет слово в требуемый формат.
Склонение выполняется с помощью [библиотеки PyMorphy ](https://pymorphy2.readthedocs.io/en/latest/user/grammemes.html). Склонения `declension` задаются в ее формате.
  

##### Примеры значений
В примере: `gent` — родительный падеж.
```
a: И склонен в нужную форму: Вы из {{ capitalize($nlp.inflect("питер", "gent")) }}?  

```

В примере: `loct` — предложный падеж.
```
state:  
        q!: inflect  
        a: {{ $nlp.inflect('Москва', "loct") }}  

```