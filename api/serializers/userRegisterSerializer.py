from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
User = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all(),message="E-mail já Cadastrado",)])
    username = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all(),message="Usuário já cadastrato")])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'password2')
        # extra_kwargs = {
        #     'first_name': {'required': False},
        #     'last_name': {'required': False}
        # }

    def validate_password1(self, password1):
        if password1 != self.initial_data["password2"]:
            raise serializers.ValidationError("Passwords do not match")
        return password1
      
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            # first_name=validated_data['first_name'],
            # last_name=validated_data['last_name']
        )  
        user.set_password(validated_data['password'])
        user.save()
        return user