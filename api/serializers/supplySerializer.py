from api.models.supply import Supply
from rest_framework import serializers


class SupplySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Supply
        fields = '__all__'
        extra_kwargs = {'user': {'required': True}}


class SupplyDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Supply
        fields = '__all__'
        extra_kwargs = {'user': {'required': True}}
        