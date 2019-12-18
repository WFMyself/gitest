# -*- coding: utf-8 -*-
# @Time    : 2019/12/18 23:55
# @Author  : Fei.Wang
# @Email   : 415892223@qq.com
# @File    : register_handle.py
# @Software: PyCharm

import time
from selenium import webdriver
from page_object_model.register_page import RegisterPage

"""上一层我们获取到注册页面中主要元素信息，接下来就该给这些元素进行数据上的操作处理（赋值）"""


class RegisterHandler(object):

    def __int__(self, driver):
        self.rp = RegisterPage(driver)

    # 输入邮箱号
    def input_email(self, email):
        self.rp.get_register_email().send_keys(email)

    # 输入用户名
    def input_username(self, username):
        self.rp.get_username().send_keys(username)

    # 输入密码
    def input_password(self, password):
        self.rp.get_password().send_keys(password)

    # 输入验证码
    def input_code_text(self, code_text):
        self.rp.get_code_text().send_keys(code_text)

    # 点击注册按钮
    def click_register_btn(self):
        self.rp.get_register_btn().click()


if __name__ == '__main__':
    register_url = 'http://www.5itest.cn/register'
    driver = webdriver.Chrome()
    driver.get(register_url)
    rh = RegisterHandler(driver)
    rh.input_email('123@163.com')
    rh.input_username('username')
    rh.input_password('123@16')
    rh.input_code_text('code')
    rh.click_register_btn()
    time.sleep(5)
    driver.close()
