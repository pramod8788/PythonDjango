from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.Home.as_view(),name='home'),
    path("accounts/", include('django.contrib.auth.urls')),
    path("dashboard/<str:category>/", views.Dashboard.as_view(),name='dashboard'),
    path("seller_upload", views.SellerUpload.as_view(),name='seller_upload'),
    path('seller_signup', views.Sellersignup.as_view(),name='seller_signup'),
    path('seller_services', views.Sellersignup.as_view(),name='services'),
    path("thankyou", views.Thankyou.as_view(), name="thankyou"),
]