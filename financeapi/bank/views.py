import sys
import os

sys.path.append("../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bank.settings")
from django.conf import settings
import django

django.setup()
from django.shortcuts import render
from Accounts.models import Users
from Accounts.models import Users
from Accounts.bank import create_account, create_accounts, create_accounts_from_csv

# Create your views here.
def add_user():
    data = create_accounts_from_csv("accounts.csv")
    for items in data:
        user_entry = Users(
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
