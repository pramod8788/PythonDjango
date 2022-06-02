from xml.etree.ElementInclude import include
from django.urls import path, include
from .views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('router-name', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
] 