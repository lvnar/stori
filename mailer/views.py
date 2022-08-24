import requests

from django.conf import settings
from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view


ROW_STR = '<tr class="{classType}"><td>{id}</td><td>{type}</td><td>{date}</td><td>{amount:.2f}</td></tr>'


@api_view(['POST'])
def send(request):
    try:
        account = request.data['number']
        name = request.data['user']['name']
        email = request.data['user']['email']

        html = None
        transactions = []

        for t in request.data['transactions']:
            transactions.append(create_HTML(
                id = t['id'],
                date = t['date'],
                amount = t['amount'],
                tType = 'Crédito' if t['credit'] else 'Débito',
                classType = 'creditRow' if t['credit'] else 'DebitRow',
            ))

        with open(str(settings.BASE_DIR) + '/mailer/template.html', 'r') as template:
            html = template.read()
            html = html.format(
                name=name, 
                account=account, 
                email=email, 
                data=''.join(transactions)
            )

        payload = {
            "sender": {"email": "no-reply@stori-card.com"},
            "to": [{"email": email}],
            "subject": "Cuenta {} actualizada".format(account),
            "htmlContent": html
        }
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "api-key": str(settings.SMTP_API_KEY)
        }
        requests.post(str(settings.SMTP_URL), json=payload, headers=headers)

        return JsonResponse({'mensaje':'Correo enviado exitosamente'}, status=status.HTTP_200_OK)

    except Exception as e:
        return JsonResponse(e, status=status.HTTP_400_BAD_REQUEST)



def create_HTML(
        id,
        date,
        amount,
        tType,
        classType):

    return ROW_STR.format(
            classType=classType,
            id=id,
            type=tType,
            date=date,
            amount=amount
        )
        