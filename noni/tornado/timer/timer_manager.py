#!/usr/bin/python
# coding=utf8

"""
@desc: 基于tornado封装定时器管理类，可以方便的使用定时器
@author: Allen.Wu
@email: allenlikeu@gmail.com
@time: 2016-06-03
"""

class TimerError(TypeError): pass
class TimerItemNotFoundError(TimerError): pass
class TimerAlreadyRunningError(TimerError): pass
class TimerRegisteParamError(TimerError): pass

import tornado.ioloop

from noni.base.singleton import Singleton
class TimerManager(object):
    """
    """
    __metaclass__ = Singleton

    def __init__(self):
        """
        """
        self.timer_list = {}

    def start_all(self):
        """
        启动所有定时器
        """
        for name, obj in self.timer_list.iteritems():
            if obj.is_running():
                continue
            obj.start()

    def stop_all(self):
        """
        关闭所有定时器
        """
        for name, obj in self.timer_list.iteritems():
            if obj.is_running():
                obj.stop()

    def start(self, name):
        """
        """
        obj = self.timer_list.get(name)
        if not obj:
            raise TimerItemNotFoundError, "timer: {0} not exist!".format(name)
        if obj.is_running():
            raise TimerAlreadyRunningError, "timer: {0} is already running".format(name)
        obj.start()

    def stop(self, name):
        """
        """
        obj = self.timer_list.get(name)
        if not obj:
            raise TimerItemNotFoundError, "timer: {0} not exist!".format(name)
        if obj.is_running():
            obj.stop()

    def registe(self, name, callback, inner_time):
        """
        注册定时器
        """
        if not name:
            raise TimerItemNotFoundError, "timer: {0} not exist!".format(name)
        if not callback:
            raise TimerRegisteParamError, "regist timer: {0} param callback error".format(name)
        if not inner_time:
            raise TimerRegisteParamError, "regist timer: {0} param inner_time error".format(name)
        self.timer_list[name] = tornado.ioloop.PeriodicCallback(callback, inner_time)

    def unregiste(self, name):
        """
        注销定时器
        """
        obj = self.timer_list.pop(name, None)
        if not obj:
            raise TimerItemNotFoundError, "timer: {0} not exist!".format(name)

        # 停止运行
        if obj.is_running:
            obj.stop()

    def reset(self):
        """
        停止所有定时器，并清空字典数据
        """
        self.stop_all()
        self.timer_list.clear()
