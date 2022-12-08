from rest_framework import serializers
from api.models.profile import Profile

class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    # created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Profile
        fields = '__all__'
        extra_kwargs = {'user': {'required': True}}