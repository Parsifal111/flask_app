# Используем официальный образ Python
FROM python:3.10

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY app.py /app

# Устанавливаем зависимости
RUN pip install flask gunicorn

# Открываем порт 80 для веб-сервера
EXPOSE 80

# Запускаем сервер Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app"]
