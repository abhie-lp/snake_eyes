"""App settings file"""

from decouple import config

DEBUG = True
SERVER_NAME = "localhost:8000"
SECRET_KEY = "this is a big secret key. Don't share it"

MAIL_DEFAULT_SENDER = "contact@snake_eyes.host"
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = config("MAIL_USERNAME")
MAIL_PASSWORD = config("MAIL_PASSWORD")

CELERY_BROKER_URL = "redis://:redispassword@redis:6379/0"
CELERY_RESULT_BACKEND = "redis://:redispassword@redis:6379/0"
CELERY_ACCEPT_CONTENT = ("json",)
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_REDIS_MAX_CONNECTIONS = 5
