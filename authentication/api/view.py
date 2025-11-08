from rest_framework import generics, permissions
from user.models import User
from .serializers import RegisterSerializer, UserSerializer
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterView(generics.CreateAPIView): #CREATE API VIEW SERVE PARA CRIAR DADOS
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]


class MeView(APIView): #API VIEW SERVE PARA PEGAR DADOS

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [permissions.AllowAny]