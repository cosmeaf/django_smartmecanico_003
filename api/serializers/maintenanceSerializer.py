from api.models.maintenance import Maintenance
from rest_framework import serializers


class MaintenanceSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Maintenance
        fields = '__all__'
        extra_kwargs = {'user': {'required': True}}


class MaintenanceDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Maintenance
        fields = '__all__'
        extra_kwargs = {'user': {'required': True}}
        