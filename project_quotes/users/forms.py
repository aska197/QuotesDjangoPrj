from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Profile

class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=100, required=True, widget=forms.TextInput())
    password = forms.CharField(label="Password", max_length=50, required=True, widget=forms.PasswordInput())
