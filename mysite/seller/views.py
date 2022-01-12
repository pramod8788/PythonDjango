from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from ecommerce import models
from django.views.generic.list import ListView
from . form import Sellerform, Sellersignup, LoginForm 
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from ecommerce import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Home(generic.ListView):
    template_name = "seller/home.html"
    model = models.Category
    context_object_name = "category"


class Sellersignup(CreateView):
    form_class = Sellersignup
    template_name = 'seller/seller_signup.html'
    success_url = '/seller'
    model = User

    def form_valid(self, form):
        data = super(Sellersignup, self).form_valid(form)

        phone, gst, aadhar = form.cleaned_data.get('phone_number'), form.cleaned_data.get('gst_id'), form.cleaned_data.get('aadhar_number')
        models.Seller.objects.create(user=self.object, phone_number=phone, gst_id=gst,aadhar_number=aadhar)
        return data


class SellerUpload(CreateView):
    model = models.Electronic
    form_class = Sellerform
    template_name = 'seller/seller_upload.html'
    success_url = "/thankyou"


class Thankyou(TemplateView):
    template_name = "seller/thankyou.html"


class Dashboard(ListView):
    template_name = 'seller/dashboard.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        model = self.kwargs['category']       
        return getattr(models, model).objects.filter(seller_name__user=self.request.user)


class Sellerservice(TemplateView):
    template_name = "seller/seller-service.html"

    
def logoutPage(request):
    logout(request)
    return redirect("seller-home")

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("seller-home")

    form = LoginForm()

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
            user = authenticate(
                request, username=username, password=password, is_active=True
            )

            if user is not None:
                login(request, user)
                return redirect("seller-home")
            else:
                messages.error(request, "Username or Password does not match...")
        except:
            messages.error(request, "User Not Found....")

    return render(request, "seller/login.html", {"form":form})

