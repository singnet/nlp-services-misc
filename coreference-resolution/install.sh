#!/usr/bin/env bash

snet_daemon_v=1.0.0
snet_daemon_v_2=4.0.0
snet_daemon_v_3=5.0.1

if [ ! -d models/ ]; then
    mkdir models
    # wget https://s3-us-west-2.amazonaws.com/allennlp/models/coref-model-2018.02.05.tar.gz -O models/coref-model-2018.02.05.tar.gz
    wget https://storage.googleapis.com/allennlp-public-models/coref-spanbert-large-2020.02.27.tar.gz -O models/coref-spanbert-large-2020.02.27.tar.gz
fi

python3.6 -m spacy download en_core_web_sm

# apt install tar
if [ ! -d snet-daemon-v$snet_daemon_v ] ; then
        echo "Downloading snetd-linux"
	wget https://github.com/singnet/snet-daemon/releases/download/v$snet_daemon_v/snet-daemon-v$snet_daemon_v-linux-amd64.tar.gz
	tar -xzf snet-daemon-v$snet_daemon_v-linux-amd64.tar.gz
	ln snet-daemon-v$snet_daemon_v-linux-amd64/snetd snetd-linux-amd64
	rm snet-daemon-v$snet_daemon_v-linux-amd64.tar.gz
        wget https://github.com/singnet/snet-daemon/releases/download/v$snet_daemon_v_2/snet-daemon-v$snet_daemon_v_2-linux-amd64.tar.gz
        tar -xzf snet-daemon-v$snet_daemon_v_2-linux-amd64.tar.gz
        ln snet-daemon-v$snet_daemon_v_2-linux-amd64/snetd snetd-linux-amd64-2
        rm snet-daemon-v$snet_daemon_v_2-linux-amd64.tar.gz
  wget https://github.com/singnet/snet-daemon/releases/download/v$snet_daemon_v_3/snet-daemon-v$snet_daemon_v_3-linux-amd64.tar.gz
  tar -xzf snet-daemon-v$snet_daemon_v_3-linux-amd64.tar.gz
  ln snet-daemon-v$snet_daemon_v_3-linux-amd64/snetd snetd-linux-amd64-3
  rm snet-daemon-v$snet_daemon_v_3-linux-amd64.tar.gz
else
	echo "Folder seems to exist"
fi

python3.6 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service_spec/CoreferenceResolutionService.proto

cp snet.config.example.mainnet snet.config.example.mainnet.json
cp snet.config.example.mainnet_2 snet.config.example.mainnet_2.json
cp snet.config.example.mainnet_3 snet.config.example.mainnet_3.json
cp snet.config.example.ropsten snet.config.example.ropsten.json
