from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.conf.urls import url
from .models import UserInfo
from django import forms
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def home(request):
    return render(request, 'student/index.html')

@csrf_exempt
def signin(request):
    print "login"
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        print "input username ", username
        try:
            if form.is_valid():
                user = authenticate(username=username, password=password)
                if user is not None:
                    print "user not none"
                    print user.username
                    print user.email
                    login(request,user)
                    return redirect("/")
                else:
                    print "login failed"
                    raise forms.ValidationError({'username':['Invalid username/password']})
            else:
                print form.errors
        except:
            raise
            

    else:
        print "hello"
        form = LoginForm()

    return render(request, 'student/login.html', {'form': form})

@csrf_exempt
def signup(request):
    print "signup"
    if request.method == 'POST':
        print "post signup"
        form = RegisterForm(request.POST)
        try:
            if form.is_valid():
                print form.cleaned_data
                u = User.objects.create_user(form.cleaned_data['emailid'], form.cleaned_data['emailid'], form.cleaned_data['passwd1'] )

                ui = UserInfo()
                ui.user = u
                ui.class_of = form.cleaned_data['gradyear']
                ui.grade = form.cleaned_data['grade']
                ui.balance = 0

                ui.save()
                user = authenticate(username=form.cleaned_data['emailid'], password=form.cleaned_data['passwd1'])
                login(request,user)
                print "after login in signup"
                return redirect("/")


            else:
                print "error"
                print form.errors
        except:
            raise
            print "error here"
            print form.errors
            pass
            #return render(request, 'student/register.html', {'form': form})
            
    else:
        form = RegisterForm()

    return render(request, 'student/register.html', {'form': form})

def forgotpassword(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        
            print form.cleaned_data
            return HttpResponseRedirect('/thanks/')
        else:
            print "INVALID"
            print form.errors
    else:
         form = LoginForm()
    return render(request, 'student/forgotpassword.html')


def studentinfo(request):
    return render(request, 'student/studentinfo.html', {} )
    
def error(request):
    return render(request, 'student/LoginError.html', {} )

def site_logout(request):
    logout(request)
    return redirect("/")
    #return render(request, 'student/studentinfo.html', {} )
