from django.contrib import admin
from .models import Account
from .models import *
# Register your models here.
admin.site.register(Account)
admin.site.register(Customer)