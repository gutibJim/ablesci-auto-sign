import requests
import os

COOKIE = os.environ["COOKIE"]
SENDKEY = os.environ["SENDKEY"]

url = "https://www.ablesci.com/user/sign"

headers = {
    "Cookie": COOKIE,
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

data = response.json()

msg = data["msg"]

print(msg)

# 微信通知
push_url = f"https://sctapi.ftqq.com/{SENDKEY}.send"

requests.post(push_url, data={
    "title": "AbleSci 自动签到",
    "desp": msg
})
