from django import forms
from django.forms import ModelForm
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class RegisterForm(forms.Form):
    GRADE_CHOICES = ( 
                (9,'9'), (10,'10'), (11,'11'), (12,'12') , 
            )
    curr_year = date.today().year
    GRAD_YEAR_CHOICES = ( 
                (curr_year,curr_year), (curr_year+1,curr_year+1), (curr_year+2,curr_year+2), (curr_year+3,curr_year+3) , 
                 )
    fname = forms.CharField(max_length = 25)
    lname = forms.CharField( max_length = 25)
    emailid = forms.EmailField()
    passwd1 = forms.CharField(max_length=100,widget=forms.PasswordInput)
    passwd2 = forms.CharField(max_length=100,widget=forms.PasswordInput)
    gradyear = forms.ChoiceField( choices=GRAD_YEAR_CHOICES)
    grade = forms.ChoiceField( choices=GRADE_CHOICES)

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()

        if cleaned_data['passwd1'] != cleaned_data['passwd2']:
            raise forms.ValidationError({'passwd1':['Password do not match']})

        if User.objects.filter(email=cleaned_data['emailid']).count():
            raise forms.ValidationError({'emailid':['Email already taken ']})

        return cleaned_data

class LoginForm(forms.Form):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = cleaned_data['username']
        password = cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            print "user not none"
            print user.username
            print user.email
        else:
            print "login failed"
            raise forms.ValidationError({'username':['Invalid username/password']})

        return cleaned_data
