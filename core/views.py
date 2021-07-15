from django.shortcuts import render, redirect
from thankyou import give_thanks
from django.contrib.auth.views import LoginView
from .forms import CoreUserCreationForm


def index(request):
    return redirect("/core/login")


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
    return redirect("/core/dashboard")

def postlogout(request):
    # Hacer algo despues?
    return redirect("/")

def dashboard(request):
    # traemos toda la informacion adicional
    # crear clients ids y esas cosas
    return render(request, "core/dashboard.html")


def hello(request):
    return render(request, "hello.html", {"thanks": give_thanks()})
