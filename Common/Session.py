# -*- coding: utf-8 -*-
# @Time    : 2018/7/24 下午3:33
# @Author  : WangJuan
# @File    : Session.py

"""
封装获取cookie方法

"""

import requests

from Common import Log
from Conf import Config


class Session:
    def __init__(self):
        self.config = Config.Config()
        self.log = Log.MyLog()

    def get_session(self, env):
        """
        获取session
        :param env: 环境变量
        :return:
        """
        # 设置请求头
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko)\
                          Chrome/67.0.3396.99 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        if env == "debug":

            # 下面的代码是获取登录cookie，这里我直接粘贴cookie过来
            # login_url = 'https://' + self.config.loginHost_debug
            # parm = self.config.loginInfo_debug  # 获取登录参数
            #
            session_debug = requests.session()  # 创建session实例，维持会话,可以让我们在跨请求时保存某些参数
            # response = session_debug.post(login_url, eval(parm), headers=headers)   # 发送post请求
            # #print(response.cookies)
            # self.log.debug('cookies: %s' % response.cookies.get_dict())
            # return response.cookies.get_dict()

            cookies ='v=AxvjVBrX-dLHIQUmHZJjft0RrnWA8C_yKQTzpg1Y95ox7DRqlcC_QjnUg_Qe; Hm_lpvt_78c58f01938e4d85eaf619eae71b4ed1=1718624352; Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1=1716793678,1716810172,1718108093,1718624352; Hm_lpvt_da7579fd91e2c6fa5aeb9d1620a9b333=1718624351; Hm_lvt_da7579fd91e2c6fa5aeb9d1620a9b333=1716793678,1716810172,1718108093,1718624351; escapename=xyja71; ticket=8a004d0131e386b4088ff3510a58be78; u_name=xyja71; user=MDp4eWphNzE6Ok5vbmU6NTAwOjM3MTQxMjg1Nzo3LDExMTExMTExMTExLDQwOzQ0LDExLDQwOzYsMSw0MDs1LDEsNDA7MSwxMDEsNDA7MiwxLDQwOzMsMSw0MDs1LDEsNDA7OCwwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMSw0MDsxMDIsMSw0MDoyNDo6OjM2MTQxMjg1NzoxNzE2NTIwMDQ3Ojo6MTQ3ODY3OTA2MDoyNjc4NDAwOjA6MWVlMzI2OGI4ZTA0NzY0ZjliZWU0MTUzOTA2ZTAwMTAzOjox; user_status=0; userid=361412857'
            cookies = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookies.split(";")}
            return cookies

        elif env == "release":
            login_url = 'https://' + self.config.loginHost_release
            parm = self.config.loginInfo_release

            session_release = requests.session()
            response = session_release.post(login_url, eval(parm), headers=headers)
            #print(response.cookies)
            self.log.debug('cookies: %s' % response.cookies.get_dict())
            return response.cookies.get_dict()

        else:
            print("get cookies error")
            self.log.error('get cookies error, please checkout!!!')


# if __name__ == '__main__':
#     ss = Session()
#     ss.get_session('debug')