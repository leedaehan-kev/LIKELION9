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
    path('admin/', admin.site.urls),
    path('home/', lms.views.home, name = "home"),
    path('',account.views.login,name="login"),
    path('login/',account.views.manuallogin,name="manuallogin"),
    path('signup/',account.views.signup,name="signup"),
    path('signup/kakao', account.views.kakao_signup, name="kakao_signup"),
    path('signup/IDsignup',account.views.idSignup,name="idSignup"),
    path('signup/lmsSignup',account.views.lmsSignup,name="lmsSignup"),
    path('account/', include('account.urls')),
    path('oauth/', account.views.oauth, name="oauth"),
    path('kakaologin/', account.views.kakoredirect, name="kakaologin"),
    path('calendar/', account.views.calendar, name = "calendar"),
]