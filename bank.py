def create_account(row):
    account = {
            "first_name":row[0] ,
            "last_name": row[1],
            "account_name": row[2],
            "account_number": row[3],
            "account_type": row[4],
            "branch_name": row[5],
            "phonenumber": row[6],
        }
    # print(account)
    return account
def create_accounts(rows):
    accounts = []
    for items in rows:
        accounts.append(create_account(items))
    return accounts

       
