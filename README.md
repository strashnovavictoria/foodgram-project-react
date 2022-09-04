# Проект «Продуктовый помощник» - Foodgram
Foodgram - Продуктовый помощник. Это онлайн-сервис, где пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

**
### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/bokhonin/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
***
### Используемые технологии:
Ubuntu 20.04 LTS
Python 3.7
Django 2.2.16
Docker 4.11.0
gunicorn 20.0.4
nginx
PostgreSQL

### Получение публикаций:
Получение списка всех произведений

http://51.250.100.223/api/v1/title/
[
  {
    "count": 0,
    "next": "string",
    "previous": "string",
    "results": [
      {
        "id": 0,
        "name": "string",
        "year": 0,
        "rating": 0,
        "description": "string",
        "genre": [
          {
            "name": "string",
            "slug": "string"
          }
        ],
        "category": {
          "name": "string",
          "slug": "string"
        }
      }
    ]
  }
]

Более подробно запросы можно посмотреть по адресу <http://51.250.100.230/redoc/>
***
### Автор:
- Виктория Страшнова [strashnovavictoria](https://github.com/strashnovavictoria)

[![Django-app workflow](https://github.com/strashnovavictoria/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)](https://github.com/strashnovavictoria/yamdb_final/actions/workflows/yamdb_workflow.yml)
