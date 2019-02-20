![singnetlogo](../assets/singnet-logo.jpg?raw=true 'SingularityNET')

# Language Detection Service
## Service User's Guide

### Welcome
This service provides wrapper around [polyglot](https://polyglot.readthedocs.io) to detect langauges. 

### How does it work?

The user must provide a request satisfying the proto descriptions [given](../../language-detection/service_spec/LanguageDetection.proto). That is

* The sentence or paragraph one wants to detect language is separated to sentences by passing it through
the tokenization library of [polyglot](https://polyglot.readthedocs.io/en/latest/Tokenization.html)

### Using the service on the platform

The returned result has the following form: 
```proto
message Output {
    repeated Language language = 1;
}
```
Where language is defined as: 
```proto
message Language {
    string sentence = 1;
    repeated Prediction prediction = 2;
}

message Prediction {
    string language = 2;
    float confidence = 3;
}
```

An example result obtained after passing the sentence: 

```Ich bin das Singularität. I am the singularity. እኔ የነጠላነት ደረጃ ነኝ::``` 
```proto
language {
  sentence: "Ich bin das Singularit\303\244t."
  prediction {
    language: "German"
    confidence: 96.0
  }
  prediction {
    language: "un"
  }
}
language {
  sentence: "I am the singularity."
  prediction {
    language: "English"
    confidence: 95.0
  }
  prediction {
    language: "un"
  }
}
language {
  sentence: "\341\212\245\341\212\224 \341\213\250\341\212\220\341\214\240\341\210\213\341\212\220\341\211\265 \341\213\260\341\210\250\341\214\203 \341\212\220\341\212\235::"
  prediction {
    language: "Amharic"
    confidence: 97.0
  }
  prediction {
    language: "un"
  }
}

```

This form isn't expected to change as the input format. 

### TODO
- Exact steps and service registry address would be updated once service had been registered to platform.
- Handle the weird encoding for the various languages. 
