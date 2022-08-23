from django.urls import path
from reader import views 
 
urlpatterns = [ 
    path('', views.input),
]