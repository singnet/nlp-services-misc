#!/usr/bin/env bash
sudo docker build -t singularitynet/language-detection-service .
sudo docker run -d -v /etc/letsencrypt:/etc/letsencrypt -it -p 8009:8009 -p 8010:8010 --name language-detection-service singularitynet/language-detection-service:latest
