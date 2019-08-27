FROM ubuntu:18.04

RUN apt-get update && apt-get install -y software-properties-common
RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get update && apt-get install -y --no-install-recommends \
        git \
        build-essential \
        python3.6 \
        python3.6-dev \
        python3-pip \
        python-setuptools \
        cmake \
        wget \
        curl \
        libsm6 \
        libxext6 \
        libxrender-dev \
	libicu-dev

COPY requirements.txt /tmp

WORKDIR /tmp

RUN curl https://bootstrap.pypa.io/get-pip.py | python3.6
RUN python3.6 -m pip install -r requirements.txt

COPY . /language-detection

WORKDIR /language-detection

RUN ./install.sh

EXPOSE 8020
EXPOSE 8010
EXPOSE 8009

RUN python3.6 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service_spec/LanguageDetection.proto

CMD ["python3.6", "run-snet-service.py","--daemon-config-path-mainnet","snet.config.example.mainnet.json","--daemon-config-path-mainnet_2","snet.config.example.mainnet_2.json","--daemon-config-path-ropsten","snet.config.example.ropsten.json"]
