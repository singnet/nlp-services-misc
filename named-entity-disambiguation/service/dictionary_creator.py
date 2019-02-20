#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import os
import glob


class DictionaryCreator:
    def __init__(self):
        self.big_list = []
        self.list_key = []
        self.list_value = []
        self.dict = {}

        self.path = glob.glob('data/kb/*.tql') # Folder Path
        pass
    def create_dictionary(self):
        for filename in self.path:
            print(filename)
            with open(filename, 'rt', encoding='utf-8') as f:
                contents = f.read()
                contents = (contents.replace("<http://dbpedia.org/ontology/wikiPageDisambiguates>", ''))
                contents= (contents.replace("<http://en.wikipedia.org/wiki/",''))
                contents = contents.split('\n')

                for content in contents:
                    array=[]
                    array.append(content)
                    self.big_list.append(array[0].split(' '))

                for list in self.big_list:
                    key = (list[0].replace('<http://dbpedia.org/resource/','').replace('>','').replace('_(disambiguation)','').replace('_',' '))
                    # print(key)
                    if len(list) > 2:
                        self.list_key.append(key)
                        value = (list[2].replace('<','').replace('>',''))
                        self.list_value.append(value)

                for key in self.list_key:
                    self.dict[key]= []

                i = 0
                for key in self.list_key:
                    self.dict[key].append(self.list_value[i])
                    i = i+1
                # print(dict)

                # pickle.dump(dict, open("output/sample_disambiguate_offline_dict.p", "wb"))
                if not os.path.isdir('output/'):
                    os.makedirs('output')
                with open("output/disambiguate_offline_dict.p", "wb") as f:
                    pickle.dump(self.dict, f)

if __name__ == '__main__':
    dictionary = DictionaryCreator()
    dictionary.create_dictionary()
