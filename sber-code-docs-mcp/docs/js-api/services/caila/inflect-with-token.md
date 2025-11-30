# function inflect(text, tag declension, token)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
Склоняет текст в требуемый формат. Метод используется для обращения к стороннему обученному классификатору при помощи API-ключа.
  

#### Синтаксис
Метод принимает в качестве аргумента текст для разметки и API-токен в виде строк `string`, тег склонения `tag`:
```
$caila.inflect("text",["tag"],"token")  

```

[Подробнее о получении API-ключа](../../../nlp/api/overview.md#section/Autentifikaciya)
[Возможные значения `tag declension`](./inflect.md#padezh2)
В качестве ответа передается строка с фразой в требуемом падеже.
  

#### Использование в сценарии
```
    state:  
        q!: inflectWithToken  
        script:  
            $reactions.answer($caila.inflectWithToken("Мария дала книгу", ["voct"], "token"))  

```