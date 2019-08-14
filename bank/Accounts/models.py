from django.db import models

# Create your models here.
class Account(models.Model):
    id = models.AutoField(primary_key=True)
<<<<<<< HEAD
=======
<<<<<<< HEAD
    first_name = models.CharField(max_length=60, blank=False, null=False)
    second_name = models.CharField(max_length=60, blank=False, null=False)
    account_name = models.CharField(max_length=100, blank=False, null=False)
    account_number = models.IntegerField(unique=True, blank=False, null=False)
    account_type = models.CharField(max_length=10, blank=False, null=False)
    branch_name = models.CharField(max_length=25, blank=False, null=False)
    phonenumber = models.CharField(max_length=20, blank=False, null=False)
    owner = models.ForeignKey('auth.User', related_name='Accounts', on_delete=models.CASCADE)

=======
<<<<<<< HEAD
    first_name = models.CharField(max_length=60, blank=False, null=False)
    second_name = models.CharField(max_length=60, blank=False, null=False)
    account_name = models.CharField(max_length=100, blank=False, null=False)
    account_number = models.IntegerField(unique=True, blank=False, null=False)
=======
>>>>>>> 72c8b97823d34f003d80545c37ccdc6fae0a274b
    first_name = models.CharField(max_length=50, blank=False, null=False)
    second_name = models.CharField(max_length=50, blank=False, null=False)
    account_name = models.CharField(max_length=100, blank=False, null=False)
    account_number = models.IntegerField( unique=True, blank=False, null=False)
<<<<<<< HEAD
=======
>>>>>>> 7c9c84d836d4bcd2d90e49866605abce2e40086c
>>>>>>> 72c8b97823d34f003d80545c37ccdc6fae0a274b
    account_type = models.CharField(max_length=10, blank=False, null=False)
    branch_name = models.CharField(max_length=25, blank=False, null=False)
    phonenumber = models.CharField(max_length=20, blank=False, null=False)
<<<<<<< HEAD
    owner = models.ForeignKey('auth.User', related_name='owner', on_delete=models.CASCADE)


=======
   
>>>>>>> 7b59037953268f4ae51fd33f8cf7f34be74744f5
>>>>>>> 72c8b97823d34f003d80545c37ccdc6fae0a274b
    class Meta:
<<<<<<< HEAD
        app_label = "Account"
=======
        app_label = "Accounts"
<<<<<<< HEAD
    def __unicode__(self):
        return self.id

=======
    

    def __unicode__(self):
        return self.id
>>>>>>> 7c9c84d836d4bcd2d90e49866605abce2e40086c
>>>>>>> 7b59037953268f4ae51fd33f8cf7f34be74744f5
