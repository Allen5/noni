#!/usr/bin/python
# coding=utf8

"""
@desc: 测试常量类是否能够正常工作。测试基于nose框架。
       测试用例包含：
       1. √ 定义常量后更改值，是否抛出 ConstError
       2. √ 定义常量后值是否相等
       3. √ 非全大写变量是否可以定义为常量（是否抛出 ConstCaseError ）
@author: Allen.Wu
@email: allenlikeu@gmail.com
@time: 2016-06-03
"""

import unittest

from noni.base.constant import ConstError
from noni.base.constant import ConstCaseError
from noni.base.constant import _const

import sys
sys.modules["const"] = _const()
import const
const.TEST_VALUE_A = 1

class ConstantValueTestCase(unittest.TestCase):
    """
    """
    def assign(self, val):
        """
        """
        const.TEST_VALUE_A = val

    def test_equal(self):
        """
        """
        self.assertEqual(const.TEST_VALUE_A, 1)

    def test_assign(self):
        """
        """
        self.assertRaises(ConstError, self.assign, 2)

    def add_const(self, val):
        """
        """
        const.TEST_VALUE_b = val

    def test_nonupper(self):
        """
        """
        self.assertRaises(ConstCaseError, self.add_const, 3)
