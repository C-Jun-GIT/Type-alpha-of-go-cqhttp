import send


def switch(gid, message, j):
    # 以下为功能列表，新增功能时直接在后面添加
    if message == '奥利奥' or message == '涩图' or message == '祖安'\
            or message == '表白' or message == '营销号' or message == '骰子' \
            or message == '朋友圈' or message == '二次元' or message == '二次元图'\
            or message == '网易云':
        if j == 0:
            updateFile(r"./data/flag.txt", message + ':1', message + ':0')
            send.send_group(gid, '已关闭功能:' + message)
        elif j == 1:
            updateFile(r"./data/flag.txt", message + ':0', message + ':1')
            send.send_group(gid, '已开启功能:' + message)


def flag(message):
    with open('./data/flag.txt', 'r', encoding='utf-8') as file:
        flag_0 = file.readlines()
        if flag_0.count(message + ':1\n') > 0 or flag_0.count(message + ':1') > 0:
            flag_1 = 1
        else:
            flag_1 = 0
    return flag_1


def updateFile(file, old_str, new_str):
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)
