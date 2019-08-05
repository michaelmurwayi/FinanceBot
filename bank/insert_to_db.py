import sys
import os

sys.path.append("../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bank.settings")
from django.conf import settings
import django
django.setup()
from Accounts.models import Accounts
from Accounts.bank import create_accounts_from_csv


def add_user():
    data = create_accounts_from_csv("accounts.csv")
    for items in data:
    
        user_entry = Accounts(
            first_name=items["firstname"],
            second_name=items["lastname"],
            account_name=items["accountname"],
            account_number=items["accountnumber"],
            account_type=items["accounttype"],
            branch_name=items["branchname"],
            phonenumber=items["phonenumber"],
            
        )
        user_entry.save()


if __name__ == "__main__":
    add_user()
