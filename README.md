# drf_music_table

# Тестовое на python backend developer
```
Используемые технологии:
* python
* django
* drf
* redoc
* swagger
* docker
```
```
Соберите с помощью Django Rest Framework каталог исполнителей и их альбомов с песнями такой структуры:
Одна и та же песня может быть включена в несколько альбомов, но под разными порядковыми номерами.
-Исполнитель
--Название
-Альбом
--Исполнитель
-Год выпуска
-Песня
--Название
--Порядковый номер в альбоме

Как я это понял и сделал схему
```
![Image alt](https://github.com/OlegZhigulin/drf_music_table/blob/main/photo_2023-02-20_21-21-46.jpg)

```
В качестве площадки для демонстрации АПИ подключен Swagger или Redoc, чтобы можно было проверить работу АПИ через Postman
```
# Плюсом я сделал админку

# Инструкции по запуску и докер
## git clone git@github.com:OlegZhigulin/drf_music_table.git
## docker-compose up --build 
