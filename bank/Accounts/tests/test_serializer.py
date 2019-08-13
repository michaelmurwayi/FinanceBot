import sys
sys.path.append('..')
from django.test import TestCase
from Accounts.serializer import AccountsSerializer
from Accounts.models import Account

class TestSerializer(TestCase):
   
# test the serialization function
   

    def test_AccountsSerializer(self):
        objects = Account(
            first_name="mike",
            second_name="Murwayi",
            account_name="mikemurwayi",
            account_number=40021,
            account_type="fixed",
            branch_name="thika",
            phonenumber="0707070707",
        )
        serializer = AccountsSerializer(objects)
        expected = {
            "id": None,
            "first_name": "mike",
            "second_name": "Murwayi",
            "account_name": "mikemurwayi",
            "account_number": 40021,
            "account_type": "fixed",
            "branch_name": "thika",
            "phonenumber": "0707070707",
        }

        self.assertEqual(serializer.data, expected)


