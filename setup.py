#!/usr/bin/python
# coding=utf8

"""
@desc: 安装程序配置，基于setuptools
@author: Allen.Wu
@email: allenlikeu@gmail.com
@time: 2016-06-03
"""

import setuptools

# 配置项
setuptools.setup(
    setup_requires=['pbr'],
    pbr=True)
