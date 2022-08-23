# from functools import partial
# from select import select
# from django.shortcuts import render
from functools import partial
import numbers
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

from api.models import User, Account, Transaction
from api.serializers import *
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def users(request):
    if request.method == 'GET':
        users = User.objects.all().filter(isActive=True)
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)
 
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user(request, id):
    try: 
        user = User.objects.get(pk=id) 
    except User.DoesNotExist: 
        return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 

    if request.method == 'GET':
        serializer = UserDetailSerializer(user, many=False)
        return JsonResponse(serializer.data, safe=False)
 
    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        serializer = UserSerializer(user, {'isActive': False}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'User with email {} deactivated'.format(user.email)}, status=status.HTTP_204_NO_CONTENT)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
def accounts(request):
    if request.method == 'GET':
        account = Account.objects.all().filter(isActive=True)
        serializer = AccountSerializer(account, many=True)
        return JsonResponse(serializer.data, safe=False)
 
    elif request.method == 'POST':
        try:
            user = User.objects.get(pk=request.data.get('userId')) 
        except User.DoesNotExist: 
            return JsonResponse({'message': 'The user does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
        account = Account.objects.create(user=user, number=request.data.get('number'))
        serializer = AccountSerializer(account)

        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def account(request, number):
    try: 
        account = Account.objects.get(number=number) 
    except Account.DoesNotExist: 
        return JsonResponse({'message': 'The account does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 

    if request.method == 'GET':
        serializer = AccountDetailSerializer(account, many=False)
        return JsonResponse(serializer.data, safe=False)
 
    elif request.method == 'PUT':
        serializer = AccountDetailSerializer(account, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        serializer = AccountSerializer(account, {'isActive': False}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Account with number {} deactivated'.format(account.number)}, status=status.HTTP_204_NO_CONTENT)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET', 'POST'])
def transactions(request):
    if request.method == 'GET':
        transaction = Transaction.objects.all()
        serializer = TransactionSerializer(transaction, many=True)
        return JsonResponse(serializer.data, safe=False)
 
    elif request.method == 'POST':
        try:
            account = Account.objects.get(number=request.data.get('numberId')) 
        except Account.DoesNotExist: 
            return JsonResponse({'message': 'The account does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
        transaction = Transaction.objects.create(
            account=account,
            date=request.data.get('date'),
            credit=(request.data.get('credit') == 'true'),
            amount=request.data.get('amount')
            )
        serializer = TransactionSerializer(transaction)

        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def transaction(request, id):
    try: 
        transaction = Transaction.objects.get(pk=id) 
    except Transaction.DoesNotExist: 
        return JsonResponse({'message': 'The transaction does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 

    if request.method == 'GET':
        serializer = TransactionSerializer(transaction, many=False)
        return JsonResponse(serializer.data, safe=False)
 
    elif request.method == 'PUT':
        serializer = TransactionSerializer(transaction, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        transaction.delete() 
        return JsonResponse({'message': 'Transaction was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
