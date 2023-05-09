from rest_framework import serializers

from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'last_login', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'profile_image', 'phone_number','verify')
        
class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length = 255,write_only = True
    )
    email = serializers.EmailField(
        write_only = True
    )
    first_name = serializers.CharField(
        max_length = 255, write_only = True
    )
    phone_number = serializers.CharField(
        max_length = 255, write_only = True
    )
    password = serializers.CharField(
        max_length = 255, write_only = True
    )
    password2 = serializers.CharField(
        max_length = 255, write_only = True
    )
    class Meta:
        model = User
        fields = ("username", 'email', 'first_name', 'last_name', 'phone_number', 'password', 'password2')
        
    def validate(self, attrs):
        if attrs ['password'] != attrs['password2']:
             return serializers.ValidationError({'password': 'Пароли отличаются'})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        