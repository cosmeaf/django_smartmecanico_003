from rest_framework import generics, viewsets
from rest_framework.permissions import AllowAny
from api.serializers.userRegisterSerializer import UserRegisterSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

################### REGISTER USER VIEW ###################       
class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer