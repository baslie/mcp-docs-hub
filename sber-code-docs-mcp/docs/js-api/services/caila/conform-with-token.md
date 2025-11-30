# function conformWithToken(text, number, token)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
Согласует слова с числительными. Метод используется для обращения к стороннему обученному классификатору при помощи API-ключа.
  

#### Синтаксис
Метод принимает в качестве аргумента текст и API-ключ к стороннему обученному классификатору в виде строк `string`, а также число для согласования `number`:
```
$caila.conform("text", number, "token")  

```

[Подробнее о получении API-ключа](../../../nlp/api/overview.md#section/Autentifikaciya)
В качестве ответа передается строка с согласованной фразой.
  

#### Использование в сценарии
Запрос на согласование фразы:
```
    state:  
        q!: conformWithToken  
        script:  
            $reactions.answer($caila.conform("хороший день", 2, "token"))  

```

Ответ: `хороших дня`.