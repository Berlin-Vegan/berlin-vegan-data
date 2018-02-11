#!/bin/bash

git checkout master
git pull

#docker build
docker-compose build

#docker up
docker-compose up -d

#migration
docker exec -ti berlinvegandata_django_1 sh -c "python manage.py migrate"

#compilemessages
docker exec -ti berlinvegandata_django_1 sh -c "python manage.py compilemessages -l de"

#collect static
docker exec -ti berlinvegandata_django_1 sh -c "python manage.py collectstatic --noinput"

#docker restart django
docker restart berlinvegandata_django_1