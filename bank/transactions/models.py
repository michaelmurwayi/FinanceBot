from django.db import models

# Create your models here.
class Records(models.Model):
    id = models.AutoField(primary_key= True)
    account_name = models.CharField(max_length=150)
    account_type = models.CharField(max_length=50)
    account_number = models.IntegerField(default=0)
    transaction_type = models.CharField(max_length=10)
    previous_amount = models.IntegerField(default=0)
    current_amount = models.IntegerField(default=0)

    class Meta:
        app_label = "Transactions"
