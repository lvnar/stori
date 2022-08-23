from django.core.mail import send_mail

def sendMail(subject='Stori Card Challenge'):
    send_mail(
        subject,
        'Here is the message.',
        'from@example.com',
        ['perez.canseco@gmail.com'],
        fail_silently=False,
    )
