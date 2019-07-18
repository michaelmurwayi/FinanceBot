import csv


def create_accounts(csvfile):
    global accounts 
    accounts= {
            "first_name": str,
            "last_name": str,
            "account_name": str,
            "account_number": str,
            "account_type": str,
            "branch_name": str,
            "phonenumber": str

        } 
    
    with open(csvfile, "r") as data:
        reader = csv.reader(data)
        for row in reader:
            accounts["first_name"] = row[0]
            accounts["last_name"]= row[1]
            accounts["account_name"]= row[2]
            accounts["account_number"]= row[3]
            accounts["account_type"]= row[4]
            accounts["branch_name"]= row[5]
            accounts["phonenumber"]= row[6]
            print(accounts)
            return accounts

def get_row(file):
    with open("accounts.csv", "r") as data:
        reader = csv.reader(data)
        for item in reader:
            global row
            row = item
            return row  
            
        


def create_account(row):
    account = {
            "first_name":str ,
            "last_name": str,
            "account_name": str,
            "account_number": str,
            "account_type": str ,
            "branch_name": str,
            "phonenumber": str,
        }
    for key, value in account.items():
        if key ==  "first_name":
            account["first_name"] = row[0]
        elif key == "last_name":
            account["last_name"] = row[1]
        elif key == "account_name":
            account["account_name"] = row[2]
        elif key == "account_number":
            account["account_number"] = row[3]
        elif key == "account_type":
            account["account_type"] = row[4]
        elif key == "branch_name":
            account["branch_name"] = row[5]
        elif key == "phonenumber":
            account["phonenumber"] = row[6]
            print(account)    
            return account

def main():
    create_accounts("accounts.csv")
    get_row("accounts.csv")
    create_account(row)


if __name__ == "__main__":
    main()
