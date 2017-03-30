# _*_  coding:utf-8 _*_
__author__ = '付康'
__date__ = '2017/3/29 14:36'

from selenium.webdriver import Remote
from selenium import webdriver

#启动浏览器
def browser():
    host = '172.16.2.18:4444' #运行主机：端口号
    #这里可以参数化配置
    driver = Remote(command_executor='http://'+host+'/wd/hub',
                    desired_capabilities={
                        'platform':'ANY',
                        'browserName':'firefox',
                        'version':'',
                        'javascriptEnabled':True
                    }
                   )
    return driver

# if __name__ == '__main__':
#     dr = browser()
#     dr.get('http://www.baidu.com')
#     dr.quit()