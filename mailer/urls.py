from django.urls import path

# from . import views
from . import sendMail
urlpatterns = [
    path('', sendMail.send_mail, name='mailer'),
]
 

# from django.http import HttpResponse

# DEBUG = True
# SECRET_KEY = '4l0ngs3cr3tstr1ngw3lln0ts0l0ngw41tn0w1tsl0ng3n0ugh'
# ROOT_URLCONF = __name__

# def home(request):
#     color = request.GET.get('color', '')
#     return HttpResponse(
#         '<h1 style="color:' + color + '">Welcome to the Tinyapp\'s Homepage!</h1>'
#     )  # don't use user input like that in real projects!
