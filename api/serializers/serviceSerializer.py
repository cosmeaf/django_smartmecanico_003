from api.models.service import Service
from rest_framework import serializers


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        # fields = '__all__'
        exclude = ['created_at', 'updated_at', 'deleted_at']
        
# class ServiceSerializer(serializers.ModelSerializer):
#     # user = serializers.StringRelatedField()
    
#     class Meta:
#         model = Service
#         fields = ['id', 'name', 'description']
#         extra_kwargs = {'user': {'required': True}}
#         #exclude = ['user']

# class ServiceDetailSerializer(serializers.ModelSerializer):
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())

#     class Meta:
#         model = Service
#         fields = ['id', 'name', 'description']
#         extra_kwargs = {'user': {'required': True}}