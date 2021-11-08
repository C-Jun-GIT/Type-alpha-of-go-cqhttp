import requests


def netease():
    url = 'https://api.ghser.com/wyy/reping.php'
    res = requests.get(url).json()
    res_data = res['data']
    name = res_data['name']
    auther = res_data['auther']
    picurl = res_data['picUrl']
    content = res_data['content']
    message_re = auther + ' - ' + name + '\n' + r'[CQ:image,file=' + picurl + r']' + '\n' + content
    return message_re
