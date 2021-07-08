from django.shortcuts import render
from thankyou import give_thanks
from django.http import HttpResponse

# Create your views here.
def hello(request):
    lala = 1
    return render(request, 'hello.html', {'thanks': give_thanks()})