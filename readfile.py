import csv

Account=[
    {
        "First_Name": str,
        "Last_Name":str,
        "Account_Name":str,
        "Account_Number":int,
        "Account_Type":str,
        "Branch_Name":str,
        "PhoneNumber":str,
    }
]
for item in Account:
    name = item["First_Name"]
    print(name) 
with open('accounts.csv', 'r') as csvFile:
    reader = csv.reader(open("accounts.csv","r"))
    for row in reader:
        for item in Account:
            item["First_Name"] = row[0]
            item["Last_Name"] = row[1]
            item["Account_Name"] = row[2]
            item["Account_Number"] = row[3]
            item["Account_Type"] = row[4]
            item["Branch_Name"] = row[5]
            item["PhoneNumber"] = row[6]
            print(Account)