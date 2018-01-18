# -*- coding:utf-8 -*-
# @Time   : 2018/1/18 18:55
import re


class HandleString():
    """
    """

    def __init__(self):
        pass

    @staticmethod
    def vaild_id(id_):
        """
        :param name: 无人机ID
        :return: True 是由数字和字母组成的合法序列
        """
        pattern = re.compile("[\w]*")
        match = pattern.match(id_)
        return True if match is not None else False

    @staticmethod
    def str2int(list_):
        """
        :param str:坐标字符串
        :return:True 合法的坐标
        """
        for i in range(len(list_)):
            try:
                int(list_[i])
            except ValueError as e:
                return None
            else:
                list_[i] = int(list_[i])
        return list_

    @staticmethod
    def split_str(str_):
        """
        :param str: 待分割的字符串，利用空格做分隔符
        :return: 返回一个字符串列表
        """
        return str_.split(" ")
