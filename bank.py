import csv
import logging


def create_account(row):
    """
    creates a single account from a row of account details
    """

    account = {
        "first_name": row[0],
        "last_name": row[1],
        "account_name": row[2],
        "account_number": int(row[3]),
        "account_type": row[4],
        "branch_name": row[5],
        "phonenumber": row[6],
    }
    if account["first_name"] == "":
        return "Missing frist name on record", row
    elif account["last_name"] == "":
        return "Missing second name on the record ", row
    elif type(account["account_number"]) != int:
        return "Account number must be a Number", row
    elif account["account_type"] != "saving" and account["account_type"] != "fixed":
        return "provide valid account type", row
    else:

        return account


def create_accounts(rows):
    """
    creates a list of accounts from rows of account details
    """
    accounts = []
    for items in rows:
        accounts.append(create_account(items))

    return accounts


def create_accounts_from_csv(csvfile):
    accounts = []
    with open(csvfile, "r") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            # import pdb;pdb.set_trace()
            accounts.append(create_account(row))
    return accounts
