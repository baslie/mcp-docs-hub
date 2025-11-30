# Прерывание слот-филлинга в Code и Brain
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)
Условия прерывания слот-филлинга задаются в файле [`chatbot.yaml`](../../project/configuration-file.md) в разделе [`injector`](../../project/configuration-file.md#sektsiya-injector2):
```
injector:  
slotfilling:  
maxSlotRetries:1  
stopOnAnyIntent:true  
stopOnAnyIntentThreshold:0.2  

```

Где:
  * `maxSlotRetries` — количество попыток для одного слота. Если пользователь ответил указанное количество раз и слот не был заполнен, процесс слот-филлинга прерывается. Последняя фраза пользователя обрабатывается в сценарии смартапа.
  * `stopOnAnyIntent` — параметр прерывания слот-филлинга по интенту. Принимает значения `true` или `false`.
  * `stopOnAnyIntentThreshold` — параметр соответствия, задающий минимально необходимую схожесть фразы с одним из классов. Является параметром прерывания слот-филлинга по интенту.

## Прерывание по интенту
Если `stopOnAnyIntent: true` и запросу клиента соответствует интент с параметром `confidence` выше, чем `stopOnAnyIntentThreshold`, слот-филлинг прерывается по интенту.
Параметр `confidence` — степень уверенности Code в том, что введенная фраза относится к определенному интенту.
Нужно учитывать контекст начала слот-филлинга. Например, если при прерывании в стейт с соответствующим интентом невозможно попасть (например, тег [`intent`](../../sa-dsl/tags/intents-tags.md) не глобальный), то запрос попадет в тег [`event!`](../../sa-dsl/tags/declarative-tags.md#event2) согласно правилу `noMatch`.
Если параметры для прерывания в конфигурационном файле `chatbot.yaml` не указаны, слот-филлинг прерывается согласно параметрам по умолчанию:
```
injector:  
slotfilling:  
maxSlotRetries:2  
stopOnAnyIntent:false  
stopOnAnyIntentThreshold:0.2  

```