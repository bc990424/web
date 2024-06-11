from django.shortcuts import render,redirect

def login(requset):
    return render(requset,'common/login.html')