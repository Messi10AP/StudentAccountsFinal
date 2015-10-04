from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls import url
from .models import User
from .forms import RegisterForm
# Create your views here.

def login(request):
    print "login"
    form = RegisterForm()
    if request.method == 'POST':
        
        print "post login"
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
        if form.is_valid():
            print form.cleaned_data
        else:
            print "error"
            print form.errors
    else:
        form = RegisterForm()
    return render(request, 'student/signup.html', {'form': form})

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
	
