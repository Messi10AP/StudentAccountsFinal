from django import forms
from django.forms import ModelForm

class RegisterForm(forms.Form):
    CHOICES = ( 
				(9,'9'), (10,'10'), (11,'11'), (12,'12') , 
			  )
    fname = forms.CharField(max_length = 25)
    lname = forms.CharField( max_length = 25)
    emailid = forms.EmailField()
    passwd1 = forms.CharField(max_length=100,widget=forms.PasswordInput)
    passwd2 = forms.CharField(max_length=100,widget=forms.PasswordInput)
    gradyear = forms.IntegerField()
    grade = forms.IntegerField()

class LoginForm(forms.Form):
    username = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
