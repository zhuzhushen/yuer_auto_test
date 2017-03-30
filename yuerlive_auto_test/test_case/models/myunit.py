# _*_  coding:utf-8 _*_
__author__ = '付康'
__date__ = '2017/3/29 16:30'

#初始化配置，测试用例中可以继承即可

from selenium import webdriver
from .driver import browser
import unittest
import os

class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = browser()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()