import os, requests
from django import forms

from api.views import account

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
            # url = '/api/transaction'
            url = os.getenv('API_URL', default='http://localhost:8000/') + 'api/transaction'

            data = {
                'accountNumber': accountNumber,
                'date': params[1],
                'credit': float(params[2]) >= 0,
                'amount': abs(float(params[2]))
            }

            # print(data)

            response = requests.post(url, data=data)

            print(response)

            
        

    # with open()
    # with open('some/file/name.txt', 'wb+') as destination:
    #     for chunk in f.chunks():
    #         destination.write(chunk)
    print('DONE!')