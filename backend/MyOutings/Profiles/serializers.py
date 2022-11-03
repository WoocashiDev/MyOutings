from rest_framework.serializers import ModelSerializer
from .models import Profile

# USER PROFILE SERIALIZER
class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields ='__all__'


