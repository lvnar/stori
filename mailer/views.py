from tempfile import template
import requests
from django.conf import settings
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view


SMTP_URL = "https://api.sendinblue.com/v3/smtp/email"
ROW_STR = '<tr class="{classType}"><td>{id}</td><td>{type}</td><td>{date}</td><td>{amount:.2f}</td></tr>'


@api_view(['POST'])
def send(request):
    try:
        account, name, email, data = create_HTML(request.data)

        payload = {
            "sender": {"email": "no-reply@myshop.com"},
            "to": [{"email": email}],
            "subject": "Cuenta {} actualizada".format(account),
            "htmlContent": data
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "api-key": "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"
        }

        response = requests.post(SMTP_URL, json=payload, headers=headers)

        return JsonResponse({'mensaje':'Correo enviado exitosamente'}, status=status.HTTP_200_OK)

    except Exception as e:
        return JsonResponse(e, status=status.HTTP_400_BAD_REQUEST)

def create_HTML(data):
    account = data['number']
    name = data['user']['name']
    email = data['user']['email']
    html = None

    transactions = []

    for t in data['transactions']:
        id = t['id']
        date = t['date']
        amount = t['amount']
        type = 'Crédito' if t['credit'] else 'Débito'
        classType = 'creditRow' if t['credit'] else 'DebitRow'

        transactions.append(ROW_STR.format(
            classType=classType,
            id=id,
            type=type,
            date=date,
            amount=amount
        ))

    with open(str(settings.BASE_DIR) + '/mailer/template.html', 'r') as template:
        html = template.read()

    html = html.format(name=name, account=account, email=email, data=''.join(transactions))

    return account, name, email, html
