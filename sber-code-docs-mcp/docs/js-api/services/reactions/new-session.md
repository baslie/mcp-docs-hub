# function newSession(arg)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Метод предназначен для явного создания новой сессии из скрипта.
  

##### Примеры значений
```
script:if(!$context.testContext&&!$request.data.newSession){  
if($parseTree){  
        $reactions.newSession({message: $parseTree.text,data:{newSession:true}});  
}else{  
        $reactions.newSession({message:'/start',data:{newSession:true}});  
}  
}  

```

```
state: reset  
        q!: reset  
        script:  
            $reactions.newSession({message: "/start", data: $request.data});  

```

[Подробнее о сессиях в платформе Code](../../session-lifetime-control.md)