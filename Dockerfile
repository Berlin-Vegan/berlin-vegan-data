FROM python:3.6-alpine

ENV DEBUG 1
ENV PYTHONUNBUFFERED 1


RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code
ADD bvdata /code
ADD .git /code

RUN apk add --update --no-cache gettext git libffi-dev libpq libjpeg-turbo-dev libxslt-dev && \
    apk add --no-cache --virtual .build-deps gcc libc-dev linux-headers musl-dev postgresql-dev python3-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

ENV DJANGO_SETTINGS_MODULE=bvdata.settings.docker

# uWSGI
ENV UWSGI_WSGI_FILE=bvdata/wsgi.py UWSGI_HTTP=:8000 UWSGI_MASTER=1 UWSGI_WORKERS=2 UWSGI_THREADS=8 UWSGI_UID=1000 UWSGI_GID=2000 UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy

# Start uWSGI
CMD uwsgi --http-auto-chunked --http-keepalive
