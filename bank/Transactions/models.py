from django.db import models

# Create your models here.
class Records(models.Model):
    account_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=50)
    phonenumber = models.IntegerField(default=0)
    transaction_type = models.CharField(max_length=10)
    account_number = models.IntegerField(default=0)
    transaction_amount = models.FloatField(null=True, default=None)

    class Meta:
        app_label = "Transactions"
