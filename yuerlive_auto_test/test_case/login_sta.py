# _*_  coding:utf-8 _*_
__author__ = '付康'
__date__ = '2017/3/29 17:34'
#这个文件我们只用来编写测试用例
from time import sleep
import unittest,random,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit,function
from page_obj.loginPage import login

class loginTest(myunit.MyTest):

    def user_login_verify(self,username = "",password = ""):

        login(self.driver).user_login(username,password)


    def test_login1(self):
        self.user_login_verify(username="18258450696",password="123456")
        function.insert_img(self.driver, "user_true_2.jpg")

    def test_login2(self):
        self.user_login_verify(username="123456789",password="123456")
        function.insert_img(self.driver, "user_true_3.jpg")


if __name__=="__main__":
    unittest.main()