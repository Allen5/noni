#!/usr/bin/python
# coding=utf8


"""
@desc: 基于tornado(version >= 4.0)封装http client
       提供异步非阻塞，同步，异步非阻塞（协程）三种接口
       要使用这三个接口，需要执行 ioloop.IOLoop.instance().start()在合适的地方
@author: Allen.Wu
@email: allenlikeu@gmail.com
@time: 2016-06-03
"""
import tornado.gen
from tornado.web import asynchronous
from tornado.httpclient import HTTPClient
from tornado.httpclient import AsyncHTTPClient

# 定义
HTTP_METHOD_GET = "GET"
HTTP_METHOD_POST = "POST"

class HttpClientError(TypeError): pass
class HttpClientMethodError(HttpClientError): pass
class HttpClientURLError(HttpClientError): pass
class HttpClientCallbackError(HttpClientError): pass
class HttpClientFetchError(HttpClientError): pass

from noni.base.singleton import Singleton
class HttpClient:
    """
    因为tornado.gen.coroutine不能装饰在类方法上，所以改为单例
    """
    __metaclass__ = Singleton

    def _pack_data(self, url, method, params):
        """
        """
        if not url:
            raise HttpClientURLError, "url wrong"
        if not method:
            raise HttpClientMethodError, "method wrong"

        # 无需整合
        if not params:
            return url, params

        if method == HTTP_METHOD_POST:
            import urllib
            params = urllib.encode(data)
        elif method == HTTP_METHOD_GET:
            from tornado.httputil import url_concat
            url = url_concat(url, params)
        return url, params

    def sync_fetch(self, url, method=HTTP_METHOD_GET, params=None):
        """
        """
        # 打包数据
        url, params = self._pack_data(url, method, params)

        http_client = HTTPClient()
        response = {}
        try:
            if method == const.GET:
                response = http_client.fetch(url, method)
            elif method == const.POST:
                response = http_client.fetch(url, method, body=body)
        except httpclient.HTTPError as error:
            raise HttpClientFetchError, str(error)
        except Exception as error:
            raise HttpClientFetchError, str(error)
        finally:
            http_client.close()

        if not response:
            return response
        return response.body

    def async_fetch(self, url, method=HTTP_METHOD_GET, params=None, callback=None):
        """
        """
        if not callback:
            raise HttpClientCallbackError, "callback is wrong"

        # 先打包数据
        url, params = self._pack_data(url, method, params)

        # 发起请求
        http_client = AsyncHTTPClient()
        if method == const.POST:
            http_client.fetch(url, request_timeout=3, callback=callback, body=params)
        elif method == const.GET:
            http_client.fetch(url, request_timeout=3, callback=callback)
        http_client.close()

    @asynchronous
    @tornado.gen.coroutine
    def coroutine_fetch(self, url, method=HTTP_METHOD_GET, params=None):
        """
        """
        # 打包数据
        url, params = self._pack_data(url, method, params)

        http_client = AsyncHTTPClient()
        response = {}
        if method == const.GET:
            response = yield http_client.fetch(url, method=method, request_timeout=3)
        elif method == const.POST:
            response = yield http_client.fetch(url, method=method, request_timeout=3, body=params)
        http_client.close()

        if not response:
            yield response
            return
        yield response.body
