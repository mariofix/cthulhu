from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
from django.contrib.auth.views import LoginView 

# URLConf
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('hello/', views.hello, name="helloworld")
]