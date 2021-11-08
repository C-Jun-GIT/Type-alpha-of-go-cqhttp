import requests
import random


def nijigen_img():
    #url_seq = ['https://api.vvhan.com/api/acgimg','http://www.dmoe.cc/random.php']
    #url = random.choice(url_seq)
    url = 'http://www.dmoe.cc/random.php'
    params = {'return': 'json'}
    res = requests.get(url, params=params).json()
    res_1 = res['imgurl']
    message_re = r'[CQ:image,file=' + res_1 + r']'
    return message_re
