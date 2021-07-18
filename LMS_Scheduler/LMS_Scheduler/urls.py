"""LMS_Scheduler URL Configuration

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
from django.urls import path, include
import account.views
import lms.views
urlpatterns = [
    path('', account.views.mainLogin,name="mainLogin"),
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('lms/', include('lms.urls')),
    path('home/', lms.views.home, name = "home"),
    path('',account.views.logout,name="logout"), # 초기화면 때문에 include 처리 안함


]