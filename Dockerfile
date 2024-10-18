# Вибір базового образу з Python 3.12
FROM python:3.12-slim

# Встановлюємо робочу директорію для контейнера
WORKDIR /app

# Встановлюємо залежності для використання PostgreSQL і Pipenv
RUN apt-get update && apt-get install -y gcc libpq-dev curl && \
    curl https://raw.githubusercontent.com/pypa/pipenv/master/get-pipenv.py | python

# Копіюємо Pipfile і Pipfile.lock до контейнера
COPY Pipfile Pipfile.lock /app/

# Встановлюємо залежності через Pipenv
RUN pipenv install --deploy --ignore-pipfile

# Додаємо діагностику для перевірки встановлених пакетів
RUN pipenv run pip freeze

# Копіюємо всі файли проекту до контейнера
COPY . /app/

# Виставляємо порт 8000
EXPOSE 8000

# Виконуємо міграції бази даних і запускаємо сервер
CMD ["sh", "-c", "pipenv run python /app/django_DS_progect/manage.py migrate && pipenv run python /app/django_DS_progect/manage.py runserver 0.0.0.0:8000"]
