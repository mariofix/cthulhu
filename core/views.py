from django.shortcuts import render, redirect
from thankyou import give_thanks
from django.contrib.auth.views import LoginView
from .forms import CoreUserCreationForm
from .models import CoreUser


def index(request):
    return redirect("/login")


def registro(request):
    
    if request.method == 'POST':
        form = CoreUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, 'registration/post_register.html')
    else:
        form = CoreUserCreationForm()
    datos = {'form': form}
    return render(request, 'registration/register.html', datos)


def postlogin(request):
    # Verificamos si es primer login para ir a buscar su informacion a API
    if request.user != 'AnonymousUser':
        print(request.user.email)
        print(request.user.is_active)
        return redirect("/dashboard")
    else:
        return redirect("/login")

def postlogout(request):
    # Hacer algo despues?
    return redirect("/")

def dashboard(request):
    # traemos toda la informacion adicional
    # crear clients ids y esas cosas
    if request.user != 'AnonymousUser':
        print(request.user.email)
        print(request.user.is_active)
    return render(request, "core/dashboard.html")

def profile(request):
    return render(request, "core/profile.html")

def help(request):
    return render(request, "core/help.html")

def hello(request):
    return render(request, "hello.html", {"thanks": give_thanks()})
