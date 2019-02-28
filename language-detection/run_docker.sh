#!/usr/bin/env bash
sudo docker build -t singularitynet/language-detection-service .
sudo docker run -d -v /home/zelalem/nlp-services-misc/language-detection/etcd:/language-detection/etcd -v /etc/letsencrypt:/etc/letsencrypt -it -p 8020:8020 -p 8010:8010 --name language-detection-service singularitynet/language-detection-service:latest
