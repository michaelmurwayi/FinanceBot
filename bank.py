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
        logging.error("Missing frist name on record= %s", row)
    elif account["last_name"] == "":
        logging.error("Missing second name on the record= %s", row)
    elif type(account["account_number"]) != int:
        logging.error("Account number must be a Number= %s", row)
    elif account["account_type"] != "saving" and row[4] != "fixed":
        logging.error(" provide valid account type= %s", row)
    
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
            accounts.append(create_account(row))
    return accounts


rows = [
    ["Michael", "Murwayi", "MichaelMurwayi", 420, "saving", "Thika", "+254746256084"],
    ["Mark", "Anderson", "MarkAnderson", 421, "fixed", "kajiado", "+254790134102"],
]
print(create_accounts(rows))
