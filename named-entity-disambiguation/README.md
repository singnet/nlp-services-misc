![singnetlogo](docs/assets/singnet-logo.jpg?raw=true 'SingularityNET')

Named Entity Disambiguation (NED)
=================================
Definition
----------
Named Entity Disambiguation (NED) also know as entity linking or entity resolution  is the task of linking mentions of entities in text to a given
knowledge Base, such as Freebase or Wikipedia.

System Description 
-----------------
The system accepts text as an input and return Named entities with their corresponding disambiguation link from the knowledge Base (KB). 

Knowledge Base (KB)
-------------------
The Knowledge base is crafted from DBpedia version 2015-10. This DBpedia release is based on updated Wikipedia dumps dating from 
October 2015. Link for unprocessed Wikipedia dump: http://downloads.dbpedia.org/2015-10/core-i18n/en/disambiguations_en.tql.bz2.
The script to build the knowledge Base (KB) can be found in script folder namely, dictionary_creator.py.

Installation
------------
To build the docker model of this application 
```bash
docker build -t singularitynet/named-entity-disambiguation .
```


Deployment
```bash
docker run --rm -it -p 8006 - p 8005 --name named-entity-disambiguation singularitynet/named-entity-disambiguation python3.6 service_provider.py
```

Authors
------
- Zelalem Fantahun - Author - [SingularityNet.io](https://singularitynet.io)
- Tesfa Yohannes - Maintainer - [SingularityNet.io](https://singularitynet.io)