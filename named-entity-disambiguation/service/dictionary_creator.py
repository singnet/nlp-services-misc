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

        self.path = glob.glob('data/*.tql')  # Folder Path
        print('initialized database creator')

    def create_dictionary(self):
        """
        This file creates the dictionary we would use to disambiguate the various entities we would find.
        """
        for filename in self.path:
            with open(filename, 'rt', encoding='utf-8') as f:
                contents = f.read()
                if filename == 'disambiguation_en.tql':
                    print('processing disambigution file')
                    contents = (contents.replace("<http://dbpedia.org/ontology/wikiPageDisambiguates>", ''))
                    save_file = "output/disambiguate_offline_dict.p"

                elif filename == 'redirects_en.tql':
                    print('processing redirects file')
                    contents = (contents.replace("<http://dbpedia.org/ontology/wikiPageRedirects>", ''))
                    save_file == 'output/redirect_offline_dict.p'

                else:
                    print('it skips the file ' + filename)
                    continue

                contents = (contents.replace("<http://en.wikipedia.org/wiki/", ''))
                contents = contents.split('\n')

                for content in contents:
                    array = []
                    array.append(content)
                    self.big_list.append(array[0].split(' '))

                for list in self.big_list:
                    key = (list[0].replace('<http://dbpedia.org/resource/', '').replace('>', '').replace(
                        '_(disambiguation)', '').replace('_', ' '))
                    # print(key)
                    if len(list) > 2:
                        self.list_key.append(key)
                        value = (list[2].replace('<', '').replace('>', ''))
                        self.list_value.append(value)

                for key in self.list_key:
                    self.dict[key] = []

                for i, key in enumerate(self.list_key):
                    self.dict[key].append(self.list_value[i])

                if not os.path.isdir('output/'):
                    os.makedirs('output')
                with open(save_file, "wb") as f:
                    pickle.dump(self.dict, f)


if __name__ == '__main__':
    dictionary = DictionaryCreator()
    dictionary.create_dictionary()
