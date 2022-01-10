from django import forms
from ecommerce.models import Fashion
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class Sellerform(forms.ModelForm):
    class Meta:
       model=Fashion
       fields= "__all__"
       labels={
           "prod_name":"Product Name"
       }

       error_messages = {
           "prod_name":{
               "required":"field cannot be empty !",
           }
       }


class Sellersignup(UserCreationForm):
    phone_number = forms.CharField(max_length=10)
    gst_id = forms.CharField(max_length=20)
    aadhar_number = forms.CharField(max_length=20)
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
 

        error_messages = {
           "email":{
               "required":"field cannot be empty !",
           }
       }
