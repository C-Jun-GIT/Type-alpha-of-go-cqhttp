import requests


def setu(message, r18_flag):
    url = 'https://api.lolicon.app/setu/v2'
    if r18_flag == 1:
        url = url + '?r18=1'
    else:
        url = url + '?r18=0'
    tag = get_tag(message)
    url_1 = url + tag
    res = requests.get(url_1)
    if not res.json()['data']:
        res = requests.get(url)
        title = res.json()['data'][0]['title']
        author = res.json()['data'][0]['author']
        pid = res.json()['data'][0]['pid']
        setu_url = res.json()['data'][0]['urls']['original']
        message_re = '检索大失败，随便来一张吧~\n' + '画师:' + author + '\n标题:' + title + '\npid:' + str(pid) + '\n' + r'[CQ:image,file=' + setu_url + r']'
        return message_re
    else:
        title = res.json()['data'][0]['title']
        author = res.json()['data'][0]['author']
        pid = res.json()['data'][0]['pid']
        setu_url = res.json()['data'][0]['urls']['original']
        message_re = '画师:' + author + '\n标题:' + title + '\npid:' + str(pid) + '\n' + r'[CQ:image,file=' + setu_url + r']'
        return message_re


def get_tag(message):
    message = message.replace('r18', '')
    message = message[3:len(message) - 2]
    if message != '':
        tag_list = message.split('+')
        tag = '&tag=' + '&tag='.join(tag_list)
    else:
        tag = ''
    return tag
