#!/bin/bash
app="docker-test"
docker build -t ${app}:2.00 .
#docker run --rm -d -p 8050:80 --name=${app} -v $PWD:/app ${app}:2.00
docker run --rm -d -p 8050:80 --name=${app} ${app}:2.00