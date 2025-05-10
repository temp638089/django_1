from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class StudentForm(ModelForm):
    
    class Meta:
        model = student
        fields = "__all__"
        widgets = {
            'deaprtment': forms.Select(),  # This ensures a dropdown menu
        }

class StudentForm2(ModelForm):
    
    class Meta:
        model = student
        fields = ['name']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(forms.Form):
    username=forms.CharField(max_length=150,widget=forms.TextInput)
    password=forms.CharField(max_length=50,widget=forms.PasswordInput)