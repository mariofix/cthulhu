from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views
from django.contrib.auth.views import LoginView 

# URLConf
urlpatterns = [
    path('', views.index, name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('hello/', views.hello, name="hello_world"),
    path('postlogin/', views.hello, name="postlogin"),
    path('create_account/', views.hello, name="create_account"),
    path('', include('django.contrib.auth.urls'))
]