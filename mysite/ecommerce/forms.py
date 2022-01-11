from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField


User = get_user_model()

class LoginForm(AuthenticationForm):
    username = UsernameField(label='Enter Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Enter Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))

class ModifiedUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


    def __init__(self, *args, **kwargs):
        super(ModifiedUserForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs['class'] = 'form-control'
        self.fields["username"].label = "Enter Username"

        self.fields["first_name"].widget.attrs['class'] = 'form-control'
        self.fields["first_name"].label = "Enter First Name"

        self.fields["last_name"].widget.attrs['class'] = 'form-control'
        self.fields["last_name"].label = "Enter Last Name"
        
        self.fields["email"].widget.attrs['class'] = 'form-control'
        self.fields["email"].label = "Enter Email"
        
        self.fields["password1"].widget.attrs['class'] = 'form-control'
        self.fields["password1"].label = "Enter Password"
        
        self.fields["password2"].widget.attrs['class'] = 'form-control'
        self.fields["password2"].label = "Confirm Password"