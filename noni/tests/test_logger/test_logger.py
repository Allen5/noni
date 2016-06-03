#!/usr/bin/python
# coding=utf8

"""
@desc: 测试Logger类
       测试用例：
       1. √ 是否为单例
       2. √ 加载配置文件。文件不存在时，是否抛出异常 LoggerConfigFileNotFoundError
       3. √ 加载配置文件。配置项不正确时，是否抛出异常 LoggerConfigFileFormatError
       4. √ 检测默认的 logger_name 是否为 "root"
@author: Allen.Wu
@email: allenlikeu@gmail.com
@time: 2016-06-03
"""

from noni.logger.logger import Logger
from noni.logger.logger import LoggerConfigFileFormatError
from noni.logger.logger import LoggerConfigFileNotFoundError

import unittest
class LoggerTestCase(unittest.TestCase):
    """
    """

    def setUp(self):
        """
        """
        self.logger_instant = Logger()

    def tearDown(self):
        """
        """

    def test_singleton(self):
        """
        """
        logger_instant_b = Logger()
        self.assertEqual(id(self.logger_instant), id(logger_instant_b))

    def test_setup_unexist_file(self):
        """
        """
        self.assertRaises(LoggerConfigFileNotFoundError, self.logger_instant.setup, "", None)
        self.assertRaises(LoggerConfigFileFormatError, self.logger_instant.setup, "./test_logger/a.conf", None)

    def test_setup_file_format(self):
        """
        """
        self.assertRaises(LoggerConfigFileFormatError, self.logger_instant.setup, "./test_logger/wrong_format.conf", None)

    def test_setup_default_logger_name(self):
        """
        """
        self.logger_instant.setup("./test_logger/test.conf", None)
        self.assertEqual("root", self.logger_instant.logger_name)

        self.logger_instant.setup("./test_logger/test.conf", "hello")
        self.assertEqual("hello", self.logger_instant.logger_name)
