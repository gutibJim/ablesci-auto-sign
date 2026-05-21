import requests

# 你的 Cookie
COOKIE = "这里以后替换成你的cookie"

# 签到接口
url = "https://www.ablesci.com/user/sign"

headers = {
    "Cookie": COOKIE,
    "User-Agent": "Mozilla/5.0"
}

# 发送请求
response = requests.get(url, headers=headers)

# 输出结果
print(response.text)
