from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import viewsets
from api.models.service import Service
from api.serializers.serviceSerializer import ServiceSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

# Create your views here.
class ServiceModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = (AllowAny, )
    
# class ServiceModelViewSet(viewsets.GenericViewSet):
#     queryset = Service.objects.all()
#     serializer_class = ServiceSerializer
#     permission_classes = [IsAuthenticated, AllowAny]

#     def get_queryset(self, pk=None):
#         if pk is None:
#             return self.get_serializer().Meta.model.objects.all()
#         return self.get_serializer().Meta.model.objects.filter(id=pk, is_active=True).first()

#     def list(self, request):
#         serializer = self.get_serializer(self.get_queryset(), many=True)
#         return Response(serializer.data)