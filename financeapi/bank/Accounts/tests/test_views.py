import sys
sys.path.append('..')
from Accounts.models import Account
from django.test import TestCase
from django.test import Client
from Accounts.views import AccountDetail
from django.shortcuts import reverse
from Accounts.serializer import AccountsSerializer
from rest_framework.test import APIRequestFactory

from rest_framework.test import APIClient
class TestAccountsViews(TestCase):
    
    def setUp(self):
        Account.objects.create(first_name= 'Michael', second_name= 'Mulama', account_name='MichaelMulama', account_number='8080', account_type='saving',branch_name='Thika', phonenumber='0780808080') 
    """
    test views in account app
    """
    def test_account_list_view(self):
        """
        test the get method in views
        """
        self.client = Client()
        resp = self.client.get('/accounts/')
        self.assertEqual(resp.status_code, 200)

    def test_account_creation_view(self):
        """
        test the post method in views
        """
        Account.objects.filter(account_number='40200').delete()
        self.client = APIClient()
        resp = self.client.post(
            "/accounts/",
            {
                "first_name": "Rein",
                "second_name": "Rain",
                "account_name": "ReinRain",
                "account_number": 40200,
                "account_type": "saving",
                "branch_name": "Thika",
                "phonenumber": "+254746256084",
            }
        )
        self.assertEqual(resp.status_code, 201)
    
    def test_accounts_update(self):
        """
        tests the put method  in the view
        """
        user= Account.objects.get(first_name= 'Michael')
        view = AccountDetail.as_view()
        factory = APIRequestFactory()
        request = factory.patch('/accounts/', {'first_name':'Mikey'})
        resp = view(request, pk= user.id)
        self.assertEqual(resp.status_code,200)
