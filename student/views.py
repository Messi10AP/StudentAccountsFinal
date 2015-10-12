from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import url
from django.contrib.auth import authenticate, login
from .models import UserInfo
from django import forms
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return render(request, 'student/homepage.html')

def signin(request):
    print "login"
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print "input username ", username
        user = authenticate(username=username, password=password)
        if user is not None:
            print "user not none"
            login(request, user)
            print user.username
            print user.email
            return render(request, 'student/info.html')
        else:
             #if form.is_valid():
                # process the data in form.cleaned_data as required
                # if password valid redirect to student info page
                # redirect to a new URL:
                
             #print form.cleaned_data
                #return HttpResponseRedirect('student/info/')
		print "login failed"
		return HttpResponseRedirect('student/error/')
         #if form.is_valid():
            # process the data in form.cleaned_data as required
            # if password valid redirect to student info page
            # redirect to a new URL:
            
 	    #print form.cleaned_data
            #return HttpResponseRedirect('student/info/')
    else:
        print "hello"
         #form = LoginForm()
    #return render(request, 'student/index.html', {'form': form})
    return render(request, 'student/login.html', {'form': form})

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

                ui.save()


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
    return render(request, 'student/error.html', {} )
