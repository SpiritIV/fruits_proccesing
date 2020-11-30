# fruits_proccesing

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
