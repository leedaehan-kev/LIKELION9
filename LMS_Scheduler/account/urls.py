from django.urls import path
from django.urls.resolvers import URLPattern
from .import views

from django.contrib import admin


urlpatterns = [
    path('signup/', views.signup , name = 'signup'),
    path('login/kakao_login', views.kakao_login , name = 'kakao_login'),
    path('',views.manuallogin,name="manuallogin"),
    path('signup/kakao', views.kakao_signup, name="kakao_signup"),
    path('signup/IDsignup',views.idSignup,name="idSignup"),
    path('signup/lmsSignup',views.lmsSignup,name="lmsSignup"),
    path('oauth/', views.oauth, name="oauth"),
    path('kakaologin/', views.kakoredirect, name="kakaologin"),
    path('calendar/', views.calendar, name = "calendar"),
    path('mypage/',views.mypage,name="mypage"),


]