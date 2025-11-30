# function tokenize(text)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
Разбивает текст на слова (токены). Возвращает массив строк.
Поддерживаемые типы токенизаторов:
  * regexp — простой токенизатор на регулярных выражениях.
  * srx — конфигурируемый токенизатор на базе настраиваемых правил сегментации. При указании данного токенизатора требуется указать файл грамматики в параметре `srxPath`.
  * default — способ сегментации по умолчанию. Является предпочтительной опцией при совместном использовании паттернов и классификатора.

Тип токенизатора и его параметры указываются в файле `chatbot.yaml`:
```
nlp:  
tokenizer: default  
morphology: pyMorphy  
costStrategy: weighted  
contextHistoryDepth:1  
nbest:1  
vocabulary: sys/dictionaries/opencorpora/opcorpora-vocab.json  
synonyms: sys/dictionaries/opencorpora/weighted-synonyms-pmiIdf.json  

```

## Примеры значений
```
 state: TestTokenize  
        q!: tokenize  
        script:  
            $temp.m = $nlp.tokenize("Добрый день, помогите с заказом. Спасибо. С наступающим.");  
        a: morph: {{$temp.m[0]}}  

```