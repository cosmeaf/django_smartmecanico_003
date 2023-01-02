from api.models.calibrateTire import CalibrateTire
from rest_framework import serializers


class CalibrateTireSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = CalibrateTire
        fields = '__all__'
        extra_kwargs = {'user': {'required': True}}


class CalibrateTireDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = CalibrateTire
        fields = '__all__'
        extra_kwargs = {'user': {'required': True}}
        