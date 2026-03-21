# -*- coding: utf-8 -*-
# @Time    : 2018/8/1 下午2:54
# @Author  : WangJuan
# @File    : Shell.py

"""
封装执行shell语句方法

"""

import subprocess


class Shell:
    @staticmethod
    def invoke(cmd):
        # 该方法返回一个元组(stdout_data, stderr_data),包括执行命令的返回结果和执行错误信息
        output, errors = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        o = output.decode("utf-8")
        return o
