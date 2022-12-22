from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from api.models.hourService import HourService
from api.serializers.hourServiceSerializer import HourServiceSerializer


# Create your views here.
class HourServiceModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HourService.objects.all()
    serializer_class = HourServiceSerializer
    permission_classes = (AllowAny, )