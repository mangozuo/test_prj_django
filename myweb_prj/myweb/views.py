from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import auth

# Create your views here.

def main(request):
    return HttpResponse("Welcome to my WebSuite!")

def login(request):
    return render(request, 'login.html')

def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            response = HttpResponseRedirect("/main/")
            # request.session["username"] = username
            return response
        else:
            return render(request, 'login.html', {"error": "用户名或者密码错误！"})
