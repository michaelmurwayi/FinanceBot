from django.db import models

<<<<<<< HEAD
# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=60, blank=False, null=False)
    second_name = models.CharField(max_length=60, blank=False, null=False)
    account_name = models.CharField(max_length=100, blank=False, null=False)
    account_number = models.IntegerField(unique=True, blank=False, null=False)
    account_type = models.CharField(max_length=10, blank=False, null=False)
    branch_name = models.CharField(max_length=25, blank=False, null=False)
    phonenumber = models.CharField(max_length=20, blank=False, null=False)
   
    class Meta:
        app_label = "Account"
=======

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    second_name = models.CharField(max_length=50, blank=False, null=False)
    account_name = models.CharField(max_length=100, blank=False, null=False)
    account_number = models.IntegerField(
        primary_key=True, unique=True, blank=False, null=False
    )
    account_type = models.CharField(max_length=10, blank=False, null=False)
    branch_name = models.CharField(max_length=20, blank=False, null=False)
    phonenumber = models.CharField(max_length=20, blank=False, null=False)

    class Meta:
        app_label = "Accounts"
>>>>>>> 78a7e4082813e6d67ddbab3671f12fed5ab8b4af
