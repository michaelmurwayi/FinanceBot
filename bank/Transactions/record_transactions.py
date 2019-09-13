import csv

def create_record(row):
	""" Create record into a dictionary"""
	record = {
	"accountname": row[0],
	"accounttype": row[1],
	"branchname": row[2],
	"phonenumber": row[3],
	"transactiontype": row[4],
	"accountnumber": int(row[5]),
	"transactionamount": float(row[6]),
	}
	
	return validation_for_blanks(record)


def create_records(rows):
	"""create records from rows of transactions"""
	records = []
	for items in rows:
		records.append(create_record(items))
	return records

def get_records_from_csv(csv_file):
	""" creates records from csv file"""

	with open(csv_file, "r") as csv_file:
		records = []
		csv_reader = csv.reader(csv_file)
		for row in csv_reader:
			records.append(create_record(row)
            
	return records

def validation_for_blanks(record):
    """ check for blanks in data recieved from files"""

    if record["accountname"] == "":
        return("Account Name cannot be  blank", record)
    elif record["accounttype"] == "":
        return ("Account Type cannot be  blank", record)
    elif record["branchname"] == "":
        return ("branchname cannot be  blank", record)
    elif record["phonenumber"] == "":
        return ("Phonenumber cannot be  blank", record)
    elif record["transactiontype"] == "":
        return ("Transaction Type cannot be  blank", record)
 
    return record

if __name__ == '__main__':
	row = ['', 'fixed', '420', '2000.00', 'withdraw', 'Thika', '0745454545']
	rows = [['MichaelMurwayi', 'fixed', '420', '2000.00', 'withdraw', 'Thika', '0745454545'],['MarkIndasi', 'savings', '423', '1057.36', 'deposit', "Mang'u", '0735353535']]
	create_record(row)
	# create_records(rows)
	# get_records_from_csv('transaction.csv')