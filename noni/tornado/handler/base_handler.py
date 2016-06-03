#!/usr/bin/python
# coding=utf8

"""
@desc: 基于tornado的RequestHandler，封装参数获取的函数。
@author: Allen.Wu
@email: allenlikeu@gmail.com
@time: 2016-06-03
"""

class TornadoHandlerError(TypeError): pass
class TornadoHandlerParameterError(TornadoHandlerError): pass

import tornado.web

class BaseHandler(tornado.web.RequestHandler):
    """
    """

    def get_int_param(self, name):
        """
        """
        param = None
        try:
            param = int(self.get_argument(name))
        except ValueError as error:
            raise TornadoHandlerParameterError, str(error)
        except tornado.web.MissingArgumentError as error:
            raise TornadoHandlerParameterError, str(error)

        return param

    def get_str_param(self, name):
        """
        """
        param = None
        try:
            param = self.get_argument(name).strip()
            if param is None or param is [] or param is {}:
                raise TornadoHandlerParameterError, "param is wrong: {0} for : {1}".format(param, name)
        except tornado.web.MissingArgumentError as error:
            raise TornadoHandlerParameterError, str(error)

        return param

    def get_numeric_param(self, name):
        """
        """
        param = None
        try:
            param = self.get_argument(name).strip()
            if not param:
                raise TornadoHandlerParameterError, "param is wrong: {0} for : {1}".format(param, name)
            else:
                from decimal import Decimal
                param = Decimal(param)
        except ValueError as error:
            raise TornadoHandlerParameterError, str(error)
        except tornado.web.MissingArgumentError as error:
            raise TornadoHandlerParameterError, str(error)

        return param

    def get_file_param(self, name):
        """
        """
        data, filename = None, ""
        if not self.request.files or not self.request.files.has_key(name):
            raise TornadoHandlerParameterError, "no file posted for key: {0}".format(name)

        # TODO: 此处应当加异常检测
        data = self.request.files[name][0]
        filename = data.filename.encode("utf8")
        return data, filename

    def get_int_array_param(self, name):
        """
        """
        data = []
        if not self.request.arguments.has_key(name):
            raise TornadoHandlerParameterError, "no value for key: {0}".format(name)

        params = self.request.arguments[name]
        if not params:
            raise TornadoHandlerParameterError, "no value for key: {0}".format(name)

        try:
            for param in params:
                data.append(int(param))
        except ValueError as error:
            raise TornadoHandlerParameterError, str(error)

        return data
