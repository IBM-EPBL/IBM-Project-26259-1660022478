from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel,TreeForeignKey
# Create your models here.

class Wallet(MPTTModel):
    name = models.CharField(verbose_name=_("Wallet Name"),help_text=("Wallet Name"),max_length=255)
    # amount = models.IntegerField(verbose_name=_("Expense Amount"),help_text=("Expense Amount"))
    parent = TreeForeignKey("self",on_delete=models.CASCADE,null=True,blank=True,related_name="children")
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by=["name"]
    
    class Meta:
        verbose_name = _("Wallet")
        verbose_name_plural = _("Wallets")
    def __str__(self) -> str:
        return self.name


class Budget(models.Model):
    expense_wallet = models.ForeignKey(Wallet,on_delete=models.RESTRICT) 
    name = models.CharField(verbose_name=_("Budget Name"),help_text=("Budget Name"),max_length=255)
    amount = models.IntegerField(verbose_name=_("Bugdget Amount"),help_text=("Budget Amount"))
    class Meta:
        verbose_name = _("Budget")
        verbose_name_plural = _("Budgets")

    def __str__(self) -> str:
        return self.name

class Expense(models.Model):
    expense_wallet = models.ForeignKey(Wallet,on_delete=models.RESTRICT)
    expense_budget = models.ForeignKey(Budget,on_delete=models.RESTRICT)
    name = models.CharField(verbose_name=_("Expense Name"),help_text=("Expense Name"),max_length=255)
    amount = models.IntegerField(verbose_name=_("Expense Amount"),help_text=("Expense Amount"))
    class Meta:
        verbose_name = _("Expense")
        verbose_name_plural = _("Expenses")

    def __str__(self) -> str:
        return self.name

class Income(models.Model):
    income_wallet = models.ForeignKey(Wallet,on_delete=models.RESTRICT) 
    income_budget = models.ForeignKey(Budget,on_delete=models.RESTRICT)
    name = models.CharField(verbose_name=_("Income Name"),help_text=("Income Name"),max_length=255)
    amount = models.IntegerField(verbose_name=_("Income Amount"),help_text=("Income Amount"))
    class Meta:
        verbose_name = _("Income")
        verbose_name_plural = _("Incomes")

    def __str__(self) -> str:
        return self.name



