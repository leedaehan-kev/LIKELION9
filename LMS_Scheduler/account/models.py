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


class Attendance(models.Model):
    user=models.ForeignKey(Customer, on_delete=models.CASCADE)
    attendance=models.DateTimeField()

class Class(models.Model):
    myclass:models.IntegerField()
    class_name=models.CharField(max_length=20)
    class_time=models.TimeField()

class Priority(models.Model):
    user=models.ForeignKey(Customer, on_delete=models.CASCADE)
    myclass=models.ForeignKey(Class, on_delete=models.CASCADE)
    rank=models.IntegerField()

class Statistics(models.Model):
    user=models.ForeignKey(Customer, on_delete=models.CASCADE)
    daily=models.TimeField()
    date=models.DateField()

class Calendercolor(models.Model):
    user=models.ForeignKey(Customer, on_delete=models.CASCADE)

class Faq(models.Model):
    faq_no=models.IntegerField()
    user=models.ForeignKey(Customer,on_delete=models.CASCADE)
    faq_title=models.CharField(max_length=45)
    faq_date=models.DateTimeField()
    faq_body=models.CharField(max_length=1000)

class Notices(models.Model):
    notice_title=models.CharField(max_length=45)
    notice_date=models.DateTimeField()
    notice_body=models.CharField(max_length=1000)
    
    
