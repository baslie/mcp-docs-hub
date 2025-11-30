# Переменные JavaScript в Code
Обновлено 10 апреля 2024
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
При вызове скриптовых расширений, задаваемых в тегах `if:`, `else:`, `elseif:`, `script:` и макроподстановках в ответах `{{}}` (тег `a:`), передаются следующие переменные:
  * [`$context`](./context.md);
  * [`$parseTree`](./parse-tree.md);
  * [`$client`](./client.md);
  * [`$session`](./session.md);
  * [`$request`](./request.md);
  * [`$response`](./response.md);
  * [`$temp`](./temp.md);
  * [`$injector`](./injector.md).

Скрипт может быть задан:
  * Непосредственно в стейте.

```
    state: Hello  
        q!: * меня зовут $Name *  
        script:  
            $session.name = $Name  
        a: Привет, {{$session.name}}!  

```

  * Вызовом функции. В таком случае объявляем скрипт в JS-файле и вызываем его в стейте после тега `script`.

Например, объявляем скрипт в JS-файле:
```
functiongetName(){  
var $session = $jsapi.context().session;  
    $session.name= $Name;  
}  

```

Вызываем скрипт в стейте:
```
    state: Hello  
        q!: * меня зовут $Name *  
        script: getName()  
        a: Привет, {{$session.name}}!  

```

Следует отметить, что в JS-файлах ко всем переменным можно обратиться, убрав знак `$` и добавив в начало `$jsapi.context()`.
Например, в JS-файле `$session`, будет иметь вид: `$jsapi.context().session`.
Объявление переменных: `var $session = $jsapi.context().session`.