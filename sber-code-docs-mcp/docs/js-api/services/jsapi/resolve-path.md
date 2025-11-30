# function resolvePath(basePath, relativePath)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
Метод предназначен для приведения относительных путей состояний к абсолютным.
  

##### Примеры значений
```
\$jsapi.resolvePath($context.currentState,`..`)- на уровень выше  
\$jsapi.resolvePath('/state1',`./state2/state3`)==`/state1/state2/state3/`  
\$jsapi.resolvePath('/state1',`/root`)==`/root`  
\$jsapi.resolvePath('/state1',`state2`)==`/state1/state2`  
\$jsapi.resolvePath('/state1',`./unused/..`)==`/state1`  

```