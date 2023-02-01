# URL conf
# 视图映射

from django.urls import path
from . import views

urlpatterns = [
    path('ping/', views.ping, name='ping'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('service/<str:name>/login', views.loginService, name='loginService'),
    path('service/<str:name>/do', views.doService, name='doService'),
]