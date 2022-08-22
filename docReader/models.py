from django.db import models

# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=False, default='')
    email = models.EmailField(blank=False)

class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    number = models.CharField(max_length=10, blank=False, default='')

class Transaction(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField(blank=False, default='')
    credit = models.BooleanField(blank=False, default=None)
    amount = models.FloatField(blank=False, default=0.0)
    accountId = models.ForeignKey(Account, on_delete=models.CASCADE)
