# jwt auth imports
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from Profiles.serializers import ProfileSerializer
from Profiles.models import Profile


# TOKEN PAIR SERIALIZER
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        profile = Profile.objects.get(user=user)
        profile_serializer = ProfileSerializer(profile, many=False)

        # Add custom claims
        token['username'] = user.username
        token['id'] = user.id
        token['profile'] = profile_serializer.data

        return token

    
class RegisterSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = '__all__'


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match"})
            
        return attrs

        
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user