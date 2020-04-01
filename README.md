# berlin-vegan-data
![](https://www.berlin-vegan.de/wp-content/themes/dorayakichildthemefolder/images/bv-header.png)
This software is made for [https://www.berlin-vegan.de/](https://www.berlin-vegan.de).
## Developing
### requirements
* Python 3.7
* [pipenv](https://github.com/pypa/pipenv)
* PostgreSQL database

example setup for Ubuntu 18.04 LTS
```
sudo apt install python3.7
pip3 install pipenv
# install docker daemon
sudo apt install docker.io 
# start database as docker container
docker run --name postgres-dev -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:10.1-alpine 
```

### start developing
```
git clone https://github.com/Berlin-Vegan/berlin-vegan-data.git
cd berlin-vegan-data
```
```
pipenv sync --dev
#copy the example .env and adjust when necessary
cp example.env .env 
 
pipenv run ./manage.py migrate
pipenv run ./manage.py createsuperuser
```
```
pipenv run ./manage.py runserver
```

## Production deployment with docker
```
git clone git@github.com:Berlin-Vegan/berlin-vegan-data.git
```
```
cd berlin-vegan-data
```
```
cp example.env .env
```
Edit .env for db, host, secret key, etc.
```
docker-compose up -d --build
```


### licence
This software is licensed under GNU AFFERO GENERAL PUBLIC LICENSE Version 3. For more information read the [LICENSE FILE](https://github.com/Berlin-Vegan/berlin-vegan-data/blob/master/LICENSE)
