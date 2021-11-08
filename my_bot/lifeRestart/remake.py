# coding=utf-8
# from hoshino import Service
# from hoshino.typing import HoshinoBot,CQEvent
from PIL import Image, ImageFont, ImageDraw
import re
from os.path import join
#from lifeRestart.Life import Life
from .Life import Life
#from lifeRestart.PicClass import *
from .PicClass import *
import traceback
import random


def draw(text, l, h, n):
    im = Image.new("RGB", (l, h), (255, 255, 255))  # mode, size, color
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype(r"C:\Windows\Fonts\msyhl.ttc", 14)  # 字体文件位置、字号大小
    dr.text((5, 5), text, font=font, fill="#000000")  # 在指定位置绘制字符串，从左到右为坐标、文本、字体、字符颜色
    #    im.show()
    path = str(os.getcwd() + '\\lifeRestart\\example\\output{0}.png')
#    path = 'D:\CJ\go\my_bot\lifeRestart\example\output{0}.png'
    im.save(path.format(n))


def genp(prop):
    ps = []
    # for _ in range(4):
    #     ps.append(min(prop, 8))
    #     prop -= ps[-1]
    tmp = prop
    while True:
        for i in range(0, 4):
            if i == 3:
                ps.append(tmp)
            else:
                if tmp >= 10:
                    ps.append(random.randint(0, 10))
                else:
                    ps.append(random.randint(0, tmp))
                tmp -= ps[-1]
        if ps[3] < 10:
            break
        else:
            tmp = prop
            ps.clear()
    return {
        'CHR': ps[0],
        'INT': ps[1],
        'STR': ps[2],
        'MNY': ps[3]
    }


def remake(name):
    mes_list = []

    Life.load(join(FILE_PATH, 'data'))
    while True:
        life = Life()
        life.setErrorHandler(lambda e: traceback.print_exc())
        life.setTalentHandler(lambda ts: random.choice(ts).id)
        life.setPropertyhandler(genp)
        flag = life.choose()
        if flag:
            break

    choice = 0
    person = name + "本次重生的基本信息如下：\n\n【你的天赋】\n"  # 基本信息
    for t in life.talent.talents:
        choice = choice + 1
        person = person + str(choice) + "、天赋：【" + t.name + "】" + " 效果:" + t.desc + "\n"

    person = person + "\n【基础属性】\n"
    person = person + "   美貌值:" + str(life.property.CHR) + "  "
    person = person + "智力值:" + str(life.property.INT) + "  "
    person = person + "体质值:" + str(life.property.STR) + "  "
    person = person + "财富值:" + str(life.property.MNY) + "  "
    mes_list.append("这是" + name + "本次轮回的基础属性和天赋:" + '\n' + person)

    res = life.run()  # 命运之轮开始转动
    res = list(res)
#    a = sorted(res, key=lambda x: len(x))[-2]
    res0 = []
    for i in res:
        for i1 in i:
            res0.append(i1)
    count = 0
    for i in res0:
        count = max(len(i), count)
    mes = '\n'.join('\n'.join(x) for x in res)
    mes_list.append("这是" + name + "本次轮回的生平:" + '\n' + mes)

    sum = life.property.gensummary()  # 你的命运之轮到头了
    mes_list.append("这是" + name + "本次轮回的评价:" + '\n' + sum)

    draw(mes_list[0], 380, 250, 0)
    draw(mes_list[1], 15 * count, 20 * (len(re.findall('\n', mes_list[1])) + 1) + 10, 1)
    draw(mes_list[2], 15 * (len(name) + 10), 230, 2)
    return mes_list


'''
if __name__ == '__main__':
    remake()
'''
