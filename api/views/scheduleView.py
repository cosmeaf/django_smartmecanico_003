from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from api.models.schedule import Schedule
from api.serializers.scheduleSerializer import ScheduleSerializer, ScheduleDetailSerializer
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User
# Create your views here.


class ScheduleModelViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    permission_classes = [IsAuthenticated, AllowAny]

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return ScheduleSerializer
        else:
            return ScheduleDetailSerializer

    def get_queryset(self, pk=None, *args, **kwargs):
        user = self.request.user
        if user.is_superuser:
            return self.queryset.all()
        else:
            return self.queryset.all().filter(user=user.id)