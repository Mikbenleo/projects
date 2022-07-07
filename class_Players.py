print("\t\t\t***** class_Players *****")

import json
from random import randint
from class_Basic_words import Basic_words
# source data:
# file_words_subwords = 'words_debug.txt'
file_words_subwords = 'words_test.txt'
file_users_clues = "users_clues.txt"



class Players(Basic_words):
    def __init__(self, basic_word, user_name):
        Basic_words.__init__(self)
        self.basic_word = basic_word
        self.user_name = user_name
        # self.dict_users_clues = self.init_dict_users_clues()
        self.dict_users_clues = self.control_dict_users_clues(user_name)
        self.list_subwords = self.get_list_subword(basic_word)
        self.list_clue_words = self.dict_users_clues[self.user_name][self.basic_word]

    def init_dict_users_clues(self):
        dict_users_clues = {}
        return dict_users_clues

    def create_dict_template_clues(self):
        with open(file_words_subwords, encoding="utf-8") as f:
            list_words_subwords = json.load(f)
        dict_template_clues = {list_words_subwords[0]['word']: ['*']}
        # dict_template_clues = {list_words_subwords[0]['word']: []}
        for i in range(1, len(list_words_subwords)):
            dict_template_clues.update({list_words_subwords[i]['word']: ['*']})
            # dict_template_clues.update({list_words_subwords[i]['word']: []})
        return dict_template_clues

    def control_dict_users_clues(self, user_name):

        with open(file_users_clues, encoding="utf-8") as f:
            a = f.read()
        if a == '':
            self.dict_users_clues = {user_name: self.create_dict_template_clues()}
            with open(file_users_clues, 'w') as f:
                json.dump(self.dict_users_clues, f)
        else:
            with open(file_users_clues) as f:
                self.dict_users_clues = json.load(f)
            if user_name not in self.dict_users_clues.keys():
                self.dict_users_clues[user_name] = self.create_dict_template_clues()
                with open(file_users_clues, 'w') as f:
                    json.dump(self.dict_users_clues, f)

        return self.dict_users_clues

    def insert_clue_in_clues(self, clue_word, basic_word, user_name):
        self.dict_users_clues[user_name][basic_word].append(clue_word)
        if self.dict_users_clues[user_name][basic_word][0] == '*':
            # self.dict_users_clues[user_name][basic_word].pop[0]
            del self.dict_users_clues[user_name][basic_word][0]
        with open(file_users_clues, 'w') as f:
            json.dump(self.dict_users_clues, f)

    def real_deleting(self, list_deleting_words, user_name):
        for word_i in list_deleting_words:
            if word_i in self.dict_word_subwords.keys():
                self.dict_users_clues[user_name][word_i] = ['*']
            else:
                print(f'{word_i} - Ошибка - такого слова нет в  списке исходных слов программы.')
        with open(file_users_clues, 'w') as f:
            json.dump(self.dict_users_clues, f)

    def deleting_early_clues_word(self, input_regime_code):
        list_temp = input_regime_code.split(' ')
        if input_regime_code == '':
            return print(f'Сохранены отгаданные ранее слова для всех исходных слов: '
                         f'{list(self.dict_word_subwords.keys())} для игрока {self.user_name}')
        else:
            list_temp = input_regime_code.split(' ')

            if  list_temp[0] == 'save':
                list_delete_temp = []
                for word_j in self.dict_word_subwords.keys():
                    if word_j not in list_temp[1:]:
                        list_delete_temp.append(word_j)
                self.real_deleting(list_delete_temp, self.user_name)
                return print(f'Стерты тгаданные ранее слова для исходных слов: {list_delete_temp} для игрока {self.user_name}')

            elif list_temp[0] == 'delete':
                list_delete_temp = []
                for word_j in self.dict_word_subwords.keys():
                    if word_j in list_temp[1:]:
                        list_delete_temp.append(word_j)
                self.real_deleting(list_delete_temp, self.user_name)
                return print(f'Стерты тгаданные ранее слова для исходных слов: {list_temp} для игрока {self.user_name}')

            else:
                pass

    def help_hint_letter_1(self, user_name, basic_word):
        list_unclue_suvwords = []
        for subword_i in self.dict_word_subwords[self.basic_word]:
            if subword_i not in self.dict_users_clues[self.user_name][self.basic_word]:
                list_unclue_suvwords.append(subword_i)
        subword_hint = list_unclue_suvwords[randint(0, len(list_unclue_suvwords) - 1)]
        return subword_hint[0: -1]

