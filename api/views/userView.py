from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.serializers.userSerializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

################### REGISTER USER VIEW ###################       
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_queryset(self, pk=None, *args, **kwargs):
        user = self.request.user
        if user.is_superuser:
            return self.queryset.all()
        else:
            return self.queryset.all().filter(username=user)