![example workflow](https://github.com/amirsvc/foodgram-project-react/actions/workflows/foodgram-project-react.yml/badge.svg)

# **Проект foodgram-project-react**

Язык программирования: Python 3.9

Размещен в инете по адресу http://amirsvc.sytes.net/ (http://51.250.71.194/)

админские данные:
админка http://amirsvc.sytes.net/admin
почта:admin@ad.com
пароль: foodgramadmin

данные пользвоателя:
почта: user@us.us
пароль: foodgramuser

Используемые библиотеки и пакеты перечислены в файле requirements из папки backend

## **Описание:**

Проект — сайт Foodgram, «Продуктовый помощник». Онлайн-сервис и API для него, где пользователи могут публиковать рецепты, подписываться на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления одного или нескольких выбранных блюд.

## **Как запустить проект:**

Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:amirsvc/foodgram-project-react.git
```
```
cd foodgram-project-react
```
Перейти в папку infra
```
cd infra
```

Создать файл .env, где харнятся секреты.
Пример наполнения:
```
SECRET_KEY=bovh!l-bg8y_ltn&797yh66^&8adw&z1xoyj+$mie7=j(^#jr1
ALLOWED_HOSTS=example.org

DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```
Развернуть контейнеры c приложением в Docker из директории infra :
```
docker-compose up -d --build
```
Выполнить миграции:
```
docker-compose exec Django python manage.py migrate
```
Собрать статику:
```
docker-compose exec Django python manage.py collectstatic --no-input
```
Загрузить в БД ингредиенты и теги:
```
docker-compose exec Django python manage.py import_from_csv
```
Создать суперпользователя:
```
docker-compose exec Django python manage.py createsuperuser
```

Проект будет доступен по адресу: http://localhost/

## **Разработчик:**

[Амир Исиналинов](https://github.com/amirsvc)

## **Лицензия:**
MIT