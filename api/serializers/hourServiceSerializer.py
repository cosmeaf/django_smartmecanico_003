from api.models.hourService import HourService
from rest_framework import serializers


class HourServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HourService
        fields = ['hour']
        # exclude = ['created_at', 'updated_at', 'deleted_at']