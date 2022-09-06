# Проект «Продуктовый помощник» - Foodgram
Foodgram - Продуктовый помощник. Это онлайн-сервис, где пользователи смогут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

**
### Как запустить проект:

Установите Docker и Docker-compose на ВМ:

sudo apt install docker.io
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose


Проверьте корректность установки Docker-compose:

sudo  docker-compose --version


После успешного деплоя:
Соберите статические файлы (статику):

docker-compose exec web python manage.py collectstatic --no-input

Примените миграции:

docker-compose exec web python manage.py makemigrations
docker-compose exec web python manage.py migrate --noinput

Создайте суперпользователя:

docker-compose exec web python manage.py createsuperuser

***
### Используемые технологии:

Ubuntu
Python
Django
Django REST Framework
PostgreSQL
Yandex.Cloud
JWT
Nginx
gunicorn
Docker
Docker-compose
Docker Hub
GitHub Actions



***
### Автор:
- Виктория Страшнова [strashnovavictoria](https://github.com/strashnovavictoria)



### Развёрнутый проект:

https://foodgram-sva.servehttp.com/ http://51.250.100.90/admin/ 


[![Django-app workflow](https://github.com/strashnovavictoria/foodgram-project-react/actions/workflows/main.yml/badge.svg)](https://github.com/strashnovavictoria/foodgram-project-react/actions/workflows/main.yml)