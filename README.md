# berlin-vegan-data
![](https://www.berlin-vegan.de/wp-content/themes/dorayakichildthemefolder/images/bv-header.png)
This software is made for [https://www.berlin-vegan.de/](https://www.berlin-vegan.de).
## requirements
* python 3.7
* packages: [pipenv](https://github.com/pypa/pipenv)
## start developing
```
git clone https://github.com/Berlin-Vegan/berlin-vegan-data.git
```
```
cd berlin-vegan-data
```
```
pipenv sync --dev
```
Copy the example .env ```cp example.env .env``` and adjust when necessary. Run all database migrations ```pipenv run ./manage.py migrate```.
## deploy with docker
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
