import requests, json
from django import forms
from django.conf import settings

class UploadFileForm(forms.Form):
    file = forms.FileField()

def inputFileHandler(file):
    accountNumber = str(file).split('.')[0]
    lines = []
    
    for chunk in file.chunks():
        lines += chunk.decode().split('\n')
    

    for line in lines:
        params = line.split(',')

        if len(params) == 3:
            url = str(settings.API_URL) + 'api/transaction'

            data = {
                'accountNumber': accountNumber,
                'date': params[1],
                'credit': float(params[2]) >= 0,
                'amount': abs(float(params[2]))
            }

            requests.post(url, data=data)
            
    url = str(settings.API_URL) + 'api/account/' + accountNumber
    return requests.get(url).json()


      