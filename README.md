![example workflow](https://github.com/antongromtsev/yamdb_final/actions/workflows/main.yml/badge.svg)
# YaMDb_final

Проект представляет собой REST API для сервиса YAMDb - база данных отзывов о фильмах, книгах, музыке и многом другом. Документация по работе с API после развертывания и настройки проекта будет доступна по адресу: http://127.0.0.1/redoc

## Перед запуском проекта

Инструкции помогут вам развернуть и запустить копию проекта на вашем локальном компьютере для целей разработки и тестирования. Примечания о том, как развернуть проект в действующей системе, см. в разделе "Развертывание проекта".

### Необходимое окружение

Чтобы запустить проект, вам необходимо установить Docker. Загрузите эту программу с официального [веб-сайта](https://www.docker.com/)



Утсановите Docker на свой копьютер, следуя инструкции по утановке для Window и MacOS.
Инструкция по утановке [Docker Linux](https://docs.docker.com/engine/install/ubuntu/)


## Развёртывание проекта

1. Клонировать репозиторий на локальный компьютер с [github](https://github.com/): 
```bash
git clone https://github.com/antongromtsev/infra_sp2.git
```
2. Перейти в домашнюю директорию проекта: 
```bash
cd infra_sp2
```
3. Создать файл .env и заполнить его:
```bash
    EMAIL_HOST_USER=xxxxxx@gmail.com
    EMAIL_HOST_PASSWORD=xxxxxxxx
```
Проект настроен для работу с почтой google. Укажите email от почты google.
Для отправки сообщений в акаунте google необходиомо [создать пароль для приложения](https://support.google.com/accounts/answer/185833?hl=ru).

```bash
    DB_NAME=postgres # имя базы данных
    POSTGRES_USER=xxxxxx # логин для подключения к базе данных
    POSTGRES_PASSWORD=xxxxxxx # пароль для подключения к БД (установите свой)
    DB_HOST=db # название сервиса (контейнера)
    DB_PORT=5432 # порт для подключения к БД
```

4. Собрать образ и запустить проект:
```bash
docker-compose up
```
Остановить проект
```bash
docker-compose down
```
## Настройка проекта

1. Открыть доплнительную консоль, перейти в деректорию проекта и выполнить миграции:
```bash
docker exec -it infra_sp2_web_1 python manage.py migrate
```
2. Создать супер пользователя:
```bash
docker exec -it infra_sp2_web_1 python manage.py createsuperuser
```
Следуюйте инструкции в консоли.
3. Собрать статикку:
```bash
docker exec -it infra_sp2_web_1 python manage.py collectstatic
```
Следуйте инструкции в консоли.

4. При необходимости БД можно заполнить тестовыми данными
```bash
docker exec -it infra_sp2_web_1 python manage.py loaddata fixtures.json
```
После завершения настройки проект будет запущен и доступен по адресу: http://127.0.0.1/redoc.

Образ на Docker Hub находиться по адресу: https://hub.docker.com/repository/docker/fenix217grom/yamdb
