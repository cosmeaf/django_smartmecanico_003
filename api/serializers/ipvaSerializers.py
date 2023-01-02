from api.models.ipva import Ipva
from rest_framework import serializers


class IpvaSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Ipva
        fields = '__all__'
        extra_kwargs = {'user': {'required': True}}


class IpvaDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Ipva
        fields = '__all__'
        extra_kwargs = {'user': {'required': True}}
        