#!/usr/bin/python
# coding=utf8

"""
@desc: 测试http_client中的三种获取数据（上传数据）接口是否可用
       1. √ 测试_pack_data. URL 为空时，是否抛出 HttpClientURLError。
       2. √ 测试_pack_data. method 为空时，是否抛出 HttpClientMethodError
       3. √ 测试sync_fetch。当URL错误时，是否抛出 HttpClientFetchError 异常
       4. √ 测试sync_fetch。当method错误时，是否抛出 HttpClientFetchError 异常
       5. √ 测试sync_fetch。当对方数据或服务出错时（超时），是否抛出 HttpClientFetchError 异常
       6. √ 测试sync_fetch。GET方式获取数据时，检测返回数据是否符合预期
       7. 测试sync_fetch。GET方式上传数据时，检测返回数据是否符合预期
       8. 测试sync_fetch。POST方式获取数据时，检测返回数据是否符合预期
       9. √ 测试sync_fetch。POST方式上传数据时，检测返回数据是否符合预期
       10. 测试async_fetch. GET方式获取数据时，检测返回数据是否符合预期
       11. 测试async_fetch. GET方式上传数据时，检测返回数据是否符合预期
       12. 测试async_fetch. POST方式获取数据时，检测返回数据是否符合预期
       13. 测试async_fetch. GET方式上传数据时，检测返回数据是否符合预期
       14. 测试coroutine_fetch. GET方式获取数据时，检测返回数据是否符合预期
       15. 测试coroutine_fetch. GET方式上传数据时，检测返回数据是否符合预期
       16. 测试coroutine_fetch. POST方式获取数据时，检测返回数据是否符合预期
       17. 测试coroutine_fetch. POST方式上传数据时，检测返回数据是否符合预期
@author: Allen.Wu
@email: allenlikeu@gmail.com
@time: 2016-06-06
"""

def async_fetch_resp(response):
    """
    """
    print "hehehehh"

def async_upload_resp(response):
    """
    """
    print "hehehhe"
    assertEqual(response, "")

import unittest
from noni.base.singleton import Singleton
from noni.tornado.http_client.http_client import HttpClient
from noni.tornado.http_client.http_client import HttpClientURLError
from noni.tornado.http_client.http_client import HttpClientMethodError
from noni.tornado.http_client.http_client import HttpClientFetchError
class HttpClientTestCase(unittest.TestCase):
    """
    """
    def setUp(self):
        """
        """
        self.url = "http://10.11.5.145:28082/monitor/sql.transaction.count"
        self.method = "GET"
        self.http_client = HttpClient()

    def test_pack_data_empty_url(self):
        """
        """
        self.assertRaises(HttpClientURLError, self.http_client.sync_fetch, "")

    def test_pack_data_empty_method(self):
        """
        """
        self.assertRaises(HttpClientMethodError, self.http_client.sync_fetch, self.url, "")

    def test_sync_wrong_url(self):
        """
        """
        resp = self.http_client.sync_fetch(self.url + "/asdasdsa")
        self.assertEqual(resp, "")

    def test_sync_wrong_method(self):
        """
        """
        self.assertRaises(HttpClientFetchError, self.http_client.sync_fetch, self.url, self.method+"xxx")

    def test_sync_fetch_data_with_get(self):
        """
        """
        resp = self.http_client.sync_fetch(self.url)
        self.assertEqual(resp, "{\"value\":0}")

    def test_sync_fetch_data_with_post(self):
        """
        """
        #TODO:

    def test_sync_upload_data_with_get(self):
        """
        """
        #TODO:

    def test_sync_upload_data_with_post(self):
        """
        """
        data = {
            "name": "李四2",
            "email": "test@test1.com",
            "message": "asdasdsad"
        }
        resp = self.http_client.sync_fetch("http://121.41.73.118/api/feedback/add", "POST", data)
        self.assertEqual(resp, "{\"data\": \"\", \"result\": 0}")

    def async_resp(self, response):
        """
        """
        self.assertRaises(response, "")

    def test_async_fetch_data_with_get(self):
        """
        """
        self.http_client.async_fetch("http://www.baidu.com", callback=async_fetch_resp)

    def test_async_fetch_data_with_post(self):
        """
        """
        #TODO

    def test_async_upload_data_with_get(self):
        """
        """
        data = {
            "name": "张四2",
            "email": "te11st@test1.com",
            "message": "asdasdsad"
        }
        resp = self.http_client.async_fetch("http://121.41.73.118/api/feedback/add", "POST", data, callback=async_upload_resp)

    def test_async_upload_data_with_post(self):
        """
        """
        data = {
            "name": "张四2",
            "email": "te11st@test1.com",
            "message": "asdasdsad"
        }
        resp = self.http_client.async_fetch("http://121.41.73.118/api/feedback/add", "POST", data, callback=async_upload_resp)

    def test_coroutine_fetch_data_with_get(self):
        """
        """
        resp = self.http_client.coroutine_fetch(self.url)
        self.assertEqual(resp, "")
