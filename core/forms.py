from django import forms 
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Username',
            'class':'w-5/6 px-6 py-3 rounded-xl',
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder':'Password', 
            'class':'w-5/6 px-6 py-3 rounded-xl',
        }
    ))


class SignupForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ('username' , 'email', 'password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder':'Username',
            'class':'w-5/6 px-6 py-3 rounded-xl',
        }
    ))

    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'placeholder':'Email',
            'class':'w-5/6 px-6 py-3 rounded-xl',
        }
    ))

    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder':'Password', 
            'class':'w-5/6 px-6 py-3 rounded-xl',
        }
    ))

    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder':'Repeat Password', 
            'class':'w-5/6 px-6 py-3 rounded-xl',
        }
    ))

