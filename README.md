AtomicHabits - это SPA веб-приложение, трекер полезных привычек.

Контекст
В 2018 году Джеймс Клир написал книгу «Атомные привычки», 
которая посвящена приобретению новых полезных привычек и искоренению старых плохих привычек. 


Установка и запуск:
	1) Установите Python и Poetry если они не установлены.
	2) Клонируйте репозиторий git clone https://github.com/CatritMe/AtomicHabits
	3) Активируйте виртульное окружение poetry shell
	4) Установите пакеты poetry install
	5) Запустите сервер python manage.py runserver
	6) Смотрите документацию к API swagger/ или redoc/ добавив это к базовому URL

Для создания контейнера в Docker выполните в консоли следующие команды:

docker network create docker_net

docker run -d --network=docker_net --name=postgres_cont -p 5432:5432 -e POSTGRES_DB=drfdocker -e POST
GRES_USER=postgres -e POSTGRES_PASSWORD=12345 postgres:latest

docker-compose up -d --build