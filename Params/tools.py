# -*- coding: utf-8 -*-
# @Time    : 2018/7/31 上午10:56
# @Author  : WangJuan
# @File    : tools.py

"""
读取yaml测试数据

"""

import yaml
import os
import os.path


def parse():
    path_ya = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))) + '/Params/Param'
    pages = {}
    for root, dirs, files in os.walk(path_ya):
        # os.walk用来遍历path_ya文件夹的地址，返回一个生成器(generator)
        #root指的是当前正在遍历的这个文件夹的本身的地址
        #dirs返回的是一个列表list，表中数据是该文件夹中所有的目录的名称(但不包括子目录名称)
        #files返回的也是一个列表list, 表中数据是该文件夹中所有的文件名称(但不包括子目录名称)

        for name in files:
            watch_file_path = os.path.join(root, name)
            with open(watch_file_path, 'r',encoding='UTF-8') as f:
                page = yaml.safe_load(f)
                # safe_load用于安全地解析 YAML 文档，不会处理 YAML 文档中的所有数据，包括 Python 对象和函数等。load会
                # page是一个字典对象,update操作相当于将page中的数据更新复制到pages中
                pages.update(page)
        return pages


class GetPages:
    @staticmethod
    def get_page_list():
        _page_list = {}
        pages = parse()
        for page, value in pages.items():
            parameters = value['parameters']
            data_list = []

            for parameter in parameters:
                data_list.append(parameter)
            _page_list[page] = data_list

        return _page_list


if __name__ == '__main__':
    lists = GetPages.get_page_list()
