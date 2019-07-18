import csv


def create_accounts(csvfile):
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
            row = item
    return row  
                    
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
       
    return account

def main():
    create_accounts("accounts.csv")
    get_row("accounts.csv")



if __name__ == "__main__":
    main()
