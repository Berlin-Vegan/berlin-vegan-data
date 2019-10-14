FROM python:3-alpine
COPY . /app
WORKDIR /app
RUN apk add --no-cache --virtual .build-deps build-base gcc libc-dev fortify-headers linux-headers python3-dev musl-dev \
    && apk add postgresql-dev gettext && pip install pipenv==2018.11.26 && pipenv sync && apk del .build-deps

ENV DJANGO_SETTINGS_MODULE=bvdata.settings.docker

CMD pipenv run python manage.py migrate && \
    pipenv run gunicorn -w 2 --bind 0.0.0.0:8000 --access-logfile - bvdata.wsgi
