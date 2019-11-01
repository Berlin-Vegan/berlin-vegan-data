#!/bin/bash

git checkout master
git pull
docker-compose up -d --build
