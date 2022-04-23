# berlin-vegan-data
![](https://www.berlin-vegan.de/wp-content/themes/dorayakichildthemefolder/images/bv-header.png)
This software is made for [https://www.berlin-vegan.de/](https://www.berlin-vegan.de).
## Developing
### requirements
* docker
* docker compose

### start developing
```
git clone https://github.com/Berlin-Vegan/berlin-vegan-data.git
cd berlin-vegan-data
```

#### copy the example .env and adjust when necessary
```
cp example.env .env
```
#### start all necessary services
```
docker-compose up -d
```

## Production deployment with docker
You can find a production deployment example in this repository https://github.com/Berlin-Vegan/bvdata-deploy


### licence
This software is licensed under GNU AFFERO GENERAL PUBLIC LICENSE Version 3. For more information read the [LICENSE FILE](https://github.com/Berlin-Vegan/berlin-vegan-data/blob/master/LICENSE)
