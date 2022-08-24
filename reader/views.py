import json
import requests

from django.conf import settings
from django.http.response import JsonResponse
from rest_framework import status

from reader import file_handler

def upload_file(request):
    if request.method == 'POST':
        form = file_handler.UploadFileForm(request.POST, request.FILES)
        
        if form.is_valid():
            account_data = file_handler.inputFileHandler(request.FILES['file'])

            url = str(settings.API_URL) + 'mail'
            resp = requests.post(url, json=account_data)
            if resp.status_code == requests.codes.ok:
                return JsonResponse(account_data, status=status.HTTP_200_OK)

        return JsonResponse(form.errors, status=status.HTTP_400_BAD_REQUEST)
