# Используем официальный образ Python
FROM python:3.10

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY app/ /app/app/
COPY app/requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт 80 для веб-сервера
EXPOSE 80

# Запускаем сервер Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:80", "app.app:app"]

