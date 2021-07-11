from django.urls import path, include
from django.urls.resolvers import URLPattern
from . import views
from django.contrib.auth.views import LoginView 
from django.conf.urls import handler400,handler403,handler404,handler500

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', LoginView.as_view(), name="login"),
    path('hello/', views.hello, name="hello_world"),
    path('postlogin/', views.postlogin, name="postlogin"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('create_account/', views.hello, name="create_account"),
    path('', include('django.contrib.auth.urls'))
]

handler400 = 'core.errorviews.handle400'
handler403 = 'core.errorviews.handle403'
handler404 = 'core.errorviews.handle404'
handler500 = 'core.errorviews.handle500'