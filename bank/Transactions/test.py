import unittest
from record_transactions import create_record, create_records, get_records_from_csv

expected_value_for_record = {
    "accountname":"MichaelMurwayi",
    "accounttype":"fixed",
    "branchname":"Thika",
    "phonenumber":"0745454545",
    "transactiontype":"withdraw",
    "accountnumber ":"420",
    "transactionamount":2000.00,
}

expected_value_for_records = [
    {
        "accountname":"MichaelMurwayi",
        "accounttype":"fixed",
        "branchname":"Thika",
        "phonenumber":"07454545454",
        "transactiontype":"withdraw",
        "accountnumber ":"420",
        "transactionamount":2000.00,
    },
    {
        "accountname":"MarkAnderson",
        "accounttype":"savings",
        "branchname":"Mang'u",
        "phonenumber":"0735353535",
        "transactiontype":"deposit",
        "accountnumber ":"423",
        "transactionamount":1057.36,
    },
]


class TestRecordTransactions(unittest.TestCase):
    maxDiff = None

    def test_create_record(self):
        # import ipdb;ipdb.set_trace()
        row = [
            "MichaelMurwayi",
            "fixed",
            "Thika",
            "0745454545",
            "withdraw",
            "420",
            2000.00,
        ]
        self.assertEqual(create_record(row), expected_value_for_record)

    def test_create_records(self):
        rows = [
            [
                "MichaelMurwayi",
                "fixed",
                "Thika",
                "07454545454",
                "withdraw",
                "420",
                2000.00,
            ],
            [
                "MarkAnderson",
                "savings",
                "Mang'u",
                "0735353535",
                "deposit",
                "423",
                1057.36,
            ],
        ]

        self.assertEqual(create_records(rows), expected_value_for_records)

    def test_get_record(self):
        self.assertEqual(
            get_records_from_csv("transaction.csv"), expected_value_for_records
        )


if __name__ == "__main__":
    unittest.main()
