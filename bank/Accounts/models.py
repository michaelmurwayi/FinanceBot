from django.db import models


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
    owner = models.ForeignKey('auth.User', related_name='Accounts', on_delete=models.CASCADE)

    class Meta:
        app_label = "Accounts"
    def __unicode__(self):
        return self.id

