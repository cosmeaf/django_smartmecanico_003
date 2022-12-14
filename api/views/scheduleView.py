from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from api.models.schedule import Schedule
from api.serializers.scheduleSerializer import ScheduleSerializer, ScheduleDetailSerializer


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
            return self.queryset.filter(user=user)