from django.shortcuts import render, redirect
from thankyou import give_thanks
from django.contrib.auth.views import LoginView


def index(request):
    return redirect("/core/login")


def postlogin(request):
    # Verificamos si es primer login para ir a buscar su informacion a API
    return redirect("/core/dashboard")


def dashboard(request):
    # traemos toda la informacion adicional
    # crear clients ids y esas cosas
    return render(request, "core/dashboard.html")


def hello(request):
    return render(request, "hello.html", {"thanks": give_thanks()})
