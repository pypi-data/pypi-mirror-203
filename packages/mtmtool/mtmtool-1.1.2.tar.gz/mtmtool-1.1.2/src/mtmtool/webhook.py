import requests
import json


def auto_send(message, *args, **kwargs):
    if args[0].lower() == "telegram":
        return telegram(message, *args[1:], **kwargs)
    if args[0].lower() == "pushplus":
        return pushplus(message, *args[1:], **kwargs)
    if args[0].lower() == "wechat":
        return wechat(message, *args[1:], **kwargs)
    if args[0].lower() == "qq":
        return qq(message, *args[1:], **kwargs)
    raise ValueError(f"Not Support API Type {args[0]}")


def dingding(text, key: str = ""):
    url = 'https://oapi.dingtalk.com/robot/send?access_token=' + key
    if ':' not in text and "." not in text and "," not in text and "。" not in text:
        text += "."
    data = {
        "msgtype": "text",
        "text": {
            "content": text
        },
    }
    headers = {"Content-Type": "application/json ;charset=utf-8 "}
    html = requests.post(url, data=json.dumps(data), headers=headers)
    return html.ok


def wechat(text, key: str = ""):
    url = 'https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=' + key
    data = {
        "msgtype": "text",
        "text": {
            "content": text
        },
    }
    headers = {"Content-Type": "application/json ;charset=utf-8 "}
    html = requests.post(url, data=json.dumps(data), headers=headers)
    return html.ok


def qq(text, key: str = ""):
    url = "https://qmsg.zendee.cn/send/" + key
    data = {'msg': text}
    html = requests.post(url, data=data)
    return html.ok


def mi(text, key: str = "", title="bot"):
    url = "https://tdtt.top/send"
    data = {"title": title, "content": text, "alias": key}
    response = requests.post(url, data=data)
    return response.ok


def telegram(text: str, bot: str, chat: str, protect_content=False):
    bot_token = bot
    chat_id = chat
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": text,
        "protect_content": protect_content,
    }
    res = requests.get(url, data=data)
    return res.json()


def pushplus(message, token, title="default", template="html"):
    url = f'http://www.pushplus.plus/send?token={token}&title={title}&content={message}&template={template}'
    resq = requests.get(url=url)
    return resq.text
