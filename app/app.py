from flask import Flask, render_template_string
import logging

app = Flask(__name__)

# Логирование ошибок
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Шаблон HTML-страницы
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome</title>
</head>
<body>
    <h1>Welcome to the Test Web Server!</h1>
</body>
</html>
"""

@app.route('/')
def home():
    try:
        return render_template_string(HTML_TEMPLATE)
    except Exception as e:
        app.logger.error(f"Error rendering the page: {e}")
        return "Internal Server Error", 500

# Обработка некорректных маршрутов
@app.errorhandler(404)
def not_found(error):
    return "Page Not Found", 404

# Обработка серверных ошибок
@app.errorhandler(500)
def internal_error(error):
    return "Internal Server Error", 500

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=80, debug=False)
    except Exception as e:
        logging.error(f"Failed to start the server: {e}")
