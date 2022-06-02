from .models import Student
from .serializers import StudentSerializer, UserSerializer
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class RegisterUser(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'status': 403,
                'errors': serializer.errors,
                'message': "Something went wrong"
            })

        serializer.save()
        user = User.objects.get(username=serializer.data['username'])

        refresh = RefreshToken.for_user(user)

        return Response({
            'status': 200,
            'payload': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'message': "Your data is saved"
        })


class StudentAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        pk = None
        if kwargs:
            pk = kwargs['pk']
        if pk:
            student_objs = Student.objects.get(id=pk)
            serializer = StudentSerializer(student_objs)
            return Response({'status':200, 'payload': serializer.data})
        else:
            student_objs = Student.objects.all()
            serializer = StudentSerializer(student_objs, many=True)
            return Response({'status':200, 'payload': serializer.data})

    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({
                'status': 403,
                'errors': serializer.errors,
                'message': "Something went wrong"
            })

        serializer.save()
        student = Student.objects.get(id=serializer.data['id'])

        refresh = RefreshToken.for_user(student)

        return Response({
            'status': 200,
            'payload': serializer.data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'message': "Your data is saved"
        })