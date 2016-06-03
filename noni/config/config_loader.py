#!/usr/bin/python
# coding=utf8

"""
@desc: 实现json文件加载，可简单的获取项
       单例模式存在，数据可全局保存
@author: Allen.Wu
@email: allenlikeu@gmail.com
@time: 2016-06-03
"""

# 定义异常信息
class ConfigFileError(TypeError): pass
class ConfigFileNotFoundError(ConfigFileError): pass
class ConfigFileFormatError(ConfigFileError): pass
class ConfigFileNotContainedItemError(ConfigFileError): pass

# 定义json加载类
class JsonConfigLoader(object):
    """
    加载json配置文件
    """

    def load(self, filename, env=None):
        """
        @param: filename 配置文件名
        @param: env [development|production] 用于区分开发环境
        @return: 加载后的数据
        """
        self.__dict__ = {}
        if not filename:
            raise ConfigFileNotFoundError, "can't find config file: {0}".format(filename)

        import json
        try:
            with open(filename, 'r') as file:
                self.__dict__ = json.load(file)
        except IOError as error:
            raise ConfigFileNotFoundError, str(error)
        except ValueError as error:
            raise ConfigFileFormatError, str(error)

        if not self.__dict__:
            raise ConfigFileFormatError, "config file[{0}] is empty or format error".format(filename)

        # 根据环境切换信息
        if env:
            if not self.__dict__.has_key(env):
                raise ConfigFileNotContainedItemError, "config file[{0}] does not contain node[{1}]".format(
                    filename,
                    env)
            return self.__dict__[env]
        return self.__dict__
