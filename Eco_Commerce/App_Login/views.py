from django.shortcuts import render,HttpResponseRedirect
# Create your views here.
from django.urls import reverse 
from django.http import HttpResponse
# Authentication
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate
# form and model
from App_Login.models import Profile
from App_Login.forms import ProfileForm, SignUpForm

# SIGN UP
def sign_up(request):
    form = SignUpForm()
    if request.method == "POST":
        form =  SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('App_Login:login'))
    return render(request, 'App_Login/signup.html', context={'form':form})        

# SIGN IN
def login_user(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username') #email is treated as username in model.py
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user) 
                return HttpResponse('Logged In')
    return render(request, 'App_Login/login.html', context={'form': form})

# SIGNOUT
@login_required
def logout_user(request):
     logout(request)
     return HttpResponse("Logged Out")




