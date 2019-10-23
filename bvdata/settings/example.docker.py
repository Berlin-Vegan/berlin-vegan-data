import os

from bvdata.settings.base import *  # noqa:  F401, F403

SECRET_KEY = os.environ.get("SECRET_KEY", "")

DEBUG = False

ALLOWED_HOSTS = []
CSRF_TRUSTED_ORIGINS = ALLOWED_HOSTS

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DATABASE_NAME", ""),
        "USER": os.environ.get("DATABASE_USER", ""),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD", ""),
        "HOST": "postgres",
        "PORT": 5432,
    }
}

ADMINS = os.environ.get("ADMINS", [])

SERVER_EMAIL = os.environ.get("SERVER_EMAIL", "")

EMAIL_HOST = os.environ.get("EMAIL_HOST", "")
EMAIL_PORT = os.environ.get("EMAIL_PORT", "")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
EMAIL_FROM = os.environ.get("EMAIL_FROM", "")
EMAIL_GASTROS = os.environ.get("EMAIL_GASTROS", "")
