# URL conf
# 视图映射

from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.Ping, name='ping'),
    path('login/', views.Login, name='login'),
    path('service/<str:name>/login', views.LoginService, name='loginService'),
    path('service/<str:name>/do', views.DoService, name='doService'),
]