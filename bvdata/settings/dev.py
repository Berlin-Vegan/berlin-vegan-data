from bvdata.settings.base import *

SECRET_KEY = 'j^zkg+vzp$r6w9$u*(u_^owohiyy$%l7f43=is2o--hgfj2^sl'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
