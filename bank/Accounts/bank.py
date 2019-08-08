import csv


def create_account(row):
    """
    creates a single account from a row of account details
    """

    account = {
        "firstname": row[0],
        "lastname": row[1],
        "accountname": row[2],
        "accountnumber": row[3],
        "accounttype": row[4],
        "branchname": row[5],
        "phonenumber": row[6],
    }
<<<<<<< HEAD
    
=======
>>>>>>> 78a7e4082813e6d67ddbab3671f12fed5ab8b4af
    if account["accounttype"] != "saving" and account["accounttype"] != "fixed":
        return "provide valid account type", row
    elif type(account["accountnumber"]) != int:
        try:
            account["accountnumber"] = int(row[3])
        except ValueError:
            return ("Account number must be a Number", row)

    return check_for_blanks_in_accounts(account)


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


def check_for_blanks_in_accounts(account):
    if account["firstname"] == "":
        return ("firstname is blank", account)
    elif account["lastname"] == "":
        return ("lastname is blank", account)
    elif account["accountname"] == "":
        return ("accountname is blank", account)
    elif account["branchname"] == "":
        return ("branchname is blank", account)
    elif account["phonenumber"] == "":
        return ("phonenumber is blank", account)
    else:
        return account
<<<<<<< HEAD

=======
>>>>>>> 78a7e4082813e6d67ddbab3671f12fed5ab8b4af
