from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from apps.accounts.models import CustomUser
from apps.accounts.serializers import UserSerializer


# Create your views here.

class RegisterUserView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]
