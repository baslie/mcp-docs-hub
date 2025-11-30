# function conform(text, number)
Обновлено 20 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
Согласует слова с числительными.
  

#### Синтаксис
Метод принимает в качестве аргумента текст в виде строки `string` и число для согласования `number`:
```
$caila.conform("text", number)  

```

В качестве ответа передается строка с согласованной фразой.
  

#### Использование в сценарии
Запрос на согласование фразы:
```
    state:  
        q!: conform  
        script:  
            $reactions.answer($caila.conform("хороший день", 2))  

```

Ответ: `хороших дня`.