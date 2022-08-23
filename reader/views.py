# from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework import status

from reader import file_handler

def upload_file(request):
    if request.method == 'POST':
        form = file_handler.UploadFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            file_handler.inputFileHandler(request.FILES['file'])
            # print(request.FILES, request.FILES['file'])
            return JsonResponse({}, status=status.HTTP_200_OK)
        return JsonResponse(form.errors, status=status.HTTP_400_BAD_REQUEST)
            # return HttpResponseRedirect('/')
    # return render(request, '/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})



# # from .file_handler import UploadFileForm

# # Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

# def upload_file(request):
#     if request.method == 'POST':
#         form = UploadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponseRedirect('/success/url/')
#     else:
#         form = UploadFileForm()
#     return render(request, 'upload.html', {'form': form})

# from functools import partial
# from select import select
# from django.shortcuts import render
# from django.http.response import JsonResponse
# from rest_framework.parsers import JSONParser 
# from rest_framework import status

# # from api.models import User, Account, Transaction
# # from api.serializers import UserSerializer, AccountSerializer, TransactionSerializer
# from rest_framework.decorators import api_view


# @api_view(['POST'])
# def input(request):
#     print(request.data.get('inputFile'))
#     if request.method == 'POST':
#         return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
#         # serializer = UserSerializer(data=request.data)
        
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
#         # return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
