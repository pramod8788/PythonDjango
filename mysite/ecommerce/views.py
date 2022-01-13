from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages
from . import models
from . import forms
import random


# Create your views here.
User = get_user_model()

class HomeView(View):

    def contexData(self):
        try:
            carousel_item = models.Carousel.objects.all()

            homedecor_prod = models.HomeDecor.objects.all().order_by('-pk')[:4]
            fashion_prod = models.Fashion.objects.all().order_by('-pk')[:4]
            electronic_prod = models.Electronic.objects.all().order_by('-pk')[:6]

            combined_list = list(electronic_prod) + list(fashion_prod) + list(homedecor_prod)
            result_list = []
            for i in range(20):
                val = random.choice(combined_list)
                if val in result_list:
                    continue
                else:
                    result_list.append(val)

            context = {
                "carousel":carousel_item,
                # "item":first_item,
                "electronic_prod":electronic_prod,
                "fashion_prod":fashion_prod,
                "homedecor_prod":homedecor_prod,
                "result_list":result_list,
            }

            return context
        except:
            return messages.error(self.request, "Try again later")

    def get(self, request):
        return render(request, 'ecommerce/home.html', self.contexData())


class SignupView(CreateView):
    template_name = 'ecommerce/signup.html'
    model = User
    form_class = forms.ModifiedUserForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        valid = super(SignupView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


class ProductDetilView(DetailView):
    template_name = 'ecommerce/product-detail.html'
    context_object_name = 'product'

    def get_queryset(self):
         model = self.kwargs['category']
         return getattr(models, model).objects.all()    


class CategoryPageView(ListView):
    template_name = 'ecommerce/category-products.html'
    context_object_name = 'category_prod'

    def get_queryset(self):
         model = self.kwargs['category']
         return getattr(models, model).objects.all().order_by('-pk')


class AboutPageView(TemplateView):
    template_name = 'ecommerce/about.html'
