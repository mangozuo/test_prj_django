#!usr/bin/python3
# encoding: utf-8

"""
@author:dell
@file: run_test.py
@time: 2019/05/23
"""
import os
import unittest


if __name__ == '__main__':
    case_path = os.path.join(os.getcwd(),"testCase")
    print(case_path)
    suite = unittest.defaultTestLoader.discover(case_path,pattern="test_*.py")

    unittest.TextTestRunner().run(suite)

