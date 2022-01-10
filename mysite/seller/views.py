from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from ecommerce import models
from django.views.generic.list import ListView
from . form import Sellerform ,Sellersignup
from django.views import generic
from ecommerce import models


class Home(generic.ListView):
    template_name = "seller/home.html"
    model = models.Category
    context_object_name = "category"


class Sellersignup(CreateView):
    form_class = Sellersignup
    template_name = 'seller/seller_signup.html'
    success_url = 'home'
    model = User

    def form_valid(self, form):
        data = super(Sellersignup, self).form_valid(form)
        phone, gst, aadhar = form.cleaned_data.get('phone_number'), form.cleaned_data.get('gst_id'), form.cleaned_data.get('aadhar_number')
        models.Seller.objects.create(user=self.object, phone_number=phone, gst_id=gst,aadhar_number=aadhar)
        return data


class SellerUpload(CreateView):
    model = models.Fashion
    form_class=Sellerform
    template_name='seller/seller_upload.html'
    success_url = "thankyou"


class Thankyou(TemplateView):
    template_name = "seller/thankyou.html"


class Dashboard(ListView):
    template_name = 'seller/dashboard.html'
    context_object_name = 'products'

    def get_queryset(self):
        model = self.kwargs['category']       
        return getattr(models, model).objects.filter(seller_name__user=self.request.user)

