#!/usr/bin/python
# coding=utf8

"""
@desc: 提供实现常量定义的类，基于这个类，可以定义常量，错误码。
       实现方式为通过监测 值更改异常，大小写异常来实现
@author: Allen.Wu
@email: allenlikeu@gmail.com
@time: 2016-06-03
"""

class ConstError(TypeError): pass
class ConstCaseError(ConstError): pass

class _const:
    """
    """
    def __setattr__(self, key, value):
        if self.__dict__.has_key(key):
            raise ConstError, "can't change const. {0}".format(key)
        if not key.isupper():
            raise ConstCaseError, "const name {0} should be in upper case".format(key)
        self.__dict__[key] = value

# e.g: 使用方法例子
# from constant import _const
# import sys
# sys.modules["const"] = _const()
# import const
# const.CONST_VALUE = 1
