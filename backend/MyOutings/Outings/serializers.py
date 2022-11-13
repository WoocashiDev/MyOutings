from rest_framework.serializers import ModelSerializer
from .models import Outing, Expense
from Profiles.models import Profile
from Profiles.serializers import ProfileSerializer


class ExpenseSerializer(ModelSerializer):
    class Meta:
        model = Expense
        fields ='__all__'

class ExpenseSerializerJoint(ModelSerializer):
    class Meta:
        model = Expense
        fields ='__all__'
    
    paid_by = ProfileSerializer(many=False, source='sponsor')
    paid_for = ProfileSerializer(many=False, source='beneficient')


class OutingSerializer(ModelSerializer):

    class Meta:
        model = Outing
        fields ='__all__'
    
    profiles = ProfileSerializer(many=True, source='participants')
    expenses = ExpenseSerializerJoint(many=True, source='expense_set')
    
    