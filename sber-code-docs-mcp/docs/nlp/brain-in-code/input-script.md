# Входной сценарий для Brain в Code
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
В файл `main.sc` добавьте следующий сценарий:
```
require: requirements.sc  
  
theme: /  
    state: Start  
        q!: $regex</start>  
        if: !$client.name  
            a: Здравствуйте! Как я могу к вам обращаться?  
            go!: /Start/GetName  
        else:  
            a: Здравствуйте! Чем могу помочь?  
  
        state: GetName  
            state:  
                q: * @pymorphy.name *  
                script: $client.name = $parseTree.value  
                a: Чем могу помочь, {{ $client.name }}?  
  
            state:  
                event: noMatch  
                a: Чем могу помочь?  
  
    state:  
       event!: noMatch  
       a: Пожалуйста, уточните запрос.  

```

Здесь:
  * Подключаем модули и зависимости:

```
require: requirements.sc  

```

  * Старт сценария. При отсутствии имени клиента смартап переходит к стейту `GetName`.

```
    state: Start  
        q!: $regex</start>  
        if: !$client.name  
            a: Здравствуйте! Как я могу к вам обращаться?  
            go!: /Start/GetName  
        else:  
            a: Здравствуйте! Чем могу помочь?  

```

  * Получение данных о клиенте. В данном стейте смартап распознает имя клиента при помощи [системной сущности](../entities/overview.md) `@pymorphy.name`. Для сущности, указанной в паттерне, автоматически создается слот и она попадает в дерево разбора `parseTree`.

Перейдите к разделу `Сущности` > `Системные`. [Активируйте распознавание сущности](https://developers.sber.ru/docs/ru/va/chat/voice-interface/command-recognition/entities/entities-types#sistemnye-sushnosti3) `@pymorphy.name`.
```
        state: GetName  
            state:  
                q: * @pymorphy.name *  
                script: $client.name = $parseTree.value  
                a: Чем могу помочь, {{ $client.name }}?  

```

  * В данном стейте мы обрабатываем кейсы, когда сущность не была распознана или клиент отказался называть имя.

```
            state:  
                event: noMatch  
                a: Чем могу помочь?  

```

  * Обработка непредусмотренных сценарием запросов клиента.

Обратите внимание, что при использовании NLU-ядра Brain для непредусмотренных сценарием запросов клиента применяется `event: noMatch`.
```
    state:  
       event!: noMatch  
       a: Пожалуйста, уточните запрос.  

```

Далее приступайте к созданию [заполнению сущностей](./entities.md).