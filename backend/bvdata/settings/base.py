"""
Django settings for bvdata project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
from pathlib import PurePath as Path

import sentry_sdk
from django.utils.translation import gettext_lazy as _
from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).parents[2]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY", "")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(os.getenv("DEBUG", False))

ALLOWED_HOSTS = [
    i for i in os.environ.get("ALLOWED_HOSTS", "data.berlin-vegan.de").split(",")
]

CSRF_TRUSTED_ORIGINS = ALLOWED_HOSTS

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
# Application definition

INSTALLED_APPS = [
    "bvdata.data",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "crispy_forms",
    "django_filters",
    "rest_framework",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if DEBUG:
    try:
        import debug_toolbar  # noqa F401

        MIDDLEWARE += [
            "debug_toolbar.middleware.DebugToolbarMiddleware",
        ]
        INSTALLED_APPS += [
            "debug_toolbar",
        ]
        INTERNAL_IPS = [
            "127.0.0.1",
        ]
    except ImportError:
        pass

ROOT_URLCONF = "bvdata.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DATABASE_NAME", "postgres"),
        "USER": os.environ.get("DATABASE_USER", "postgres"),
        "PASSWORD": os.environ.get("DATABASE_PASSWORD", "postgres"),
        "HOST": os.environ.get("DATABASE_HOST", "postgres"),
        "PORT": os.environ.get("DATABASE_PORT", 5432),
    }
}

CRISPY_TEMPLATE_PACK = "bootstrap4"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.SessionAuthentication",
    ),
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_RENDERER_CLASSES": (
        "djangorestframework_camel_case.render.CamelCaseJSONRenderer",
        "djangorestframework_camel_case.render.CamelCaseBrowsableAPIRenderer",
    ),
    "DEFAULT_PARSER_CLASSES": (
        "djangorestframework_camel_case.parser.CamelCaseFormParser",
        "djangorestframework_camel_case.parser.CamelCaseMultiPartParser",
        "djangorestframework_camel_case.parser.CamelCaseJSONParser",
    ),
}

REST_REGISTRATION = {
    "REGISTER_VERIFICATION_ENABLED": False,
    "RESET_PASSWORD_VERIFICATION_ENABLED": False,
    "REGISTER_EMAIL_VERIFICATION_ENABLED": False,
    "PROFILE_SERIALIZER_CLASS": "bvdata.data.api_v1.serializers.AccountProfileModelSerializer",
}

WSGI_APPLICATION = "bvdata.wsgi.application"

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = "en"

LANGUAGES = [("de", _("German")), ("en", _("English"))]

TIME_ZONE = "Europe/Berlin"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATICFILES_DIRS = [os.path.join(BASE_DIR, "bvdata/static")]

STATIC_URL = "/dstatic/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

LOGIN_REDIRECT_URL = "/dashboard/"

# email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
SERVER_EMAIL = os.environ.get("SERVER_EMAIL", "")
EMAIL_HOST = os.environ.get("EMAIL_HOST", "")
EMAIL_PORT = os.environ.get("EMAIL_PORT", "")
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER", "")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD", "")
EMAIL_FROM = os.environ.get("EMAIL_FROM", "")
EMAIL_GASTROS = os.environ.get("EMAIL_GASTROS", "")

sentry_sdk.init(
    dsn=os.environ.get("SENTRY_DSN", None),
    integrations=[DjangoIntegration()],
    traces_sample_rate=0.2,
)
