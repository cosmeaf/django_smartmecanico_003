from api.models.insurance import Insurance
from rest_framework import serializers


class InsuranceSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Insurance
        fields = '__all__'
        extra_kwargs = {'user': {'required': True}}


class InsuranceDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Insurance
        fields = '__all__'
        extra_kwargs = {'user': {'required': True}}
        