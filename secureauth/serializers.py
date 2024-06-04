from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Role

User = get_user_model()

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['name']


class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2', 'role']

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        del attrs['password2']  
        return attrs

    def create(self, validated_data):
        role_data = validated_data.pop('role')
        user = User.objects.create_user(**validated_data)  
        user.role = role_data
        user.save()  
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'token']

    def validate(self, attrs):
        user = User.objects.filter(username=attrs['username']).first()
        if user and user.check_password(attrs['password']):
            attrs['token'] = user.auth_token.key  
            return attrs
        raise serializers.ValidationError({"error": "Invalid credentials"})

