from django.db import models

# Create your models here.
class Records(models.Model):
    account_name = models.CharField(max_length=100)
    account_type = models.CharField(max_length=50)
    branch_name = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=20)
    transaction_type = models.CharField(max_length=10)
    account_number = models.IntegerField(default=0)
    transaction_amount = models.FloatField(null=True, default=None)
    owner = models.ForeignKey('auth.User', related_name='admin', on_delete=models.CASCADE)    
   
    class Meta:
        app_label = "Transactions"
