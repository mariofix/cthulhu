from django.shortcuts import render, redirect
from thankyou import give_thanks
from django.contrib.auth.views import LoginView 


def index(request):
    return redirect("/core/login")

def hello(request):
    return render(request, 'hello.html', {'thanks': give_thanks()})