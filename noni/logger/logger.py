#!/usr/bin/python
# coding=utf8

"""
@desc: 简化logging的配置步骤。提供加载配置文件的接口用与配置日志格式。
       TODO: 提供字典等方式进行配置
@author: Allen.Wu
@email: allenlikeu@gmail.com
@time: 2016-06-03
"""
import logging
import logging.config

class LoggerError(TypeError): pass
class LoggerConfigFileNotFoundError(LoggerError): pass
class LoggerConfigFileFormatError(LoggerError): pass
class LoggerQualnameNotExistError(LoggerError): pass

from noni.base.singleton import Singleton
class Logger(object):
    """
    """

    __metaclass__ = Singleton

    def __init__(self):
        """
        """
        self.logger_name = "root" # 默认使用root

    def setup(self, filename, logger_name=None):
        """
        """
        if not filename:
            raise LoggerConfigFileNotFoundError, "can't find config file:{0}".format(filename)

        import ConfigParser
        try:
            logging.config.fileConfig(filename)
        except ConfigParser.NoSectionError as error:
            raise LoggerConfigFileFormatError, str(error)
        except ConfigParser.ParsingError as error:
            raise LoggerConfigFileFormatError, str(error)

        # 指定初始logger名称
        if logger_name:
            self.logger_name = logger_name

    def get_logger(self, logger_name=None):
        """
        """
        logger = None
        if not logger_name:
            logger = logging.getLogger(self.logger_name)
        else:
            logger = logging.getLogger(logger_name)
        print logger
        return logger
