from bvdata.settings.base import *  # noqa: F401, F403

SECRET_KEY = "j^zkg+vzp$r6w9$u*(u_^owohiyy$%l7f43=is2o--hgfj2^sl"

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "bvdata",
        "USER": "bvdata",
        "PASSWORD": "bvdata",
    }
}

EMAIL_HOST = "localhost"
EMAIL_PORT = 1025
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_FROM = "test@test.de"
EMAIL_GASTROS = "test@test.de"
