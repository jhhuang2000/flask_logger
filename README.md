LOGGER с использованием flask, БД - sqlite, ORM - SQLAlchemy

Что делает?
Собирает всю возможную информацию о пользователе, зашедшим на сайт и перенаправляет его на facebook.com


Как использовать?
1. Скачаиваем все файлы(БД уже создана(log_users.db))
2. Открываем logger.py через python3
3. Необходимо установить(если не установлено) библиотеки: flask, flask_sqlalchemy
4. Запустить logger.py


Что собирает?
1. ip
2. user_agent
3. encoding
4. languages
5. mimetypes
6. connection
7. referer
8. время захода на сервер
