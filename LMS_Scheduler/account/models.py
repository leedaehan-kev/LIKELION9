from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateTimeField

# Create your models here.
class Account(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
