# Подготовка проекта Code для Brain
Обновлено 1 февраля 2024
[ ![](https://developers.sber.ru/docs/img/badges/Brain.png)Brain ](https://developers.sber.ru/docs/ru/va/code/nlp/overview)[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
[](https://public.oprosso.sberbank.ru/p/docs_csi_2025)
NLU-ядро Brain — подключаемая функция платформы. Если для аккаунта включено использование NLU-ядра, в настройках проекта отображаются дополнительные параметры конфигурации.
  1. В SmartApp Studio создайте проект [Code](https://developers.sber.ru/docs/ru/va/chat/script/project-creation#sozdanie-proekta-code) на основе шаблона [**Проект для SmartApp Brain**](../../templates/smartapp-templates.md#proekt-dlya-smart-app-brain).
  2. Убедитесь, что в конфигурационном файле `chatbot.yaml` заданы [параметры для работы со SmartApp Brain](https://developers.sber.ru/docs/ru/va/chat/voice-interface/command-recognition/nlu_core):
```
# Название проекта. По умолчанию brain  
name: pizza-order  
# Основной сценарий, с которого начинается работа смартапа  
entryPoint:  
- main.sc  
botEngine: v2  
language: ru  
# Порог срабатывания классификатора. Рекомендуется настраивать в зависимости от выбранного алгоритма   
caila:  
noMatchThreshold:0.2  

```

  3. Убедитесь, что в основном сценарии `main.sc` подключен модуль слот-филлинга и сценарий опроса пользователя `order.sc`.
  4. В папке `src/themes` создайте файл сценария `order.sc`, который будет отвечать за [прием заказа](./loan-script.md).

Здесь мы подключаем [модуль слот-филлинга](../slot-filling/overview.md) и файл со сценарием дозапроса `order.sc`.
Далее приступайте к созданию [входного сценария смартапа `main.sc`](./input-script.md).