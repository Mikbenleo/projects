print("\t\t\t***** main ******")

from class_Basic_words import Basic_words
from class_Players import Players

# source data:
# Lists of main words and subwords here are shorter than in the test file words_test
# file_words_subwords = 'words_debug.txt'
file_words_subwords = 'words_test.txt'

# This file must be empty before the first run
file_users_clues = "users_clues.txt"

b = Basic_words()

input_user_name = input(f"Введите ваше имя  \n")

print(f'''Здравствуйте {input_user_name}. Выберите исходное слово для составления из его букв новых слов.
Новые слова должны быть не короче трех букв. В качестве исходного можете взять \"{b.get_rand_basic_word()}\".
Оно случайно выбрано из списка слов программы. Либо другоe слово из этого списка: \"{b.list_basic_words}\".
''')

input_basic_word = input(f"Введите исходное слово  \n")

if input_basic_word not in b.list_basic_words:
    print(f'Ошибка - такого слова нет в  списке исходных слов программы.')
    exit()

p = Players(input_basic_word, input_user_name)

if len(p.dict_users_clues[p.user_name][p.basic_word]) == (len(p.dict_word_subwords[p.basic_word])):
    print(f'''Вы уже отгадали все слова к исходному слову "{p.basic_word}": {p.list_clue_words}''')
    delete_input = input(f'Чтобы в дальнейшем играть с этим словом, введите   "delete {p.basic_word}" ')
    if delete_input == f'delete {p.basic_word}':
        list_deleting = [p.basic_word]
        p.real_deleting(delete_input, p.user_name)
        print(f'''Отгаданные вами ранее слова к исходному слову "{p.basic_word}" стерты. 
        Можете сново  играть с этим словом''')
    exit()
else:
    print(f'''Вот отгаданные вами слова к исходному слову "{p.basic_word}": {p.list_clue_words}''')

print('''Выберите режим работы с ранее отгаданныыми словами: 
1)сохранить списки отгаданных Вами подслов для Всех исходных слов - код режима <пустая строка>> 
2)сохранить списки отгаданных Вами подслов для указанных исходных слов - код режима 'save' + <список исходных слов> ,
для остальных исходных слов стереть списки отгаданных Вами подслов
3)стереть списки отгаданных Вами подслов для указанных исходных слов - код режима 'delete' + <список исходных слов> 
''')

input_regime_code = input(f"Введите код режима работы с ранее отгаданныыми словами\n")

p.deleting_early_clues_word(input_regime_code)  # Clearing the list of clue words according to the entered mode code

# ===================  Go!  ==============  питон   "пони", "ион", "опт"  ========== набор   "бар", "бон", "бор" ======

# def to_play(): #, user_name=user_name, basic_word=basic_word):
print(f'''С этого места возможны следующие варианты вашего ввода: 
1)отгадываемое слово, 
2)* для показа заготовок отгадываемых слов,
3)"stop" или "стоп" для остановки ввода отгадываемых слов
''')
while len(p.dict_users_clues[p.user_name][p.basic_word]) < (len(p.dict_word_subwords[p.basic_word])):
    user_input = input(f'{p.user_name}:   ')
    if 'stop стоп'.count(user_input) != 0:
        print(f'Вы ввели {user_input} - программа завершена')
        exit()
    # input '*' means  request  a piece of the guessing word
    elif '*'.count(user_input) != 0:
        print(f'''Программа: Вот заготовка слова "{p.help_hint_letter_1(p.user_name, p.basic_word)}"
        - нужно добавить последнюю букву''')
    # inputted word is in the subword of basic word list and is not early guessed words list
    elif (user_input in b.dict_word_subwords[p.basic_word]) and (user_input not in p.list_clue_words):
        p.insert_clue_in_clues(user_input, p.basic_word, p.user_name)
        print(f'Программа: верно. Продолжаем, Ваше следующее слово:')
    elif (user_input in b.dict_word_subwords[p.basic_word]) and (user_input in p.list_clue_words):
        print(f'Программа:верно, но Вы уже вводили это слово')
    elif user_input not in b.dict_word_subwords[p.basic_word]:
        print(f'Программа: неверно.')
        print(f'''Если хотите, дадим идею. Введите * и получите подсказку - 
         случайное из неотгаданных слово без последней буквы.''')
    else:
        pass
print(f'''Программа: слова закончились, игра завершена!\nПрограмма: 
Вы угадали {len(b.dict_word_subwords[p.basic_word])} слов.''')

print('программа завершена')

