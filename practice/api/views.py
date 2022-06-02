from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['name']

    # filter_backends = [filters.SearchFilter]
    # search_fields = ['^name']

    filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['name']

    # def get_queryset(self):
    #     user = self.request.user
    #     return User.objects.filter(name="Ramu")