#!/usr/bin/python
# coding=utf8

"""
@desc: 利用 __metaclass__ 实现单例类
       原理为：在类创建时（会调用__call__方法），检测是否已经存在该类，如果是，则返回当前实例。
       如果还未创建，则调用 type 的__call__方法，并传入参数完成创建。同时加入到字典中。
@author: Allen.Wu
@email: allenlikeu@gmail.com
@time: 2016-06-03
"""

class Singleton(type):
    """
    """

    _inst = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._inst:
            cls._inst[cls] = super(Singleton, cls).__call__(*args)
        return cls._inst[cls]

# e.g: 使用方法
# class Test(object):
#   __metaclass__ = Singleton
