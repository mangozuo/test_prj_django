#!usr/bin/python3
# encoding: utf-8

"""
@author:dell
@file: test_login.py
@time: 2019/05/23
"""
import unittest
from selenium import webdriver
import time
import os

class TestLogin(unittest.TestCase):
    def setUp(self):
        ce = "http://192.168.1.9:5555/wd/hub"
        dc_chrome = {
            "browserName": "chrome",
            "version": "",
            "platform": "ANY",
        }

        self.driver = webdriver.Remote(command_executor=ce,desired_capabilities=dc_chrome)

        # exe_path = os.path.join(os.getcwd(),"tools","chromedriver")
        # self.driver = webdriver.Chrome(executable_path=exe_path)

        self.driver.get("http://192.168.1.12:8008/login/")

    def test_login_1(self):
        self.driver.find_element_by_name("username").send_keys("testops")
        self.driver.find_element_by_name("password").send_keys("test123456")
        self.driver.find_element_by_id("btn").click()
        time.sleep(5)
        actText = self.driver.find_element_by_tag_name("body").text
        eptText = "Welcome to my WebSuite!"
        self.assertEqual(actText,eptText,"登录不成功或者登录后显示错误")

    def tearDown(self):
        time.sleep(3)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()


