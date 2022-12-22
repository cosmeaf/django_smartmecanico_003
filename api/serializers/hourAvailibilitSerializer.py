from api.models.schedule import Schedule
from rest_framework import serializers


class HourAvailibilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ['hour', 'day']
        # exclude = ['created_at', 'updated_at', 'deleted_at']