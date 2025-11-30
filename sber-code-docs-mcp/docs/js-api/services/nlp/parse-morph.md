# function parseMorph(word)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
Производит морфологический анализ слова.
Морфологический анализ выполняется с помощью [PyMorphy ](https://pymorphy2.readthedocs.io/en/latest/user/guide.html#id3).
  

##### Примеры значений
Пример вызова:
```
  script:  
    $temp.res = $nlp.parseMorph("яблочки");  
    log($temp.res);  
  a: {{ $temp.res.normalForm }}  

```

Результат вызова:
```
log:{"score":0.5,"normalForm":"яблочко","tags":["inan","neut","NOUN","plur","nomn"]}  
answer: яблочко  

```