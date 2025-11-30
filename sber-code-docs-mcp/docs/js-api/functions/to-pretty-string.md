# function toPrettyString(obj)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Преобразует переданный объект в форматированный JSON-объект с отступами.
Тип возвращаемого значения: `string`.
  

##### Примеры значений
Можно использовать при логировании:
```
var customer ={  
firstName:'John',  
lastName:'Doe',  
id:5566,  
cart:[  
{itemName:'Удочка',price:432},  
{itemName:'Леска',price:34},  
],  
};  

```

Сравните примеры логирования объектов с использованием `toPrettyString` и без:
  * `log(customer)`

```
log(customer):  
{"firstName":"John","lastName":"Doe","id":5566,"cart":[{"itemName":"Удочка","price":432},{"itemName":"Леска","price":34}]}  

```

  * `log(“Customer info:\n” + customer)`

```
[object Object]  

```

  * `log(toPrettyString(customer))`

```
{  
"firstName":"John",  
"lastName":"Doe",  
"id":5566,  
"cart":[  
{  
"itemName":"Удочка",  
"price":432  
},  
{  
"itemName":"Леска",  
"price":34  
}  
]  
}  

```

  * `log(“Customer info:\n” + toPrettyString(customer))`

```
Customer info:  
{  
"firstName":"John",  
"lastName":"Doe",  
"id":5566,  
"cart":[  
{  
"itemName":"Удочка",  
"price":432  
},  
{  
"itemName":"Леска",  
"price":34  
}  
]  
}  

```