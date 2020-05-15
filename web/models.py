from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Token(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    token=models.CharField(max_length=45)
    def __str__(self):
        return '{}_token'.format(self.user)



class Expense(models.Model):
    text=models.CharField(max_length=255)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)  #user is an object of class Userpythn
    def __str__(self):
        return '{}-{}'.format(self.text, self.date)


class Income(models.Model):
    text=models.CharField(max_length=155)
    date=models.DateTimeField()
    amount=models.BigIntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return '{}_{}'.format(self.text, self.user)

