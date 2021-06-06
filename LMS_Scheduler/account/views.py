from django.shortcuts import render, redirect

# Create your views here.
def signup(request):
    return render(request, 'signup.html')

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


