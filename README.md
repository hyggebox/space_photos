# Фото на космическую тематику

Скрипт скачивает последние доступные фото на космическую тематику:
  - Запусков SpaceX
  - [APOD](https://apod.nasa.gov/apod/astropix.html) (Astronomy Picture of the Day)
  - [EPIC](https://epic.gsfc.nasa.gov/) (Earth Polychromatic Imaging Camera)

## Установка и запуск

- Для работы скрипта необходим токен. Чтобы его получить, нужно зарегистрироваться 
на сайте [api.nasa.gov](https://api.nasa.gov/).


- Скачайте файлы. Токен должен лежать в файле .env:

```
NASA_API_KEY=<ваш_токен>
```

- Python3 должен быть уже установлен. Используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirements.txt
```

- Запустите сайт командой `python` (или `python3`, если есть конфликт с Python2):

```
python main.py
```


- Скрипт загрузит фото в папку `/images`



## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).