from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserCreateSerializer(BaseUserCreateSerializer):
     nickname = serializers.CharField(required=False)
     department = serializers.CharField(required=False)
     profile_picture = serializers.ImageField(required=False)

     class Meta(BaseUserCreateSerializer.Meta):
         model = CustomUser
         fields = BaseUserCreateSerializer.Meta.fields + ('nickname', 'department', 'profile_picture')

class UserSerializer(serializers.ModelSerializer):
     class Meta:
         model = CustomUser
         exclude = ('is_deleted',)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        if self.user.is_deleted:
            raise serializers.ValidationError('User is deactivated')
        return data
