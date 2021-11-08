import random


def dice(uid, message):
    d = message.find('d')
    if d == -1:
        message_re = r'[CQ:at,qq=' + str(uid) + r'] ' + '1d100掷骰结果是：' + str(random.randint(1, 100))
    else:
        amount_0 = int(message[2:d])
        range_0 = int(message[d + 1:])
        list1 = []
        for i in range(0, amount_0):
            list1.append(random.randint(1, range_0))
        total = sum(list1)
        message_re = r'[CQ:at,qq=' + str(uid) + r'] ' + '掷骰结果是=' + r','.join(str(l) for l in list1) + ' ，总和是：' + str(
            total)
    return message_re
