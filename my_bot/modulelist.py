def modlist():
    with open('./data/flag.txt', 'r', encoding='utf-8') as file:
        modls = file.readlines()
    message_re = []
    for modl in modls:
        m = modl.split(':')          #以':'分割行，m[0]为模块名，m[1]为模块状态
        if int(m[1]) > 0:
            message_re.append('|○|' + m[0] + '\n')
        else:
            message_re.append('|×|' + m[0] + '\n')
    return ''.join(message_re)

