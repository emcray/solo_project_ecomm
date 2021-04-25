from django.urls import path
from . import views

urlpatterns=[
    path('', views.home),
    path('login_page', views.login_page),
    path('register', views.register),
    path('login', views.login),
    path('success', views.success),
]