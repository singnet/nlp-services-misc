![singnetlogo](../docs/assets/singnet-logo.jpg?raw=true 'SingularityNET')

Coreference Resolution
======================
Definition and Application area
----------
Coreference resolution is the task of finding all expressions that refer to the same entity in a text. It is an 
important step for a lot of higher level NLP tasks that involve natural language understanding such as document
summarization, question answering, and information extraction. 

This service provides a wrapper around [allenlp](https://demo.allennlp.org/coreference-resolution)'s great demo and models available for reference resolution

Installation 
============
* Natively
```bash
pip install -r requirements.txt
./install.sh
```
* Using Docker
```bash
docker build -t singuliartynet/coreference-resolution-service .
```

Deployment
-----
- GRPC endpoint
```
docker run --rm -it -p 8001 --name coref singularitynet/coreference-resolution-service 
```
- Dameon endpoint
```
docker run --rm -it -p 8007 -p 8008 --name coref singularitynet/coreference-resolution-service 
```

For sample usage: Look at [usage](../docs/users_guide/index.html) documentation.

Authors
------
- Zelalem Fantahun - Author - [SingularityNet.io](https://singularitynet.io)
- Tesfa Yohannes - Maintainer - [SingularityNet.io](https://singularitynet.io)