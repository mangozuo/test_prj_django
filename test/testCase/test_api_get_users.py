#!usr/bin/python3
# encoding: utf-8

"""
@author:dell
@file: test_api_get_users.py
@time: 2019/05/24
"""
import unittest
import requests

class TestGetUsers(unittest.TestCase):
    def setUp(self):
        pass

    def test_get_users_1(self):
        response = requests.get("http://192.168.1.12:8008/api/get_users/")

        code = response.status_code

        self.assertEqual(code,200,"请求失败")
        print(response.json())

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()

