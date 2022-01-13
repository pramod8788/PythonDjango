from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from . form import LoginForm
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.Home.as_view(),name='seller-home'),
    path("loginpage/", views.loginPage, name="seller-login"),
    path("logoutpage/", views.logoutPage, name="seller-logout"),
    # path("uploadproduct/", views.SellerUpload.as_view(),name='upload-product'),
    path("uploadproduct/", views.product_upload, name='upload-product'),
    path("thankyou/", views.Thankyou.as_view(), name="thankyou"),
    path('seller-service/', views.Sellerservice.as_view(),name='seller-service'),
    path('sellersignup/', views.Sellersignup.as_view(),name='seller-signup'),
    path("dashboard/<str:category>/", login_required(views.Dashboard.as_view(),login_url='seller-login'), name='dashboard'),
]