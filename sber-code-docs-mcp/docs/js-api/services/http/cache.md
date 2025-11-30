# Кэширование http-вызовов
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Кэширование http-ответов осуществляется, если в `$http.query` передан флаг `cachingRequired` со значением `true`. При этом обязательна предварительная инициализация параметра кэша `cacheTimeToLiveInSeconds` через вызов `$http.config`.
В качестве композитного ключа кэша используются следующие параметры http-вызовы:
  * `method`;
  * `url`;
  * `headers`;
  * `query`;
  * `body`;
  * `form`;
  * `dataType`.

Параметр `cacheTimeToLiveInSeconds` определяет время, в течение которого повторные запросы `cachingRequired: true` с одним и тем же ключом будут возвращать результат из кэша, вместо совершения реальных http-вызовов.
Результаты вызовов, завершившихся с ошибкой (с http-кодом ответа не принадлежащим интервалу [200;300) ), не кэшируются.
  

#### Примеры значений
Запросы с одинаковыми по структуре `body`. Результат второго вызова будет взят из кэша.
```
theme: /  
  
    init:  
        $http.config({  
            cacheTimeToLiveInSeconds: 2  
        });  
  
    state:  
        q!: *  
        script:  
            var object1 = {  
                key1:'value1',  
                key2:'value2',  
                a: { a: 'a', b: 'b' },  
                c: null,  
                b: [3, 1, 2]  
            };  
  
            var object2 = {  
                b: [3,1,2],  
                key2:'value2',  
                key1:'value1',  
                a: {b: 'b', f: function () {}, a: 'a'},  
                c: null  
            };  
  
            $http.get('http://localhost:9000/get-from-cache', {  
                cachingRequired: true,  
                body: object1  
            });  
  
            $http.get('http://localhost:9000/get-from-cache', {  
                cachingRequired: true,  
                body: object2  
            });  
});  

```

```
$temp.m= $http.get('https://www.random.org/strings/?num=1&len=10&digits=on&unique=on&format=plain&rnd=new',{  
cachingRequired:true,  
});  

```