import requests
import csvGenerator
import os
import json

email = os.getenv('T_EMAIL', 'perez.canseco@gmail.com')
server = os.getenv('API_URL', 'http://localhost:8000')
name = os.getenv('T_NAME', 'Cesar Perez Canseco')
account = os.getenv('T_ACCOUNT', 'A123456780')


try:
    payload_user = {
        'email': email,
        'name': name
    }
    headers_user = { 'Content-Type': 'application/json' }
    resp = requests.request(
        "POST",
        server + '/api/user',
        headers=headers_user,
        data=json.dumps(payload_user)
    ).json()
    userId = resp['id']
    print('User created!')
except Exception as e:
    userId = 1
    print('User not created:', e)

try:
    payload_account = {
        'userId': userId,
        'number': account
    }
    headers_account = { 'Content-Type': 'application/json' }
    requests.request(
        "POST",
        server + '/api/account',
        headers=headers_account,
        data=json.dumps(payload_account)
    ).text
    print('Account created!')
except Exception as e:
    print('Account error:', e)

try:
    csvGenerator.create(fileName=account + '.csv', n=5)
    print('Input file generated!')
except Exception as e:
    print('CSV error:', e)

try:
    files=[(
        'file',
        (account + '.csv', open('./' + account + '.csv','rb'),
        'text/csv')
    )]
    requests.request("POST", server + '/input', files=files)
    print('Input data sent!')

except Exception as e:
    print('Input sending error:', e)