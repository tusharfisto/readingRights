"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
import mysite.views

urlpatterns = [
    path('', mysite.views.index, name="index"),
    path('register', mysite.views.register, name="register"),
    path('signup',mysite.views.signup,name='signup'),
    path('login',mysite.views.login,name='login'),
    path('addGrocery', mysite.views.addgr,name="addgr"),
    path('updateGr',mysite.views.updateGr,name="updateGr"),
    path('delgr',mysite.views.delgr,name="delgr"),
    path('search',mysite.views.search,name="search"),
    path("logoff",mysite.views.search)
]
