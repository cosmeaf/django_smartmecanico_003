from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models.address import Address
from api.serializers.addressSerializer import AddressSerializer, AddressDetailSerializer


class AddressModelViewSet(ModelViewSet):
    queryset = Address.objects.all()
    permission_classes = [IsAuthenticated, AllowAny]

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return AddressSerializer
        else:
            return AddressDetailSerializer

    def get_queryset(self, pk=None, *args, **kwargs):
        user = self.request.user
        if user.is_superuser:
            return self.queryset.all()
        else:
            return self.queryset.all().filter(user=user.id)