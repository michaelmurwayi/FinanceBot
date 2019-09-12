import unittest
from record_transactions import create_record, create_records, get_records_from_csv

expected_value_for_record = {
    "accountname": "MichaelMurwayi",
    "accounttype": "fixed",
    "branchname": "Thika",
    "phonenumber": "0745454545",
    "transactiontype": "withdraw",
    "accountnumber": 420,
    "transactionamount": 2000.00,
}

expected_value_for_records = [
    {
        "accountname": "MichaelMurwayi",
        "accounttype": "fixed",
        "branchname": "Thika",
        "phonenumber": "07454545454",
        "transactiontype": "withdraw",
        "accountnumber": 420,
        "transactionamount": 2000.00,
    },
    {
        "accountname": "MarkAnderson",
        "accounttype": "savings",
        "branchname": "Mang'u",
        "phonenumber": "0735353535",
        "transactiontype": "deposit",
        "accountnumber": 423,
        "transactionamount": 1057.36,
    },
]


class TestRecordTransactions(unittest.TestCase):
    # maxDiff = None

    def test_create_record(self):
        """ create record from single row"""

        row = [
            "MichaelMurwayi",
            "fixed",
            "Thika",
            "0745454545",
            "withdraw",
            "420",
            "2000.00",
        ]
        self.assertEqual(create_record(row), expected_value_for_record)

    def test_create_records(self):
        """ test creation of records from multiple rows"""

        rows = [
            [
                "MichaelMurwayi",
                "fixed",
                "Thika",
                "07454545454",
                "withdraw",
                "420",
                "2000.00",
            ],
            [
                "MarkAnderson",
                "savings",
                "Mang'u",
                "0735353535",
                "deposit",
                "423",
                "1057.36",
            ],
        ]

        self.assertEqual(create_records(rows), expected_value_for_records)

    def test_get_record(self):
        """ test function to get records from csv file """

        self.assertEqual(
            get_records_from_csv("transaction.csv"), expected_value_for_records
        )

    def test_vadation_for_blank_accountname(self):
        """ validate that account name is not blank"""

        row = ["", "fixed", "Thika", "0745454545", "withdraw", "420", "2000.00"]
        expected_value = (
            "Account Name cannot be  blank",
            {
                "accountname": "",
                "accounttype": "fixed",
                "branchname": "Thika",
                "phonenumber": "0745454545",
                "transactiontype": "withdraw",
                "accountnumber": 420,
                "transactionamount": 2000.00,
            },
        )

        self.assertEqual(create_record(row), expected_value)

    def test_vadation_for_blank_accounttype(self):
        """Validate account type is not blank """

        row = [
            "MichaelMurwayi",
            "",
            "Thika",
            "0745454545",
            "withdraw",
            "420",
            "2000.00",
        ]
        expected_value = (
            "Account Type cannot be  blank",
            {
                "accountname": "MichaelMurwayi",
                "accounttype": "",
                "branchname": "Thika",
                "phonenumber": "0745454545",
                "transactiontype": "withdraw",
                "accountnumber": 420,
                "transactionamount": 2000.00,
            },
        )

        self.assertEqual(create_record(row), expected_value)

    def test_vadation_for_blank_branchname(self):
        """Validate account type is not blank """

        row = [
            "MichaelMurwayi",
            "fixed",
            "",
            "0745454545",
            "withdraw",
            "420",
            "2000.00",
        ]
        expected_value = (
            "branchname cannot be  blank",
            {
                "accountname": "MichaelMurwayi",
                "accounttype": "fixed",
                "branchname": "",
                "phonenumber": "0745454545",
                "transactiontype": "withdraw",
                "accountnumber": 420,
                "transactionamount": 2000.00,
            },
        )
        # import ipdb;ipdb.set_trace()
        self.assertEqual(create_record(row), expected_value)

    def test_vadation_for_blank_phonenumber(self):
        """Validate account type is not blank """

        row = ["MichaelMurwayi", "fixed", "Thika", "", "withdraw", "420", "2000.00"]
        expected_value = (
            "Phonenumber cannot be  blank",
            {
                "accountname": "MichaelMurwayi",
                "accounttype": "fixed",
                "branchname": "Thika",
                "phonenumber": "",
                "transactiontype": "withdraw",
                "accountnumber": 420,
                "transactionamount": 2000.0,
            },
        )

        self.assertEqual(create_record(row), expected_value)

    def test_vadation_for_blank_transactiontype(self):
        """Validate account type is not blank """

        row = ["MichaelMurwayi", "fixed", "Thika", "0745454545", "", "420", "2000.00"]
        expected_value = (
            "Transaction Type cannot be  blank",
            {
                "accountname": "MichaelMurwayi",
                "accounttype": "fixed",
                "branchname": "Thika",
                "phonenumber": "0745454545",
                "transactiontype": "",
                "accountnumber": 420,
                "transactionamount": 2000.00,
            },
        )

        self.assertEqual(create_record(row), expected_value)

    def test_vadation_for_blank_accountnumber(self):
        """Validate account type is not blank """

        row = [
            "MichaelMurwayi",
            "",
            "Thika",
            "0745454545",
            "withdraw",
            "420",
            "2000.00",
        ]
        expected_value = (
            "Account Type cannot be  blank",
            {
                "accountname": "MichaelMurwayi",
                "accounttype": "",
                "branchname": "Thika",
                "phonenumber": "0745454545",
                "transactiontype": "withdraw",
                "accountnumber": 420,
                "transactionamount": 2000.00,
            },
        )

        self.assertEqual(create_record(row), expected_value)


if __name__ == "__main__":
    unittest.main()
