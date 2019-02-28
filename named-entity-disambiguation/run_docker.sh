#!/usr/bin/env bash
sudo docker build -t singularitynet/named-entity-disambiguation .
sudo docker run -d -v /home/zelalem/nlp-services-misc/named-entity-disambiguation/etcd:/named-entity-disambiguation/etcd -v /etc/letsencrypt:/etc/letsencrypt -it -p 8016:8016 -p 8006:8006 --name named-entity-disambiguation singularitynet/named-entity-disambiguation:latest
