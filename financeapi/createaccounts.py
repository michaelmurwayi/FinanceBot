import mysql.connector
from bank import *

db = mysql.connector.connect(
    host="localhost", user="huncho", password="c11h28no3", database="bank"
)

cursor = db.cursor()


def create_table_in_db():
    import ipdb;ipdb.set_trace()
    cursor.execute(
        "CREATE TABLE account(firstname varchar(255),lastname varchar(255),accountname varchar(255),accountnumber int, accounttype varchar(255), branchname varchar(255),phonenumber varchar(255))"
    )


def insert_data_to_db():
    data = create_accounts_from_csv("accounts.csv")
    for items in data:
        sql = "INSERT INTO account VALUES ('%s','%s','%s','%d','%s','%s','%s')" % (
            items["firstname"],
            items["lastname"],
            items["accountname"],
            items["accountnumber"],
            items["accounttype"],
            items["branchname"],
            items["phonenumber"],
        )
        cursor.execute(sql)
        db.commit()


create_table_in_db()
insert_data_to_db()
