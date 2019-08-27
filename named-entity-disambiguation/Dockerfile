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
        libxrender-dev

COPY requirements.txt /tmp

WORKDIR /tmp

RUN curl https://bootstrap.pypa.io/get-pip.py | python3.6
RUN python3.6 -m pip install -r requirements.txt

RUN python3.6 -m nltk.downloader stopwords


# To avoid downloading the wiki dump.

RUN mkdir -p /tmp/data/kb

RUN wget http://downloads.dbpedia.org/2016-10/core-i18n/en/disambiguations_en.tql.bz2 -P data/kb

RUN wget http://downloads.dbpedia.org/2016-10/core-i18n/en/redirects_en.tql.bz2 -P data/kb

WORKDIR /tmp/data/kb

RUN bzip2 -d disambiguations_en.tql.bz2

RUN bzip2 -d redirects_en.tql.bz2

RUN mkdir -p /named-entity-disambiguation && cp -a /tmp/data/kb /named-entity-disambiguation/data

COPY . /named-entity-disambiguation

WORKDIR /named-entity-disambiguation

RUN ./install.sh

EXPOSE 8016
EXPOSE 8006
EXPOSE 8005

CMD ["python3.6", "run-snet-service.py","--daemon-config-path-mainnet","snet.config.example.mainnet.json","--daemon-config-path-mainnet_2", "snet.config.example.mainnet_2.json", "--daemon-config-path-ropsten","snet.config.example.ropsten.json"]
