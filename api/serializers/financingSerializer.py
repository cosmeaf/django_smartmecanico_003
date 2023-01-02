from api.models.financing import Financing
from rest_framework import serializers


class FinancingSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Financing
        fields = '__all__'
        extra_kwargs = {'user': {'required': True}}


class FinancingDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Financing
        fields = '__all__'
        extra_kwargs = {'user': {'required': True}}
        