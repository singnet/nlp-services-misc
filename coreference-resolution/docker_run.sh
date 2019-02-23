#!/usr/bin/env bash
sudo docker build --file Dockerfile . -t singularitynet:coreference-resolution-service
sudo docker run -d -v /etc/letsencrypt:/etc/letsencrypt -it -p 8007:8007 -p 8008:8008 --name coreference-resolution-service singularitynet:coreference-resolution-service
