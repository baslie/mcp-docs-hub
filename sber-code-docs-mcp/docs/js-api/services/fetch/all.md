# $fetch.all(iterable)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Возвращает промис, который выполнится тогда, когда будут выполнены все промисы, переданные в виде перечисляемого аргумента, или отклонен любой из переданных промисов.
В параметр передается перечисляемый объект, например массив.
## Пример
```
var first = $fetch.post('http://example1.ru')  
.then(function(response){  
if(response.status!=200){  
throw"example1 failed: "+ response.status;  
}  
  $jsapi.log('first then');  
return response.json();  
});  
  
var second = $fetch.post('http://example2.ru')  
.then(function(response){  
if(response.status!=200){  
throw"example2 failed: "+ response.status;  
}  
  $jsapi.log('second then');  
return response.json();  
});  
  
$fetch.all([first, second])  
.then(function(jsons){  
    $jsapi.log("success");  
})  
.catch(function(error){  
  $jsapi.log(error);  
})  
  
$jsapi.log('scenario');  

```

Последовательность вывода в консоль при выполнении кода:
```
scenario  
second then  
first then  
success  

```