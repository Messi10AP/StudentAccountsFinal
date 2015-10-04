from django import forms
from django.forms import ModelForm

class LoginForm(forms.Form):
	fname = forms.CharField(label = 'firstname', max_length = 25)

