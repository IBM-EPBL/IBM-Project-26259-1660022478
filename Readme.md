# Team ID: PNT2022TMID03491\

**Team Lead** : Anand mohanan\
**Team Member 1**: Syed Rayaan Ahmedh R\
**Team Member 2**: Arunachalam S\
**Team Member 3**:Prasanna M\
**Industry Mentor Name**: Khusboo\
**Faculty Mentor Name**: Dr. A. Elakkiya
class Wallet(MPTTMODEL):
name = models.CharField(verbose*name=*("Wallet Name"),help*text=("Wallet Name"),max_length=255) # amount = models.IntegerField(verbose_name=*("Expense Amount"),help_text=("Expense Amount"))
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
expense*wallet = models.ForeignKey(Wallet,on_delete=models.RESTRICT)
name = models.CharField(verbose_name=*("Budget Name"),help*text=("Budget Name"),max_length=255)
amount = models.IntegerField(verbose_name=*("Bugdget Amount"),help*text=("Budget Amount"))
class Meta:
verbose_name = *("Budget")
verbose*name_plural = *("Budgets")

    def __str__(self) -> str:
        return self.name

class Expense(models.Model):
expense*wallet = models.ForeignKey(Wallet,on_delete=models.RESTRICT)
expense_budget = models.ForeignKey(Budget,on_delete=models.RESTRICT)
name = models.CharField(verbose_name=*("Expense Name"),help*text=("Expense Name"),max_length=255)
amount = models.IntegerField(verbose_name=*("Expense Amount"),help*text=("Expense Amount"))
class Meta:
verbose_name = *("Expense")
verbose*name_plural = *("Expenses")

    def __str__(self) -> str:
        return self.name

class Income(models.Model):
income*wallet = models.ForeignKey(Wallet,on_delete=models.RESTRICT)
income_budget = models.ForeignKey(Budget,on_delete=models.RESTRICT)
name = models.CharField(verbose_name=*("Income Name"),help*text=("Income Name"),max_length=255)
amount = models.IntegerField(verbose_name=*("Income Amount"),help*text=("Income Amount"))
class Meta:
verbose_name = *("Income")
verbose*name_plural = *("Incomes")

    def __str__(self) -> str:
        return self.name
