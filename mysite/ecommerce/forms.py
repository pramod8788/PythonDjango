from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class loginForm(forms.Form):
    username = forms.CharField(
        label="Enter Username:",
        max_length=100,
    )

    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Enter Password:"
    )

class ModifiedUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
