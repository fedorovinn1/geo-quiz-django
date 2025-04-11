# settings.py
"""
Конфигурационный файл для Django проекта. Здесь задаются основные параметры проекта.
"""

from pathlib import Path

# Получаем путь к корневой директории проекта
BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ Django (не используйте в продакшн-окружении, он должен быть уникальным)
SECRET_KEY = 'django-insecure-key-for-demo'

# Включение режима отладки (не рекомендуется включать в продакшн-окружении)
DEBUG = True

# Список разрешенных хостов (указывайте домены, с которых разрешен доступ к приложению)
ALLOWED_HOSTS = []

# Установленные приложения (включает стандартные приложения Django и приложение quiz)
INSTALLED_APPS = [
    'django.contrib.staticfiles',  # Для работы с статики
    'quiz',  # Ваше приложение quiz
]

# Промежуточное ПО для обработки запросов
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # Безопасность
    'django.middleware.common.CommonMiddleware',  # Общие задачи для запросов
]

# Корневой URL конфиг для проекта
ROOT_URLCONF = 'geography_quiz.urls'

# Шаблоны и конфигурация рендеринга
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.'
        'django.DjangoTemplates',  # Использование Django шаблонов
        'DIRS': [BASE_DIR / 'templates'],  # Путь к каталогу шаблонов
        'APP_DIRS': True,  # Разрешает использовать шаблоны внутри приложений
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # Дебаг контекст
                'django.template.context_processors.request',  # Запрос в контексте шаблонов
            ],
        },
    },
]

# Конфигурация WSGI приложения
WSGI_APPLICATION = 'geography_quiz.wsgi.application'

# Конфигурация базы данных (используется SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Используем SQLite для разработки
        'NAME': BASE_DIR / 'db.sqlite3',  # База данных будет храниться в корне проекта
    }
}

# Языковая и временная настройка
LANGUAGE_CODE = 'ru-ru'  # Используется русский язык
TIME_ZONE = 'UTC'  # Установлен UTC

USE_I18N = True  # Включение интернационализации
USE_TZ = True  # Использование временных зон

# Настройки для работы со статическими файлами
STATIC_URL = '/static/'  # URL для статики
STATICFILES_DIRS = [BASE_DIR / 'static']  # Путь к статическим файлам проекта
