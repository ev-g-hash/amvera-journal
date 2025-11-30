import os
import logging
from pathlib import Path
from dotenv import load_dotenv

# Пытаемся загрузить .env, но если его нет - не страшно
try:
    load_dotenv()
except Exception:
    pass  # Игнорируем ошибки загрузки .env

BASE_DIR = Path(__file__).resolve().parent.parent

# Секретный ключ из переменных окружения
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-change-me-in-prod')

DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# Разрешённые хосты
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# ... остальной код без изменений ...

# Безопасность для продакшена
if not DEBUG:
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_SSL_REDIRECT = False
    SESSION_COOKIE_SECURE = False
    CSRF_COOKIE_SECURE = False
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'

LOGIN_URL = 'accounts:login'
LOGIN_REDIRECT_URL = 'journal:index'
LOGOUT_REDIRECT_URL = 'journal:index'

# Логирование
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'gunicorn.error': {
            'level': 'INFO',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}