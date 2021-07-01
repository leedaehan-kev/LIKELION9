from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import Collector
from django.db.models.fields import DateTimeField

# Create your models here.
class Account(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    lmsId = models.IntegerField()
    lmsPwd = models.CharField(max_length=45)
    # name = models.CharField(max_length=10)
    # color = models.CharField(max_length=20)
    # stamp = models.IntegerField()
    # calendar_type = models.IntegerField()
    # font = models.IntegerField()
    # type = models.IntegerField()
    # language = models.IntegerField()

    def __str__(self):
        return self.user
