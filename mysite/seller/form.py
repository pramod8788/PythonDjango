from django import forms
from ecommerce.models import Fashion
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


User = get_user_model()

class Sellerform(forms.ModelForm):
    class Meta:
       model=Fashion
       fields= "__all__"
       exclude = ("slug",)
       labels={
           "prod_name":"Product Name"
       }

       error_messages = {
           "prod_name":{
               "required":"field cannot be empty !",
           }
       }


class Sellersignup(UserCreationForm):
    phone_number = forms.CharField(label="Enter Phone Number", max_length=10, widget=forms.TextInput(attrs={'class':'form-control'}))
    gst_id = forms.CharField(label="Enter GSTIN", max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    aadhar_number = forms.CharField(label="Enter Aadhar Number", max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2',
            ]

    def __init__(self, *args, **kwargs):
        super(Sellersignup, self).__init__(*args, **kwargs)
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


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput(attrs={'class':'form-control'}))