# Вибір базового образу, наприклад Python
FROM python:3.11-slim

# Створення робочої директорії в контейнері
WORKDIR /app

# Копіювання файлу з залежностями (requirements.txt) в робочу директорію
COPY requirements.txt /app/

# Встановлення необхідних залежностей через pip
RUN pip install -r requirements.txt

# Копіювання всіх файлів проєкту в контейнер
COPY . .

# Команда для запуску програми
CMD ["python", "app.py"]
