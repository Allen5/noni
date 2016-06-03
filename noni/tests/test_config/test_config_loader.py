#!/usr/bin/python
# coding=utf8

"""
@desc: 测试文件加载
       测试用例：
       1. √ json文件加载。文件不存在，是否抛ConfigFileNotFoundError异常
       2. √ json文件加载。文件内容为空，是否抛ConfigFileFormatError异常
       3. √ json文件加载。内容格式不符合json，是否抛ConfigFileFormatError异常
       4. √ json文件加载。带上env节点，内容中不含env时，是否抛ConfigFileNotContainedItemError异常
       5. √ json文件加载。带上env节点，取值是否符合预期。
@author: Allen.Wu
@email: allenlikeu@gmail.com
@time: 2016-06-03
"""

import unittest
from noni.config.config_loader import JsonConfigLoader

from noni.config.config_loader import ConfigFileNotFoundError
from noni.config.config_loader import ConfigFileFormatError
from noni.config.config_loader import ConfigFileNotContainedItemError

class JsonConfigLoaderTestCase(unittest.TestCase):
    """
    """

    def setUp(self):
        self.loader = JsonConfigLoader()

    def test_load_unexist_file(self):
        """
        """
        self.assertRaises(ConfigFileNotFoundError, self.loader.load, "./test_config/a.json", None)

    def test_load_empty_file(self):
        """
        """
        self.assertRaises(ConfigFileFormatError, self.loader.load, "./test_config/empty.json", None)

    def test_load_wformat_file(self):
        """
        """
        self.assertRaises(ConfigFileFormatError, self.loader.load, "./test_config/wrong_format.json", None)

    def test_load_file_with_unexist_env(self):
        """
        """
        self.assertRaises(ConfigFileNotContainedItemError, self.loader.load, "./test_config/test.json", "c")

    def test_load_file_value_equal(self):
        """
        """
        value = self.loader.load("./test_config/test.json", "a")
        self.assertEqual(111, value)
        value = self.loader.load("./test_config/test.json", "b")
        self.assertNotEqual(111, value)
