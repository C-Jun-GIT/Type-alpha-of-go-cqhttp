import requests
import random


"""
def nijigen():#癌症二次元
    with open('./data/nijigen.txt', 'r', encoding='utf-8') as file:
        list1 = file.readlines()
    a = random.choice(list1)
    a = a.strip()
    return a
"""


def nijigen():
    url = 'http://api.easys.ltd/api/api/ylapi.php'
    message_re = requests.get(url).text
    return message_re
