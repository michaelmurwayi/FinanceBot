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
