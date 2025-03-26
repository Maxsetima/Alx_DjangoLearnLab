from rest_framework import generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import CustomUser
from .serializers import UserSerializer

# Registration view
class UserRegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = CustomUser.objects.get(id=response.data['id'])
        token, created = Token.objects.get_or_create(user=user)
        response.data['token'] = token.key
        return response

# Optionally, add login and user detail/update views here using DRF generics
