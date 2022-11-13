from django.contrib import admin
from mptt.admin import MPTTModelAdmin


# Register your models here.

from .models import(
    Budget,Expense,Income,Wallet
)

admin.site.register(Wallet,MPTTModelAdmin)