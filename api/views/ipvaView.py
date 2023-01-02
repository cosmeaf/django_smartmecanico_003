from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models.ipva import Ipva
from api.serializers.ipvaSerializers import IpvaSerializer, IpvaDetailSerializer

class IpvaModelViewSet(ModelViewSet):
    queryset = Ipva.objects.all()
    permission_classes = [IsAuthenticated, AllowAny]

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return IpvaSerializer
        else:
            return IpvaDetailSerializer

    def get_queryset(self, pk=None, *args, **kwargs):
        user = self.request.user
        if user.is_superuser:
            return self.queryset.all()
        else:
            return self.queryset.all().filter(user=user.id)