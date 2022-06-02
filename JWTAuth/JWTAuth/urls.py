from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from base import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.StudentAPI.as_view(), name="students-list"),
    path('students/<int:pk>/', views.StudentAPI.as_view(), name="students-list"),
    path('register/', views.RegisterUser.as_view(), name="register"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refres'),
]
