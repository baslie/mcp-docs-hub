# function checkMyVocabulary(word)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
[](https://public.oprosso.sberbank.ru/p/docs_csi_2025)
Проверяет, является ли переданный текст словарным словом.
Для проверки используется словарь, указанный в `chatbot.yaml` в параметре `nlp.vocabulary`. Словарь может быть создан в лингвистическом сервисе действием `vocabulary-from-text`.
Возвращает:
  * `false` — если слово не находится в словаре;
  * `true` — если слово является словарным.

  

##### Примеры значений
```
state:  
    q!: *  
    script:  
        var text = $parseTree.text;  
        $temp.res = $nlp.checkMyVocabulary(text);  
    if: $temp.res  
        a: есть в словаре  
    else:  
        a: нет в словаре  

```