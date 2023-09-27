# FastApi + PostgreSQL, SQLAlchemy, Pytest

Операции над созданием/удалением/обновлением/запросом Ресторанного меню. 
```
menu --> | 
         | submenu --> |
         |             | dishes
```
Реализациия операций CRUD на Fastapi тестами на Pytest. Взаимодействие с базой данных (Postgres) через SQLAlchemy.
Упакованно в docker.

## Старт FastApi + PostgreSQL
```
docker-compose build && docker-compose up -d
```
### host: localhost
### port: 8000
### http://localhost:8000/docs

## Старт тестов pytest (после запуска FastApi + PostgreSQL)
```
cd tests && docker-compose build && docker-compose up
```
