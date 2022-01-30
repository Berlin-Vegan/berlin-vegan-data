#!/bin/bash

git checkout main
git pull
docker-compose up -d --build
