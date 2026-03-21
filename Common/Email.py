# -*- coding: utf-8 -*-
# @Time    : 2018/7/19 下午5:23
# @Author  : WangJuan
# @File    : Email.py

"""
封装发送邮件的方法
email*库用于构建邮件发送的内容，包括主题，文字内容，图片，html，附件等
"""
import smtplib
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from Common import Consts
from Common import Log
from Conf.Config import Config


class SendMail:

    def __init__(self):
        self.config = Config()
        self.log = Log.MyLog()

    def sendMail(self):
        # 创建邮件内容对象
        msg = MIMEMultipart()
        # body = """
        # <h3>Hi，all</h3>
        # <p>本次接口自动化测试报告如下。</p>
        # """
        # mail_body = MIMEText(body, _subtype='html', _charset='utf-8')
        stress_body = Consts.STRESS_LIST
        result_body = Consts.RESULT_LIST
        body2 = 'Hi，all\n本次接口自动化测试报告如下：\n   接口响应时间集：%s\n   接口运行结果集：%s' % (stress_body, result_body)
        # 邮件的文字内容
        # 内容：就是文字字符串
        # 类型：plain(简单的文字内容)、html(超文本)
        mail_body2 = MIMEText(body2, _subtype='plain', _charset='utf-8')
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

        # 设置邮件主题对象
        sub=Header("接口自动化测试报告"+"_"+tm, 'utf-8')
        msg['Subject'] = sub

        # 设置邮件发送者
        msg['From'] = self.config.sender

        # 设置邮件接收者
        receivers = self.config.receiver
        toclause = receivers.split(',')
        msg['To'] = ",".join(toclause)
        # msg.attach(mail_body)

        # 将邮件文字对象添加到邮件对象
        msg.attach(mail_body2)

        try:
            # 连接邮箱服务器
            # smtp = smtplib.SMTP()
            # smtp.connect(self.config.smtpserver)
            #smtp_srv = self.config.smtpserver
            smtp = smtplib.SMTP_SSL(self.config.smtpserver.encode(), 465)
            # 登录邮箱
            smtp.login(self.config.username, self.config.password)

            # 发送邮件
            smtp.sendmail(self.config.sender, toclause, msg.as_string())
        except Exception as e:
            print(e)
            print("发送失败")
            self.log.error("邮件发送失败，请检查邮件配置")

        else:
            print("发送成功")
            self.log.info("邮件发送成功")
        finally:
            smtp.quit()
