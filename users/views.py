from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from users.serializers import  UserSerializer

from users.models import CustomUser


# Create your views here.
class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset=CustomUser.objects.all()
    def perform_create(self, serializer):
        user=serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


