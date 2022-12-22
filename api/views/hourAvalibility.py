from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from api.serializers.hourAvailibilitSerializer import HourAvailibilitySerializer
from api.models.schedule import Schedule

# Create your views here.
class HourAvailibility(viewsets.ReadOnlyModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = HourAvailibilitySerializer
    permission_classes = (AllowAny, )