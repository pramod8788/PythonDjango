from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home1'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signuppage/', views.SignupView.as_view(), name='signup-page'),
    path('categorypage/<str:category>/', views.CategoryPageView.as_view(), name='category-page'),
    path('productdetail/<str:category>/<slug:slug>/', views.ProductDetilView.as_view(), name='product-detail'),
]
