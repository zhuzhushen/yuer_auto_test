# _*_  coding:utf-8 _*_
__author__ = '付康'
__date__ = '2017/3/29 16:33'

from selenium import webdriver
import os

#截图函数
def insert_img(driver,file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\','/')
    base = base_dir.split('/test_case')[0]
    file_path = base + "/report/image/" + file_name
    driver.get_screenshot_as_file(file_path)

if __name__ == "__main__":
    driver = webdriver.Ie()
    driver.get("http://www.baidu.com")
    insert_img(driver,'baidu.jpg')
    driver.quit()