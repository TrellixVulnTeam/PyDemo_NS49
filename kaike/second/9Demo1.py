import requests
# 引入requests。
url_login = 'https://xiaoke.kaikeba.com/example/wordpress/wp-login.php'
# 把登录的网址赋值给url。
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
# 加请求头，为了避免被反爬虫
data_login = {
    'log': 'kaikeba',  # 写入账户
    'pwd': 'kaikeba888',  # 写入密码
    'wp-submit': '登录',
    'redirect_to': 'https://xiaoke.kaikeba.com/example/wordpress/2019/10/17/%e5%bc%80%e8%af%be%e5%90%a7%e6%97%a0%e6%95%8c%e5%a5%bd%e5%90%83%e7%9a%84%e9%a3%9f%e5%a0%82%e4%b8%80%e5%91%a8%e8%8f%9c%e8%b0%b1/',
    'testcookie': '1'
}
# 把有关登录的参数封装成字典，赋值给data。
login_in = requests.post(url_login, headers=headers, data=data_login)
# 用requests.post发起请求，放入参数：请求登录的网址、请求头和登录参数，然后赋值给login_in。
print(login_in)
# 打印login_in
