# berlin-vegan-data
![](https://www.berlin-vegan.de/wp-content/themes/dorayakichildthemefolder/images/bv-header.png)
This software is made for [https://www.berlin-vegan.de/](https://www.berlin-vegan.de).
## requirements
* python 3.6
* packages ``` gettext git libffi-dev libpq libjpeg-turbo-dev libxslt-dev gcc libc-dev linux-headers musl-dev postgresql-dev python3-dev```
## start developing
```
git clone https://github.com/Berlin-Vegan/berlin-vegan-data.git
```
```
cd berlin-vegan-data
```
```
python3.6 -m venv env
```
```
source env/bin/activate
```
```
pip install -Ur requirements.txt
```
```
./manage.py migrate
```
## deploy with docker
```
git clone git@github.com:Berlin-Vegan/berlin-vegan-data.git
```
```
cd berlin-vegan-data
```
```
cp bvdata/settings/example.docker.py bvdata/settings/docker.py
```
Edit docker.py and add your host as string. 
```
cp example.env .env
```
Edit .env for db and secret key (must be long and random, have a look at 'bvdata/settings/dev.py').
```
docker-compose build
```
```
docker-compose up -d
```
### licence
This software is licensed under GNU AFFERO GENERAL PUBLIC LICENSE Version 3. For more information read the [LICENSE FILE](https://github.com/Berlin-Vegan/berlin-vegan-data/blob/master/LICENSE) 