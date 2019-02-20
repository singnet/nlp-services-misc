![singnetlogo](../assets/singnet-logo.jpg?raw=true 'SingularityNET')

# Named Entity Disambiguation
### Service User's Guide

### Welcome
This service provides named entity disambiguation for words detected using dbpedia 2016 dumps to disambiguate between words. 
For words that don't exist in the dbpedia disambiguation dump, the returned result is empty. 
o

This service utilizes spacy's small english vocaubulary to find word entities and nlt's stopwords module to tokenize the 
given sentence. 

### How does it work?

The user must provide an input sentence that is not `None` or ''. Besides there aren't yet restriction to that. 

### Using the service on the platform: 
```proto
message Input {
    string input = 1;
}
```
The output is models as follows
```proto
message Output {
    repeated Disambiguation disambiguation = 1;
}

message Disambiguation {
    string named_entity = 1;
    string disambiguation_word = 2;
    string disambiguation_link = 3;
}
```

For query input: 



Examples 1: 
```bash
input: "Macdonald was a great firm before it was sold to S. J. Wolfe & Co. "
```
protobuf result
```bash
disambiguation {
  named_entity: "Macdonald"
  disambiguation_word: "John Alexander Macdonald"
  disambiguation_link: "http://dbpedia.org/resource/John_Alexander_Macdonald"
}
```
python, MessageToDict converted result
```python
{'disambiguation': [{'namedEntity': 'Macdonald', 'disambiguationWord': 'John Alexander Macdonald', 'disambiguationLink': 'http://dbpedia.org/resource/John_Alexander_Macdonald'}]}
```

Example 2:

MessageToDict converted result
```proto
input: "Silicon Valley is a great series. So was The Big Bang Theory."
```
output from our service
```proto
disambiguation {
  named_entity: "Silicon Valley"
  disambiguation_word: "Silicon Valley TV series"
  disambiguation_link: "http://dbpedia.org/resource/Silicon_Valley_TV_series"
}
```
Python MessageToDict converted result
```python
{'disambiguation': [{'namedEntity': 'Silicon Valley', 'disambiguationWord': 'Silicon Valley TV series', 'disambiguationLink': 'http://dbpedia.org/resource/Silicon_Valley_TV_series'}]}
```

The named entity disambiguator is not perfect yet though. Queries like this make it output nothing as dbpedia is limited. 

```proto
input: "MacDonald's is great place to eat fast food."
```
response from our service
```proto
disambiguation {
}
```
Python MessageToDict converted result
```python
{'disambiguation': [{}]}
```
