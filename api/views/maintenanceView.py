from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models.maintenance import Maintenance
from api.serializers.maintenanceSerializer import MaintenanceSerializer, MaintenanceDetailSerializer

class MaintenanceModelViewSet(ModelViewSet):
    queryset = Maintenance.objects.all()
    permission_classes = [IsAuthenticated, AllowAny]

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return MaintenanceSerializer
        else:
            return MaintenanceDetailSerializer

    def get_queryset(self, pk=None, *args, **kwargs):
        user = self.request.user
        if user.is_superuser:
            return self.queryset.all()
        else:
            return self.queryset.all().filter(user=user.id)