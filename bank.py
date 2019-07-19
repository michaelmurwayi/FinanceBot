import csv

def create_account(row):
    """
    """
    account = {
        'first_name':row[0],
        'last_name':row[1],
        'account_name':row[2],
        'account_number':row[3],
        'account_type':row[4],
        'branch_name':row[5],
        'phonenumber':row[6],
    }   

    return account


def create_accounts(rows):
    accounts = []
    for items in rows:
        # import pdb;pdb.set_trace()
        accounts.append(create_account(items))

    return accounts


def create_accounts_from_csv(csvfile):
    accounts = []
    with open("accounts.csv","r" ) as csvfile:
        reader =csv.reader(csvfile)
        for row in reader:
            accounts.append(create_account(row))
    return accounts
row = [
            "Michael ",
            "Murwayi",
            "MichaelMurwayi",
            "420",
            "saving",
            "Thika",
            " +254746256084",
        ]