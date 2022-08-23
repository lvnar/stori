from functools import partial
from select import select
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

# from api.models import User, Account, Transaction
# from api.serializers import UserSerializer, AccountSerializer, TransactionSerializer
from rest_framework.decorators import api_view


@api_view(['POST'])
def input(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
