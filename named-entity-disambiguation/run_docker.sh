#!/usr/bin/env bash
sudo docker build -t singularitynet/named-entity-disambiguation .
sudo docker run -d -v /etc/letsencrypt:/etc/letsencrypt -it -p 8005:8005 -p 8006:8006 --name named-entity-disambiguation singularitynet/named-entity-disambiguation:latest
