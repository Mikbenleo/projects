print("\t\t\t***** class_Basic_words *****")

import json
from random import randint

# source data:
# file_words_subwords = 'words_debug.txt'
file_words_subwords = 'words_test.txt'
file_users_clues = "users_clues.txt"

class Basic_words:
    def __init__(self):
        self.dict_word_subwords = self.create_dict_word_subwords()
        self.list_basic_words = self.dict_word_subwords.keys()

    # The dictionary dict_word_subwords is more convenient to use
    # than the dictionary in the source file file_words_subwords

    def create_dict_word_subwords(self, file_words_subwords=file_words_subwords):
        with open(file_words_subwords, encoding='utf-8') as f:
            list_temp = json.load(f)
        self.dict_word_subwords = {}
        for dict_temp in list_temp:
            key_ = dict_temp['word']
            self.dict_word_subwords[key_] = dict_temp['subwords']
        return self.dict_word_subwords

    def get_list_subword(self, basic_word):
        return self.dict_word_subwords[basic_word]

    def get_rand_basic_word(self):
        list_basic = self.dict_word_subwords.keys()
        rand_basic = list(list_basic)[randint(0, len(list_basic) - 1)]
        return rand_basic



