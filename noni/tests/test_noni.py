#!/usr/bin/python
# coding=utf8

"""
@desc: 测试入口
@author: Allen.Wu
@email: allenlikeu@gmail.com
@time: 2016-06-03
"""

# 将所有文件添加到此处，用于检测语法错误，依赖库缺失
from noni.base.constant import *
from noni.base.singleton import *
from noni.config.config_loader import *
from noni.logger.logger import *
from noni.tornado.handler.base_handler import *
from noni.tornado.http_client.http_client import *
from noni.tornado.timer.timer_manager import *

import nose
if __name__ == "__main__":
    nose.main()
