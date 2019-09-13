import sys
import os

sys.path.append("../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bank.settings")
import django
django.setup()

from django.conf import settings
from record_transactions import get_records_from_csv
from Transactions.models import Records
def add_record():
	data = get_records_from_csv('transaction.csv')
	
	for items in data:
		Record_entry = Records(
			account_name = items["accountname"], 
    		account_type = items["accounttype"],
    		branch_name = items["branchname"],
    		phonenumber = items["phonenumber"],
    		transaction_type = items["transactiontype"],
    		account_number = items["accountnumber"],
    		transaction_amount = items["transactionamount"]
    	 	)
		Record_entry.save()

if __name__ == '__main__':
	add_record()