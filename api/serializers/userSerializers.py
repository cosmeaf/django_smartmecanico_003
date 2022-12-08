from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    # created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = User
        fields = ['id', 'user','username', 'email', 'first_name', 'last_name']
        extra_kwargs = {'user': {'required': True}}