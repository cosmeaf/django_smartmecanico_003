from api.models.fineTraffic import FineTraffic
from rest_framework import serializers


class FineTrafficSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = FineTraffic
        fields = '__all__'
        extra_kwargs = {'user': {'required': True}}


class FineTrafficDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = FineTraffic
        fields = '__all__'
        extra_kwargs = {'user': {'required': True}}
        