import spacy
import pickle
import re
import numpy
from nltk.corpus import stopwords
import sys
import logging


class NamedEntityDisambiguation:
    def __init__(self, text):
        self.english_stopwords = stopwords.words('english')
        self.nlp = spacy.load('en_core_web_sm')
        self.text = text
        self.logger = logging
        try:
            with open('output/disambiguate_offline_dict.p', 'rb') as f:
                self.offline_dic = pickle.load(f)
        except FileNotFoundError as e:
            self.logger.error('File not found')

    def named_entity_disambiguation(self):
        named_entities, _big_final_dict = self._candidate_generation()
        entities = []
        if _big_final_dict is not None:
            entities = self._candidate_ranking(_big_final_dict)

        return named_entities, entities


    def _candidate_generation(self):
        """
        Rough entity identifier using spacy models for isolating words and searching the knowledge base to find
        entities.

        TODO: Case robustness. Better entity recognizers. Better candidate extraction.

        :return: list of entities that exist in the knowledge base from the given names, and their list of candidates
        form the dictionary. If entities don't exist in kb it returns None.
        """
        doc = self.nlp(self.text)
        named_entity_dict = {}
        named_entity_key_list = []
        named_entity_value_list = []
        entity_from_text_list = []
        offline_dic_list = []
        matched_element_list = []

        for ent in doc.ents:
            named_entity = (str(ent.text) + ':' + str(ent.label_))
            named_entity = (named_entity.split(':'))
            # named_entity_key = named_entity[0].replace('\n', '')
            # named_entity_key_list.append(named_entity_key)
            # named_entity_value = named_entity[1].replace('\n', '')
            # named_entity_value_list.append(named_entity_value)
            named_entity_value = named_entity[1].replace('\n', '')
            named_entity_value_list.append(named_entity_value)
            filtered_words = (str(ent.text).split())
            filtered_words =[w for w in filtered_words if w.lower() not in self.english_stopwords]
            named_entity_key = [' '.join(filtered_words)]
            for i in named_entity_key:
                named_entity_key_list.append(i)
        for key in named_entity_key_list:
            named_entity_dict[key] = []
        i = 0
        for key in named_entity_key_list:
            named_entity_dict[key].append(named_entity_value_list[i])
            i = i + 1

        entities = "ORG PERSON LOC GPE".split()
        for entity in entities:
            entity_from_text = [k for k, v in named_entity_dict.items() if entity in v]
            for item in entity_from_text:
                entity_from_text_list.append(item)

        if not entity_from_text_list:
            self.logger.info('No named entity found in the input text')
        else:
            self.logger.info('Entities which are identified from the input sentence')
            self.logger.info(entity_from_text_list)

        for key, value in self.offline_dic.items():
            offline_dic_list.append(key)

        for item in entity_from_text_list:
            for item1 in offline_dic_list:
                if item == item1:
                    matched_element_list.append(item)

        big_final_dict = []
        for i in matched_element_list:
            candidate_list = [v for k, v in self.offline_dic.items() if str(k) == str(i)]
            final_dict = dict(zip(i.split('\n'), candidate_list))
            big_final_dict.append(final_dict)

        if not big_final_dict:
            self.logger.warning("No Match found in the KB")
            return matched_element_list, None
        else:
            self.logger.info('found entities')
            return matched_element_list, big_final_dict

    def _candidate_ranking(self, big_final_dict):
        """
        Rough draft of candidate ranking that utilizes word count within the candidate available words in the sentence.

        TODO: Split sentences. Query Expansion.
        :param big_final_dict: list of candidate as key dictionary pair.
        :return: list of key - resolution pairs that are candidates
        """
        self.logger.info("Disambiguated Entity Link")
        big_list = []

        for dict in big_final_dict:
            for dict_value in dict.values():
                temp = []
                for i in dict_value:
                    x = (i.split("http://dbpedia.org/resource/"))
                    y = list(filter(None, x))
                    yy = (y[0].split('_'))
                    strg = ''
                    for x in yy:
                        strg = strg + x + ' '
                    strg = strg[:-1]
                    temp.append(strg)
                big_list.append(temp)

        big_arr2 = []
        for small_list in big_list:
            arr2 = []
            for i in small_list:
                arr2.append(re.sub(r'[^\w\s]', '', (i)))

            big_arr2.append(arr2)

        input_text_cleaned = re.sub(r'[^\w\s]', '', self.text)
        arr1 = input_text_cleaned.split()  # remove stop words
        arr1 = [w for w in arr1 if w.lower() not in self.english_stopwords]

        self.ranked_entities = []
        for arr2 in big_arr2:
            a = numpy.zeros(shape=(len(arr2), len(arr1)))
            for i in range(len(arr1)):
                for j in range(len(arr2)):
                    if arr1[i] in arr2[j]:
                        a[j][i] = 1
                    else:
                        a[j][i] = 0

            rows = len(a)
            cols = len(a[0])
            highest = []

            for x in range(0, rows):
                rowtotal = 0
                for y in range(0, cols):
                    rowtotal = rowtotal + int(a[x][y])
                highest.append(rowtotal)

            highest_value = highest.index(max(highest))
            ranked_entity = arr2[highest_value]
            self.logger.info(
                'Ambiguous word:' + ranked_entity + '     ' + 'Disambiguation link' + ' ' + 'https://en.wikipedia.org/wiki/' + (
                    ranked_entity).replace(' ', '_'))
            self.ranked_entities.append([ranked_entity,'https://en.wikipedia.org/wiki/' + (ranked_entity).replace(' ', '_')])
        return self.ranked_entities


if __name__ == '__main__':
    NED = NamedEntityDisambiguation(text="Silicon Valley is a great series. So was The Big Bang Theory.")
    named_entities, big_final_dict = NED._candidate_generation()
    print(named_entities)
    if big_final_dict is not None:
        entities = NED._candidate_ranking(big_final_dict)
        print(entities)

