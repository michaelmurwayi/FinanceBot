from Accounts.models import Account
from django.test import TestCase

class TestAccountModel(TestCase):
    def create_account(self):
        
        # create user object in database
        
        return  Account.objects.create(first_name= 'Michael', second_name= 'Mulama', account_name='MichaelMulama', account_number='8080', account_type='saving',branch_name='Thika', phonenumber='0780808080')

    def test_account_creation(self):
        
        # test the user creation method
        
        Accounts = self.create_account()
        self.assertTrue(isinstance(Accounts, Account))
        self.assertEqual(user.__unicode__(), user.id)
        