
import csv
import json
from transliterate import translit, get_available_language_codes
import requests
import time
import os

import re

text = u'This is a smiley face \U0001f602'
print(text) # with emoji

def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)

print(deEmojify(text))


txt_file = 'data\girik_txt\Jirinovskiyi_V._Antikissindjer.txt'
def convert_1stver(txt_file, n, m):
    """ Берем тестовый файл и составляем на его основе формат all_essays.jsonl
    {"text": "Тема: Комедия или драма? (по пьесе А.С. Грибоедова «Горе от ума»)\nСочинение: Грибоедов рассматривал театр
    1) Просто весь текст файла помещаем в поле "text"
    2) Вариант 2, если 1й плохой: сделать сплит по "Владимир Вольфович Жириновский" в каждом файле и брать "Тема: краткое содержание книги или начало вразы, а \nСочинение: полный текст книги.
    """
    results = []
    all_files = os.listdir("data\girik_txt")
    print(all_files)
    for file_name in all_files:
        file_name_path = "data/girik_txt" + "/" + file_name
        with open(file_name_path, mode="r", encoding="windows-1251", errors = 'backslashreplace') as csvfile:  # windows-1251
            #print(csvfile.read())
            raw_text = csvfile.read().strip().lstrip().rstrip().replace('\n', ' ').replace('\r', '').replace("'","")
            #print(raw_text)
            jsonl_string = {"text":raw_text}
            print(jsonl_string)
            results.append(jsonl_string)

    with open('data/girik_all.txt', 'a', encoding="utf-8") as out:
        for item in results:
            text = item
            try:
                out.write("{}".format(text) + '\n')
            except:
                print('encode error')

#convert_1stver(txt_file, 30000, 33000)

def convert_2ndver(path):
    """ Берем тестовый файл и составляем на его основе формат all_essays.jsonl
    {"text": "Тема: Комедия или драма? (по пьесе А.С. Грибоедова «Горе от ума»)\nСочинение: Грибоедов рассматривал театр
    2) Вариант 2, сделать сплит по "Владимир Вольфович Жириновский" в каждом файле и брать "Тема: краткое содержание книги или начало вразы, а \nСочинение: полный текст книги.
    а лучше по абзацам
    """
    results = []
    all_files = os.listdir(path)
    print(all_files)
    for file_name in all_files:
        file_name_path = path + "/" + file_name
        with open(file_name_path, mode="r", encoding="windows-1251", errors = 'backslashreplace') as csvfile:  # windows-1251
            #print(csvfile.read())
            raw_text = csvfile.read()
            # try:
            #     split_text = 'Владимир Вольфович Жириновский'
            #     question = raw_text.split(split_text)[0]
            #     answer = raw_text.split(split_text)[1]
            # except:

            print('no Владимир Вольфович Жириновский')
            split_text = '\n\n'
            question = ' '.join(raw_text.splitlines()[0:7])
            print('question', question)
            answer = ' '.join(raw_text.splitlines()[6:5000])
            print('answer', answer)

            #print(raw_text)
            jsonl_string = {"text":"Скажи:{}\nВ. Жириновский:{}".format(question.strip().lstrip().rstrip().replace('\n', ' ').replace('\r', '').replace("'","").replace("--",""),answer.strip().lstrip().rstrip().replace('\n', ' ').replace('\r', '').replace("'","").replace("--",""))}
            print(jsonl_string)
            results.append(jsonl_string)

    with open('data/girik_all2.txt', 'a', encoding="utf-8") as out:
        for item in results:
            text = item
            try:
                out.write("{}".format(text) + '\n')
            except:
                print('encode error')

convert_2ndver("data\girik_txt")