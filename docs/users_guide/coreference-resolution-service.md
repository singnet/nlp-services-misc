![singnetlogo](../assets/singnet-logo.jpg?raw=true 'SingularityNET')

# Correference Resolution Service
## Service User's Guide

### Welcome

This service provides a wrapper around [allenlp](https://demo.allennlp.org/coreference-resolution)'s great demo and models available for reference resolution


### Using the service on the platform
- The input to the system is straight forward. It is a sentence or group of sentences as defined by the following proto. 
```proto
message InputSentence {
    string sentence = 1;
}
```

- The response to the given query is the references and the tokenized words list defined as:
```proto
message ReferenceResolution {
    repeated References references = 1;
    Words words = 2;
}

message References {
    Indexes key = 1;
    repeated Indexes mappings = 2;
}

message Indexes {
    int32 firstIndex = 1;
    int32 secondIndex = 2;
}

message Words {
    repeated string word = 1;
}
```

The following is the response to the query: "Michael is a great man. He does what is required of him.""
```text
references {
  key {
  }
  mappings {
    firstIndex: 6
    secondIndex: 6
  }
  mappings {
    firstIndex: 12
    secondIndex: 12
  }
}
words {
  word: "Michael"
  word: "is"
  word: "a"
  word: "great"
  word: "man"
  word: "."
  word: "He"
  word: "does"
  word: "what"
  word: "is"
  word: "required"
  word: "of"
  word: "him"
  word: "."
}
```

A dictionary represenation of this by passing to google.protobuf's message to dictionary gives:
```python
[{'references': [{'key': {'firstIndex': 0, 'secondIndex': 0},
                 'mappings': [{'firstIndex': 6, 'secondIndex': 6},
                {'firstIndex': 12, 'secondIndex': 12}]}], 'words': {
            'word': ['Michael', 'is', 'a', 'great', 'man', '.', 'He', 'does', 'what', 'is', 'required', 'of', 'him',
                     '.']}}
```

