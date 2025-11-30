# $fetch.get(url, settings)
Обновлено 15 декабря 2023
[ ![](https://developers.sber.ru/docs/img/badges/Code.png)Code ](https://developers.sber.ru/docs/ru/va/code/overview)
[](https://public.oprosso.sberbank.ru/p/docs_csi_2025)
Возвращает данные с внешнего сервера.
Эквивалентен вызову `$fetch.query(url, settings)`, при условии, что `settings.method == 'GET'`.
Параметры:
  * `url` — адрес сервера в виде строки, может содержать параметры, которые будут заполнены из поля `query`, переданного в параметре `settings`.
  * `settings` — валидный JSON с параметрами запроса.

## Примеры
```
patterns:  
    $city =(москв*:moscow/питер*:saint_petersburg)||converter=function($pt){return $pt.value.replace("_","%20");}  
  
state:Weather  
    q!: Сколько градусов в $city  
script:  
var q = $parseTree.value;  
var url ="https://api.apixu.com/v1/current.json?key="+ $injector.wheatherApiKey+"&q="+ q;  
var response = $fetch.get(url);  
if(response.isOk){  
            $temp.degree= response.data.current.temp_c;  
}  
a: Сейчас {{ $temp.degree}}°C.  

```