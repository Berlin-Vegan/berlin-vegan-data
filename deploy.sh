#!/bin/bash

#git checkout master
#git pull

docker-compose up -d --build

#migration
docker-compose exec django sh -c "pipenv run python manage.py migrate"

#compilemessages
docker-compose  exec django sh -c "pipenv run python manage.py compilemessages -l de"

#collect static
docker-compose  exec django sh -c "pipenv run python manage.py collectstatic --noinput"
