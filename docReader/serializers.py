from rest_framework import serializers 
from docReader.models import Account, Transaction, User
 
 
class UserSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = User
        fields = ('id',
                  'name',
                  'email')
 
class AccountSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Account
        fields = ('id',
                  'userId',
                  'number')
 
class TransactionSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Transaction
        fields = ('id',
                  'date',
                  'credit',
                  'amount',
                  'accountId')
