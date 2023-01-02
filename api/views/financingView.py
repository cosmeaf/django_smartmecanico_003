from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.models.financing import Financing
from api.serializers.financingSerializer import FinancingSerializer, FinancingDetailSerializer

class FinancingModelViewSet(ModelViewSet):
    queryset = Financing.objects.all()
    permission_classes = [IsAuthenticated, AllowAny]

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return FinancingSerializer
        else:
            return FinancingDetailSerializer

    def get_queryset(self, pk=None, *args, **kwargs):
        user = self.request.user
        if user.is_superuser:
            return self.queryset.all()
        else:
            return self.queryset.all().filter(user=user.id)