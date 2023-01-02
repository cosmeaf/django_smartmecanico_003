from api.models.schedule import Schedule
from rest_framework import serializers


################### SCHEDULE SERIALIZERS ###################
class ScheduleSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    
    class Meta:
        model = Schedule
        # fields = '__all__'
        # depth = 1
        exclude = ['created_at', 'updated_at', 'deleted_at']
        # extra_kwargs = {'user': {'required': True}}
        
    def to_representation(self, instance):
      return {
        'id': instance.id,
        'user': instance.user.username,
        'address': instance.address.cep,
        'service': instance.service.name,
        'vehicle': instance.vehicle.brand,
        # 'hour': instance.hour.hour,
        'hour': instance.hour,
        'day': instance.day,
      }

class ScheduleDetailSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Schedule
        # fields = '__all__'
        exclude = ['created_at', 'updated_at', 'deleted_at']
        extra_kwargs = {'user': {'required': True}}
        
    def to_representation(self, instance):
      return {
        'id': instance.id,
        'user': instance.user.username,
        'address': instance.address.cep,
        'service': instance.service.name,
        'vehicle': instance.vehicle.brand,
        # 'hour': instance.hour.hour,
        'hour': instance.hour,
        'day': instance.day,
      }