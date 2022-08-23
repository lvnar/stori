from enum import unique
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    email = models.EmailField(blank=False, unique=True)
    isActive = models.BooleanField(default=True)

class Account(models.Model):
    user = models.ForeignKey(User, related_name='accounts', on_delete=models.CASCADE)
    number = models.CharField(max_length=10, blank=False, default='', unique=True)
    isActive = models.BooleanField(default=True)

    # def __str__(self):
    #     return '%s' % (self.number)

class Transaction(models.Model):
    date = models.DateField(blank=False, default='')
    credit = models.BooleanField(blank=False, default=None)
    amount = models.FloatField(blank=False, default=0.0)
    account = models.ForeignKey(Account, related_name='transactions', on_delete=models.CASCADE)

    # def __str__(self):
    #     type = 'Credit' if self.credit else 'Debit'
    #     return '%s - %s: %s' % (type, self.date, self.amount)
