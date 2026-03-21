# -*- coding: utf-8 -*-
# @Time    : 2018/8/21 下午10:14
# @Author  : WangJuan
# @File    : Assert.py


"""
封装Assert方法

"""
from Common import Log
from Common import Consts
import json


class Assertions:
    def __init__(self):
        self.log = Log.MyLog()

    def assert_code(self, code, expected_code):
        """
        验证response状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert code == expected_code
            return True
        except:
            self.log.error("statusCode error, expected_code is %s, statusCode is %s " % (expected_code, code))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_body(self, body, body_msg, expected_msg):
        """
        验证response body中任意属性的值
        :param body:
        :param body_msg:
        :param expected_msg:
        :return:
        """
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            return True

        except:
            self.log.error("Response body msg != expected_msg, expected_msg is %s, body_msg is %s" % (expected_msg, body_msg))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_in_text(self, body, expected_msg):
        """
        验证response body中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body, ensure_ascii=False)
            # print(text)
            assert expected_msg in text
            return True

        except:
            self.log.error("Response body Does not contain expected_msg, expected_msg is %s" % expected_msg)
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_text(self, body, expected_msg):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            return True

        except:
            self.log.error("Response body != expected_msg, expected_msg is %s, body is %s" % (expected_msg, body))
            Consts.RESULT_LIST.append('fail')

            raise


    def assert_not_text(self, body, expected_msg):
        """
        验证response body中是否不等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body != expected_msg
            return True

        except:
            self.log.error("Response body != expected_msg, expected_msg is %s, body is %s" % (expected_msg, body))
            Consts.RESULT_LIST.append('fail')

            raise


    def assert_length_atleast(self, body, expected_length):
        """
        验证response body中返回的数据条数是否大于等于预期的数据条数
        :param body: 请求返回体中的数据，假定为列表形式
        :param expected_length:预期的数据条数
        :return: 如果数据条数大于等于预期，则返回True；否则记录错误并抛出异常
        """
        try:
            # 确保body是列表类型，如果不是，尝试将其转换为列表
            if not isinstance(body, list):
                body = [body]  # 如果body不是列表，将其放入列表中以计算条数

            # 计算body中的数据条数
            actual_length = len(body)
            assert actual_length >= expected_length
            return True

        except:
            self.log.error("Response data count is less than expected_count, expected_count is %s, actual_count is %s" % (expected_length, actual_length))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_time(self, time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            return True

        except:
            self.log.error("Response time > expected_time, expected_time is %s, time is %s" % (expected_time, time))
            Consts.RESULT_LIST.append('fail')

            raise


