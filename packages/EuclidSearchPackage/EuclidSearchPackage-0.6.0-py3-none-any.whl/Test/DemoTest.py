# -*- coding: utf-8 -*-
# @Time    : 2023/3/28 16:39
# @Author  : Euclid-Jie
# @File    : DemoTest.py
import src.EuclidSearchPackage as ESP
ESP.Set_cookie('cookie.txt')
timeBegin = '2023-03-01-0'
timeEnd = '2023-03-10-0'
demoClass = ESP.WeiboClassV1(Mongo=False)
demoClass.main_get(['北师大', '珠海'], timeBegin, timeEnd)
