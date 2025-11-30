# Препроцессы и постпроцессы в Code
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
[](https://public.oprosso.sberbank.ru/p/docs_csi_2025)
Pre/post-процессы являются обработчиками, которые вызываются перед выполнением основного цикла обработки запроса и после него.
`preProcess` может быть использован для инициализации каких-либо данных, проверки условий и выполнения переходов в другие состояния, альтернативные предложенных матчером.
`postProcess` может быть использован для добавления дополнительных данных в ответ, записи статистики и другое.
## Синтаксис
Для установки pre/post-процессов используется функция [`bind ()`](./functions/bind-type-handler-path-name.md), объявленная в теге [`init:`](../sa-dsl/tags/declarative-tags.md#init2).
Pre/post-процессы работают только внутри тега `init:`.
## Примеры значений
```
patterns:  
    $num = $regexp<\d+>  
  
theme: /myApp  
  
    init:  
        bind("preProcess", function($context) {  
            // Запускается перед выполнением каждого блока  
            if ($context.parseTree._num) {  
                $context.session.L = 2 * 3.14 * $context.parseTree._num;  
            }  
        }, "/myApp");  
        bind("postProcess", function($context) {  
            // Запускается после выполнением каждого блока  
            if ($context.session.L > 50) {  
                $reactions.transition('/myApp/bigCircle');  
                $context.session.L = 0;  
            }  
        }, "/myApp");  
  
    state: start  
        q!: *start  
        a: Задайте радиус круга, а я посчитаю длину его окружности!  
  
    state: radius  
        q!: $num  
        script:  
            $session.radius = $parseTree._num;  
            $reactions.transition('/myApp/diameter');  
  
    state: diameter  
        a: Длина окружности: {{ $session.L }}  
  
    state: bigCircle  
        a: Длина окружности больше 50  

```

Из `postProcess` также возможен переход обратно в сценарий, для этого используется конструкция `$reactions.transition`. Например:
```
theme: /  
    init:  
  
        bind("preProcess", function($context) {  
            log('preProcess!');  
            $context.temp.count = 1;  
        });  
  
        bind("postProcess", function($context) {  
            log('postProcess!');  
            var $context = $jsapi.context();  
            if ($context.temp.count == 5) {  
                return;  
            }  
            $context.temp.targetState = "/fray_test/testpostprocess";  
            if ($context.temp.count > 2) {  
                $reactions.transition("/postprocess2");  
            } else {  
                $reactions.transition("/postprocess");  
            }  
            $context.temp.count = $context.temp.count + 1  
        });  
  
    state: start  
        q!: start  
        a: this should be executed only once before postprocess  
  
    state: postprocess  
        go!: ./postprocessEnd  
  
        state: postprocessEnd  
            a: state from postprocess transition  
  
    state: postprocess2  
        a: postprocess2  
  
    state: fray_test  
        state: testpostprocess  
            a: fray_test  

```

Стейт, указанный в `$context.temp.targetState` использоваться не будет. Вместо него будет выбран стейт, указанный в `$reactions.transition`.
Если будет совершено больше пяти переходов, исполнение будет приостановлено.