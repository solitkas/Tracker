# Tracker
Небольшое консольное приложения для мониторинга свободного времени и несколько скриптов для аналитики полученных данных.

## Установка
Для работы необходим [Python3](https://www.python.org), модуль `matplotlib` для графиков и модуль `PIL` и `numpy` для генерации кружочка времени

```
pip3 install -r requirements.txt
```
  
## Использование
Трекер управляется вручную, после каждого этапа устанавливается следующий. Временная метка нового этапа появляется сразу после завершения предыдущего этапа, таким образом невозможно сделать пробел во времени начала одного события и конца другого. 

![main app](images/main.png)

Также доступно изменение и удаление последних этапов, добавление пояснительных подписей. 

При изменении времени предыдущего этапа можно пользоваться константами для часа, минуты и секунды, синтаксис общего выражения такой же как и для обычного калькулятора. 

![change time](images/change_time.png)

При завершении сессии программа выведет простую статистику всего сохранения. 

![stats](images/stats.png)

Само сохранение находится в файле `save.py`, все данные в котором поддаются редактированию. Последние две ячейки каждого массива нужны для более лёгкого поиска нужных точек и их редактирования, в скрипте временные метки отчитываются в формате unix-time. (Для изменения активности меняйте её unix-time метку в сохранении)

![save](images/save.png)

## Аналитика
Попимо простой аналитики после завершения сессии трекера, можно запустить скрипты, генерирующие графики на основе файла сохранения. Оба скрипта одинаковые, просто формат графиков разный. 

`bar.py`  
![bar](images/bar.png)

`barh.py`  
![barh](images/barh.png)

Также на основе данных можно сгенерировать изображение - кружочек времени. На изображении точками отмечены даты начала этапов. Сам круг представляет 24 часовой циферблат, вверху полночь.

![circles](images/circles.png)

## Настройки
В файле `constants.py` содержатся константы для всех скриптов, настройки предлгаемых этапов для трекера, параметры генерации графиков и кружочка времени. Если вы хотите расширить или заменить этапы на свои собственные, то следует изменить словарь `ACTIVITIES`, добавив названия новых активностей и их цвета (цвета будут использованы для рисования графиков и кружочка). Также если данных слишком много, то окна графиков могут занимать больше одного экрана, для того, чтобы ограничить размер окна графиков, можно установить переменную `FULL` на противоположное значение. 
