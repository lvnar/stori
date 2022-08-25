from email.policy import default
from rest_framework import serializers 
from api.models import Account, Transaction, User
 
 
class TransactionSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Transaction
        fields = '__all__'
 
class AccountSerializer(serializers.ModelSerializer):
    isActive = serializers.BooleanField(default=True)
    transactions = serializers.StringRelatedField(many=True)
 
    class Meta:
        model = Account
        exclude = ['user']
 
class AccountDetailSerializer(serializers.ModelSerializer):
    isActive = serializers.BooleanField(default=True)
    transactions = TransactionSerializer(many=True, read_only=True)
 
    class Meta:
        model = Account
        fields = '__all__'
        depth = 1
 
class UserSerializer(serializers.ModelSerializer):
    isActive = serializers.BooleanField(default=True)
    # accounts = serializers.StringRelatedField(many=True)
 
    class Meta:
        model = User
        fields = '__all__'
 
class UserDetailSerializer(serializers.ModelSerializer):
    isActive = serializers.BooleanField(default=True)
    accounts = AccountSerializer(many=True, read_only=True)
 
    class Meta:
        model = User
        fields = '__all__'
