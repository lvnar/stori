from django.urls import path
from api import views 
 
urlpatterns = [ 
    path('user', views.users),
    path('user/<id>', views.user),
    path('account', views.accounts),
    path('account/<number>', views.account),
    path('transaction', views.transactions),
    path('transaction/<id>', views.transaction),
]