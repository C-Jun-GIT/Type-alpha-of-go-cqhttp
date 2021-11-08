import requests
import json


def send_group(gid, message):
    """发送群聊消息"""
    url = 'http://127.0.0.1:5700/send_group_msg?group_id={0}&message={1}'
    r = requests.get(url.format(gid, message))
    return r


def send_private(uid, message):
    """发送私聊消息"""
    url = 'http://127.0.0.1:5700/send_private_msg?user_id={0}&message={1}'
    r = requests.get(url.format(uid, message))
    return r


def delete_msg(gid, mid):
    """撤回本机发送的消息"""
    url = 'http://127.0.0.1:5700/delete_msg?group_id={0}&message_id={1}'
    requests.get(url.format(gid, mid))


def msg_id(r):
    """获取本机发送消息的message_id"""
    r = r.text
    r = json.loads(r)
    r = r['data']['message_id']
    return r
