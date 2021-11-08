import os
import re
import time

# 基础功能模块导入
import send as sd                # 消息发送
from switch import switch, flag  # 功能开关
import modulelist as mdl         # 模块列表
import random

# 扩展功能模块导入
import oreo     # 奥利奥（bot目录不能有中文）
import setu     # 涩图
import img      # 杂图
import spambot  # 垃圾话（营销号、祖安、朋友圈、表白）
import dicebot  # 骰子
import nijigen  # 守护最好的二次元
import netease  # 网易云评论
from lifeRestart.remake import remake


'下面这个函数用来判断信息开头的几个字是否为关键词'
'如果是关键词则触发对应功能，群号默认为空'


def keyword(message, uid, gid=None, nickname=None):
    # 以下为常驻功能区
    if message[0:] == '申请出刀':
        sd.send_group(gid, '剑来！')
    if message[0:] == 'sl':
        sd.send_group(gid, '你行不行啊？')
    if message[0:] == '挂树':
        sd.send_group(gid, '就这？')
    if message[0:] == 'zaima' or message[0:] == '在吗' or message[0:] == '在嘛':
        sd.send_group(gid, 'buzai，guna')
    if message[0:4] == 'send':
        sd.send_private('547118963', '收到来自' + str(uid) + '的一条反馈:“' + message[4:] + '”')  # 记得填你自己的QQ号作为后台
        sd.send_group(gid, '您的反馈已提交~')
    if message[0:] == '帮助文档':
        sd.send_group(gid, '帮助啊，在写了，已经新建文本文档了，将于本月22号与黑暗剑22同步上线')
    # 以下为模块功能区，使用开关来控制运行状态
    if message[0:4] == 'draw':
        if flag('奥利奥') == 1:
            name = message[4:len(message)]
            sd.send_group(gid, r'[CQ:image,file=file:///' + oreo.draw(name) + r']')
    if message[0:3] == '来一份' and (message.find('色图') > -1 or message.find('涩图') > -1):
        if flag('涩图') == 1:
            sd.send_group(gid, '少女祈祷中……')
            if message.find('r18') > -1:
                r = sd.send_group(gid, setu.setu(message, 1))
                time.sleep(17)
                sd.delete_msg(gid, sd.msg_id(r))
            else:
                sd.send_group(gid, setu.setu(message, 0))
    if message[0:] == '来一些色图' or message[0:] == '来一些涩图':
        if flag('涩图') == 1:
            sd.send_group(gid, '少女加倍祈祷中……！')
            for i in range(random.randint(3, 5)):
                sd.send_group(gid, setu.setu(message, 0))
    if message[0] == '骂':
        if flag('祖安') == 1:
            if message[1:7] == r'[CQ:at':
                message_re = spambot.nima(re.findall('.+]', message[11:len(message)])[0].strip(']'))
            elif message[1] == '我':
                message_re = spambot.nima(uid)
            sd.send_group(gid, message_re)
    if message[0:3] == '营销号':
        if flag('营销号') == 1:
            sd.send_group(gid, spambot.yingxiaohao(message))
    if message[0:2] == '表白':
        if flag('表白') == 1:
            if message[2:8] == r'[CQ:at':
                message_re = spambot.biaobai(re.findall('.+]', message[12:len(message)])[0].strip(']'))
                sd.send_group(gid, message_re)
            elif message[2] == '我':
                message_re = spambot.biaobai(uid)
                sd.send_group(gid, message_re)
    if message[0:2] == '.r':
        if flag('骰子') == 1:
            sd.send_group(gid, dicebot.dice(uid, message))
    if message[0:] == '来点二次元语录':
        if flag('二次元') == 1:
            sd.send_group(gid, nijigen.nijigen())
    if message[0:] == '来点朋友圈':
        if flag('朋友圈') == 1:
            sd.send_group(gid, spambot.pyq())
    if message[0:] == '来点二次元图':
        if flag('二次元图') == 1:
            sd.send_group(gid, '少女祈祷中……')
            sd.send_group(gid, img.nijigen_img())
    if message[0:] == '来点网易云':
        if flag('网易云') == 1:
            sd.send_group(gid, netease.netease())
    if message[0:] == '/remake' or message[0:] == '人生重来':
        if flag('重开') == 1:
            remake(nickname)
            pic_path = str(os.getcwd() + '/lifeRestart/example/output{0}.png')
            pic_path = pic_path.replace('\\', '/')
            sd.send_group(gid, '命运之轮正在转动......')
            sd.send_group(gid, r'[CQ:image,file=file:///' + pic_path.format(0) + r']')
            sd.send_group(gid, r'[CQ:image,file=file:///' + pic_path.format(1) + r']')
            sd.send_group(gid, r'[CQ:image,file=file:///' + pic_path.format(2) + r']')
    # 以下为开关区。开关时，无论现有状态如何，统一按输入的命令进行状态的重新设置
    if message[0:2] == '关闭':
        switch(gid, message[2:], 0)
    if message[0:2] == '开启':
        switch(gid, message[2:], 1)
    if message[0:] == '模块列表':
        sd.send_group(gid, '模块列表：\n' + mdl.modlist())
