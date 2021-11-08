import requests


def yingxiaohao(message):
    message_0 = message.split(" ", 3)[1]  # 对象
    message_1 = message.split(" ", 3)[2]  # 事件
    message_2 = message_0 + message_1     # 对象+事件
    message_3 = message.split(" ", 3)[3]  # 事件的另一种说法
    message_re = message_2 + '是怎么回事呢？' + message_0 + '相信大家都很熟悉，但是' \
                 + message_2 + '是怎么回事呢，下面就让小编带大家一起了解吧。\n' \
                 + message_2 + '，其实就是' + message_3 + '，大家可能会很惊讶' + message_0 \
                 + '怎么会' + message_1 + '呢？但事实就是这样，小编也感到非常惊讶。\n' \
                 + '这就是关于' + message_2 + '的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！'
    return message_re


def nima(uid):
    url = 'https://nmsl.shadiao.app/api.php?level=min&lang=zh_cn'
    zu_an = requests.get(url)
    message_re = r'[CQ:at,qq=' + str(uid) + r'] ' + zu_an.text
    return message_re


def biaobai(uid):
    url = 'https://chp.shadiao.app/api.php'
    message_re = requests.get(url)
    message_re = r'[CQ:at,qq=' + str(uid) + r'] ' + message_re.text
    return message_re


def pyq():
    url = 'https://pyq.shadiao.app/api.php'
    message_re = requests.get(url).text
    return message_re
