import sys
sys.path.append('..')
from Accounts.models import Account
from django.test import TestCase
from django.test import Client
from Accounts.serializer import AccountsSerializer
from django.urls import reverse

class TestAccountsViews(TestCase):
    allow_database_queries = True
    """
    test views in account app
    """

    def test_account_list_view(self):
        """
        test the get method in views
        """
        self.client = Client()
        resp = self.client.get("/accounts/")
        self.assertEqual(resp.status_code, 200)
<<<<<<< HEAD
=======

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
        self.client = APIClient()
        resp = self.client.put("/accounts/2/",{"account_number":"420420"})
        import pdb; pdb.set_trace()
        self.assertEqual(resp.status_code, 200) 
>>>>>>> Tests for post method in views
