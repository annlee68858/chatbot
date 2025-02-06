
import requests
import json
import random
import time

def gen_context():
    """
    预设的剧本信息，聚焦于 Sahara 社区建设相关的活动与公告
    """
    context_list = [
        "2分钟了?",
        "休息一下",
        "继续卷",
        "继续冲刺20级",
        "大家加油",
        "聊聊天聊聊天",
        "兄弟们好",
        "半天没升一级",
        "太难了"
    ]
    return random.choice(context_list)

def send_message(token, channel_id, message, proxies=None):
    """
    发送消息到 Discord 指定频道
    
    :param token: 认证 token
    :param channel_id: 频道 ID
    :param message: 要发送的消息内容
    :param proxies: 可选的 HTTP 代理配置字典
    :return: requests.Response 对象
    """
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0"
    }
    data = {
        "content": message,
        "nonce": str(random.randrange(1000000000, 9999999999)),
        "tts": False
    }
    response = requests.post(url, headers=headers, data=json.dumps(data), proxies=proxies)
    return response

if __name__ == '__main__':
    # 如需要使用代理，请配置代理（下例为示例代理），否则将 proxies 设为 None
    proxies = {
        "https": "http://14a14daf4664c:8df3b8be0f@194.40.205.150:12324",
        "https": "http://14a51466092b1:bad8c98aa0@212.236.127.133:12323",
        "https": "http://14a51466092b1:bad8c98aa0@212.236.236.229:12323",
        "https": "http://14a51466092b1:bad8c98aa0@212.236.113.118:12323",
        "https": "http://14a51466092b1:bad8c98aa0@89.23.76.212:12323",
        "https": "http://14a51466092b1:bad8c98aa0@212.236.216.12:12323"
    }
    # 如果不需要代理，请取消下面这一行注释
    # proxies = None

    # 多账户配置：每个账户包含 token 和对应的 channel_id
    accounts = [
       
        # 可添加更多账户，例如：
        # {"token": "MTI2Mzc1ODM1NTI0NDI1NzI5Mw.GXXF2j.L939ZQ4Tap9B48bmwupwACAOhp_7neWIdlt0J0", "channel_id": "1275205888977801339"}
    ]

    while True:
        # 生成预设聊天消息
        msg = gen_context()
        for account in accounts:
            response = send_message(account["token"], account["channel_id"], msg, proxies=proxies)
            print(f"账户 {account['token'][:10]}... 发送结果：", response.text)
            # 每个账户之间稍作等待（10到20秒）
            time.sleep(random.randint(10, 20))
        # 每轮所有账户发送完成后，随机等待120到150秒后再发送下一条消息
        wait_time = random.randint(120, 150)
        print(f"等待 {wait_time} 秒后发送下一条消息。")
        time.sleep(wait_time)
