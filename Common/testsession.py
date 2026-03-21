# # -*- coding: utf-8 -*-
# # @Time    : 2018/7/24 下午3:33
# # @Author  : WangJuan
# # @File    : Session.py
#
# """
# 封装获取cookie方法
#
# """
#
# import requests
#
# class Session:
#
#
#     def get_session(self, env):
#         """
#         获取session
#         :param env: 环境变量
#         :return:
#         """
#         # 设置请求头
#         headers = {
#             "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko)\
#                           Chrome/67.0.3396.99 Safari/537.36",
#             "Content-Type": "application/x-www-form-urlencoded"
#         }
#
#         if env == "debug":
#             login_url = 'https://' + 'upass.10jqka.com.cn/login?isIframe=1&main=3&pannel=1&source=sns&redir=https://t.10jqka.com.cn/static/loginBack.html'
#             parm = {
#                 "uname": "EUY6a0eRcQxbP31nZbr2rUl70/W6AgE0FhhBhJ8pxacl1dnjCpWbvCP5Ws9DqcQ/g4ej945ZO6NdRh0DW0RuHIEqYdFtjN11MKTB/i77XTe07Ckn28zMV2A9tXvUFk\
#                          0/oU+UbcOZu9cahXUCavpTQ7CNT7HE8nPuGMW3/cQWbSU=",
#                 "passwd": "JvrxC9U7kMN6FUUW+XHbRPyJigJ+3riqp2sccGrGocR8rVcIhXuQIZ4CNY53BpaKSi4sEh4jGGqIKz0lM1lTQoS40Smnv9Isyl2AaRZbdPZ0Ig+g9oNIcDO6ekF\
#                           r/s8hVSn+tk/OqRrmk7+5ClSBhDOs3PRuoP45fjm30OoJCAo="
#             }
#             # 获取登录参数
#
#             session_debug = requests.session()  # 创建session实例，维持会话,可以让我们在跨请求时保存某些参数
#             response = session_debug.post(login_url, parm, headers=headers)   # 发送post请求
#             print(response.cookies)
#
#             #self.log.debug('cookies: %s' % response.cookies.get_dict())
#             print(response.cookies.get_dict())
#             return response.cookies.get_dict()
#
#
#         elif env == "release":
#             login_url = 'http://' + self.config.loginHost_release
#             parm = self.config.loginInfo_release
#
#             session_release = requests.session()
#             response = session_release.post(login_url, eval(parm), headers=headers)
#             print(response.cookies)
#             #self.log.debug('cookies: %s' % response.cookies.get_dict())
#             return response.cookies.get_dict()
#
#         else:
#             print("get cookies error")
#             #self.log.error('get cookies error, please checkout!!!')
#
#
# if __name__ == '__main__':
#     ss = Session()
#     ss.get_session('debug')

import json
import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko)\
                          Chrome/67.0.3396.99 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded"
        }

login_url = 'https://' + 'upass.10jqka.com.cn/login?isIframe=1&main=3&pannel=1&source=sns&redir=https://t.10jqka.com.cn/static/loginBack.html'
parm = {
    "uname": "EUY6a0eRcQxbP31nZbr2rUl70/W6AgE0FhhBhJ8pxacl1dnjCpWbvCP5Ws9DqcQ/g4ej945ZO6NdRh0DW0RuHIEqYdFtjN11MKTB/i77XTe07Ckn28zMV2A9tXvUFk\
                         0/oU+UbcOZu9cahXUCavpTQ7CNT7HE8nPuGMW3/cQWbSU=",
    "passwd": "JvrxC9U7kMN6FUUW+XHbRPyJigJ+3riqp2sccGrGocR8rVcIhXuQIZ4CNY53BpaKSi4sEh4jGGqIKz0lM1lTQoS40Smnv9Isyl2AaRZbdPZ0Ig+g9oNIcDO6ekF\
                          r/s8hVSn+tk/OqRrmk7+5ClSBhDOs3PRuoP45fjm30OoJCAo="
}

session_debug = requests.session()  # 创建session实例，维持会话,可以让我们在跨请求时保存某些参数
response = session_debug.post(login_url, parm, headers=headers)   # 发送post请求
print(response.cookies)
cookies=response.cookies  # 获取登录cookie
jar=requests.cookies.RequestsCookieJar()
for k,v in cookies.items():
    jar.set(k,v)

#cookies='Hm_lvt_722143063e4892925903024537075d0d=1694488870,1695198616,1695261226,1695349448; Hm_lvt_929f8b362150b1f77b477230541dbbc2=1694488872,1695198616,1695278098,1695349449; hxmPid=med_video.tuijian.topicshow; u_ukey=A10702B8689642C6BE607730E11E6E4A; u_uver=1.0.0; u_dpass=5c5M6PPrQlQdqFWmmaV23Tk8OiemEjWRII8lr8KiOL7RJ0PW3SXoRGaWwvpDAZbR%2FsBAGfA5tlbuzYBqqcUNFA%3D%3D; u_did=8ACCBD7E42154A469A536BB8F0EAEF1B; u_ttype=WEB; user_status=0; PHPSESSID=86vkh29hl8v5k5tqeeg5tnag84; Hm_lvt_da7579fd91e2c6fa5aeb9d1620a9b333=1711700055,1712021799,1712026535,1712575895; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1711700055,1712021799,1712026535,1712575895; ttype=WEB; user=MDp4eWphNzE6Ok5vbmU6NTAwOjM3MTQxMjg1Nzo3LDExMTExMTExMTExLDQwOzQ0LDExLDQwOzYsMSw0MDs1LDEsNDA7MSwxMDEsNDA7MiwxLDQwOzMsMSw0MDs1LDEsNDA7OCwwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMSw0MDsxMDIsMSw0MDoyNDo6OjM2MTQxMjg1NzoxNzEyNTc3OTQ0Ojo6MTQ3ODY3OTA2MDo2MDQ4MDA6MDoxM2FiNmQ4ZjliM2EzNThmNWYxNDc5NDM5YTk4NGY1MjA6ZGVmYXVsdF80OjE%3D; userid=361412857; u_name=xyja71; escapename=xyja71; ticket=0dfc016d54920a13e31ee1dc399f93fc; utk=318933834c9c4d508cfa518951efc78d; Hm_lpvt_da7579fd91e2c6fa5aeb9d1620a9b333=1712577949; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1712577949; v=AyM6V3XjQRk4NA0tmC0XegEDsmzIGLda8az7jlWAfwL5lE0S3ehHqgF8i91m'
cookies_dict = requests.utils.dict_from_cookiejar(response.cookies)
print(cookies_dict)
# 使用utils.dict_from_cookiejar 将cookies数据类型转化为字典
#cookies_str = json.dumps(cookies_dict)
# 再使用 json.dumps 将字典转化为str字符串

url="http://t.10jqka.com.cn/portfolio/base/myPortfolioList"
response = requests.get(url=url, headers=headers, cookies=jar)
print(response.text)


# cookies_str='nh5rm5g5n6espqimudkitla258r3lqrm'
# cookies_dict = json.loads(cookies_str)
# # 使用json的loads函数，把str转化为字典。这里需要注意是loads，不是load
# cookies = requests.utils.cookiejar_from_dict(cookies_dict)
# # 再将字典恢复成原来的cookies
# session.cookies=cookies
# 可以拿去用啦
