FROM python:3.9.0-alpine
COPY . /app
WORKDIR /app
RUN apk add --no-cache --virtual .build-deps build-base gcc libc-dev fortify-headers linux-headers python3-dev musl-dev \
    && apk add postgresql-dev gettext make && pip install pipenv==2018.11.26 && pipenv sync && apk del .build-deps

ENV DJANGO_SETTINGS_MODULE=bvdata.settings.base
EXPOSE 8000
CMD ["make", "prod"]
