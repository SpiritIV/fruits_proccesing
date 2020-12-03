# fruits_proccesing

###### В рамках данного проекта мной был выбран dataset с Kaggle (https://www.kaggle.com/moltean/fruits), итогом которого является интерфейс по загрузке изображения одного из перечисленных фруктов в виде изображения и демонстрации результата в виде вероятности загрузки того или иного фрукта пользователем.

Список фруктов: 
# python-flask-docker
Итоговый проект курса "Машинное обучение в бизнесе"

Стек:

ML: sklearn, pandas, numpy, opencv
API: flask
Данные: с kaggle - https://www.kaggle.com/moltean/fruits

Задача: определение фрукта по загруженному изображению (апельсин, банан, клубника, киви, лемон, кокос, ананас, персик).

### Запускаем контейнер
```
$ docker run -d -p 8180:8180 -p 8181:8181 fimochka/gb_docker_flask_example
```

### Переходим на localhost:8181
