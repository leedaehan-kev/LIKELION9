from django.db import models

# Create your models here.
class Account(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()