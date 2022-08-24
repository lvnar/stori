from django.urls import path
from mailer import views

urlpatterns = [
    path('', views.send),
]
