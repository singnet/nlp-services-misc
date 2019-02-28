#!/usr/bin/env bash
sudo docker build --file Dockerfile . -t singularitynet:coreference-resolution-service
sudo docker run -d -v /home/zelalem/nlp-services-misc/coreference-resolution/etcd:/correference-resolution-service/etcd -v /etc/letsencrypt:/etc/letsencrypt -it -p 8018:8018 -p 8008:8008 --name coreference-resolution-service singularitynet:coreference-resolution-service
