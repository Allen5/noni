#!/usr/bin/python
# coding=utf8

"""
@desc: 测试单例类。
       测试逻辑：先定义一个单例类，创建两个实例，比较两个实例的id是否相等
@author: Allen.Wu
@email: allenlikeu@gmail.com
@time: 2016-06-03
"""
import unittest

from noni.base.singleton import Singleton
class TestClassA(object):
    __metaclass__ = Singleton

class SingletonTestCase(unittest.TestCase):
    """
    """

    def setUp(self):
        self.test_inst_a = TestClassA()
        self.test_inst_b = TestClassA()

    def tearDown(self):
        """
        """

    def test_equal(self):
        """
        """
        self.assertEqual(id(self.test_inst_a), id(self.test_inst_b))
