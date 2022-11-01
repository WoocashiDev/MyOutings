from rest_framework.serializers import ModelSerializer
from .models import Outing

class OutingSerializer(ModelSerializer):
    class Meta:
        model = Outing
        fields ='__all__'