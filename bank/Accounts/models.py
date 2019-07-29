from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=50)
    second_name = models.CharField(max_length=50)
    account_name = models.CharField(max_length=100)
    account_number = models.IntegerField(primary_key=True)
    account_type = models.CharField(max_length=10)
    branch_name = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=20)
