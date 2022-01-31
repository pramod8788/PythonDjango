from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('upload/', views.fileupload, name="upload"),
    # path('create-info/', views.create_info, name="create-info"),
    path('create-info/', views.CreateInfoView.as_view(), name="create-info"),
    path('image-info/', views.image_page, name="image-info"),
    path('image-rate/', views.image_rate, name="image-rate"),
    path('image-like/', views.image_like, name="image-like"),
    path('rating-remove/<int:id>', views.rating_remove, name="rating-remove"),
]
