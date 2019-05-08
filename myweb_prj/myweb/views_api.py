#!usr/bin/python3
# encoding: utf-8

"""
@author:dell
@file: views_api.py
@time: 2019/05/08
"""
from django.http import JsonResponse
from django.contrib.auth.forms import User

def get_users(request):
    users = User.objects.all()
    print(type(users))

    if len(users)==0:
        return JsonResponse({"status": 10011, "message": "用户不存在"})

    json_user = []
    for user in users:
        dict_user = {}
        dict_user["id"] = user.id
        dict_user["name"] = user.username
        dict_user["email"] = user.email
        json_user.append(dict_user)

    return JsonResponse({"status": 200, "message": "success", "data": json_user})
