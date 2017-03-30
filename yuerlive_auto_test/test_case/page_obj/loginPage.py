# _*_  coding:utf-8 _*_
__author__ = '付康'
__date__ = '2017/3/29 17:03'

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep


#登录对象：包含所有的登录必要的元素。其实就是封装了登录时候必要的一些元素定位。我这里把每个输入框，每个按钮都看作是一个对象
#其他的对象，可以新建文件进行封装，如注册对象，发起直播对象，评论对象，关注主播对象，送礼物对象等等

class login(Page):
    '''
    用户登录
    '''
    url = '/'

    #Action
    login_get_loc = (By.XPATH,"html/body/div[1]/div/div[2]/a[1]")
    login_username_loc = (By.XPATH,"html/body/div[2]/div/input[1]")
    login_password_loc = (By.XPATH,"html/body/div[2]/div/input[2]")
    login_button_loc = (By.XPATH,"html/body/div[2]/div/button")

    #点击登录进入页面
    def login_get(self):
        self.find_element(*self.login_get_loc).click()
        sleep(1)

    #登录用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).send_keys(username)

    #登录密码
    def login_password(self,password):
        self.find_element(*self.login_password_loc).send_keys(password)

    #登录按钮
    def login_button(self):
        self.find_element(*self.login_button_loc).click()

    #定义统一登录接口
    def user_login(self,username = "18258450696",password = "123456"):
        self.open()
        sleep(2)
        self.login_get()
        self.login_username(username)
        self.login_password(password)
        self.login_button()
        sleep(1)
