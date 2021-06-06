from django.urls import path
from django.urls.resolvers import URLPattern
from .import views

urlpatterns = [
    path('signup/', views.signup , name = 'signup'),
    path('signup/kakao', views.kakao_login , name = 'kakao_login'),
]
