from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models.vehicle import Vehicle
from api.serializers.vehicleSerializer import VehicleSerializer, VehicleDetailSerializer


class VehicleModelViewSet(ModelViewSet):
    queryset = Vehicle.objects.all()
    permission_classes = [IsAuthenticated, AllowAny]

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return VehicleSerializer
        else:
            return VehicleDetailSerializer

    def get_queryset(self, pk=None, *args, **kwargs):
        user = self.request.user
        if user.is_superuser:
            return self.queryset.all()
        else:
            return self.queryset.all().filter(user=user.id)