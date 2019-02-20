import sys
import argparse
from polyglot.detect import Detector
from polyglot.text import Text


class LanguageDetector:
    def __init__(self):
        self.result_dict = {}
        self.sentence_dict = {}

    def language_id(self, text):
        sentences = Text(text)
        for sentence in sentences.sentences:
            self.sentence_dict = {}
            for language in Detector(str(sentence)).languages:
                self.sentence_dict[language.name] = language.confidence
            self.result_dict[str(sentence)] = self.sentence_dict
        return self.result_dict


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', '-t', help='Enter the sentence you want to detect')
    args = parser.parse_args()
    if args.text == None:
        print('Please enter a sentence. Exiting.')
        sys.exit(0)
    print(args.text)

    lang = LanguageDetector()
    lang.language_id(args.text)
