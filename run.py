# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 上午10:42
# @Author  : WangJuan
# @File    : run.py

"""
运行用例集：
    python3 run.py

# '--allure_severities=critical, blocker'
# '--allure_stories=测试模块_demo1, 测试模块_demo2'
# '--allure_features=测试features'

"""

import pytest

from Common import Log
from Common import Shell
from Conf import Config
from Common import Email

if __name__ == '__main__':
    conf = Config.Config()
    log = Log.MyLog()
    log.info('初始化配置文件, path=' + conf.conf_path)

    shell = Shell.Shell()
    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path

    # 定义测试集，执行测试用例
    # --alluredir 在指定目录生成allure报告
    args = ['-s', '-q', '--alluredir', xml_report_path,'--clean-alluredir']
    pytest.main(args)

    # 将临时的xml文件生成为html文件，在后面的目录下创建allure-report目录，存放报告
    # 加上-c/--clear  代表删除allure报告生成的目录
    cmd = 'allure generate %s -o %s -c' % (xml_report_path, html_report_path)

    try:
        shell.invoke(cmd)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise

    try:
        mail = Email.SendMail()
        mail.sendMail()
    except Exception as e:
        log.error('发送邮件失败，请检查邮件配置')
        raise

