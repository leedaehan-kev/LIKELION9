from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.


def oauth(request):
    code = request.GET['code']
    print("code = ", str(code))
    return render(request, 'home.html')

def kakao_login(request):
    login_request_uri = 'https://kauth.kakao.com/oauth/authorize?'
    client_id = 'f73eac580e0bc9a9152e0eaedda3100a'
    redirect_uri = 'http://127.0.0.1:8000/oauth'

    login_request_uri += 'client_id=' + client_id
    login_request_uri += '&redirect_uri=' + redirect_uri
    login_request_uri += '&response_type=code'
    
    return redirect(login_request_uri)


def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/home')
        else:
            return render(request,'login.html',{'error':"사용자 이름 혹은 패스워드가 일치하지 않습니다"})
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def signup(request):
    return render(request,'signup.html')

def idsignuppage(request):
    return render(request, 'IDsignup.html')

def IDsignup(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request,'IDsignup.html',{'error':"이미 존재하는 사용자입니다."})
        if password==request.POST['passwordCheck']:
            user=User.objects.create_user(
                username,password=password
            )
            auth.login(request,user)
            return render(request,'home.html')
        else :
            return render(request,'IDsignup.html',{'error':"비밀번호 확인이 일치하지 않습니다"})
    else:
        return render(request,'IDsignup.html')


def manuallogin(request):
    return render(request,'idLogin.html')