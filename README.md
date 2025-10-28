# Создание виртуального окружения
python -m venv .venv

# Активация виртуального окружения
# Для Windows:
.venv\Scripts\activate
# Для Linux/Mac:
source .venv/bin/activate

# Установка зависимостей
pip install django
pip install Pillow

# Запуск сервера разработки
python manage.py runserver