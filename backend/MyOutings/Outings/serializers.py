from rest_framework.serializers import ModelSerializer
from .models import Outing, Expense

class OutingSerializer(ModelSerializer):
    class Meta:
        model = Outing
        fields ='__all__'

class ExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields ='__all__'