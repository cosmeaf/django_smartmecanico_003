from api.models.address import Address
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Address
        fields = ['id', 'cep', 'logradouro', 'complemento', 'bairro', 'localidade', 'uf', 'user']
        extra_kwargs = {'user': {'required': True}}


class AddressDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Address
        fields = ['id', 'cep', 'logradouro', 'complemento', 'bairro', 'localidade', 'uf', 'user']
        extra_kwargs = {'user': {'required': True}}