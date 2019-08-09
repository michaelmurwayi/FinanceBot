import unittest
import sys

sys.path.append("../")
from Accounts.bank import create_account, create_accounts, create_accounts_from_csv


expected_value_for_account = {
    "firstname": "Michael ",
    "accountname": "MichaelMurwayi",
    "lastname": "Murwayi",
    "accountnumber": 420,
    "accounttype": "saving",
    "branchname": "Thika",
    "phonenumber": "0746256084",
}


expected_value_for_accounts = [
    {
        "firstname": "Michael",
        "lastname": "Murwayi",
        "accountname": "MichaelMurwayi",
        "accountnumber": 420,
        "accounttype": "saving",
        "branchname": "Thika",
        "phonenumber": "0746256084",
    },
    {
        "firstname": "Mark",
        "lastname": "Anderson",
        "accountname": "MarkAnderson",
        "accountnumber": 421,
        "accounttype": "fixed",
        "branchname": "kajiado",
        "phonenumber": "0790134102",
    },
]


class TestBank(unittest.TestCase):
    def test_create_account(self):
        row = [
            "Michael ",
            "Murwayi",
            "MichaelMurwayi",
            420,
            "saving",
            "Thika",
            "0746256084",
        ]
        self.assertEqual(create_account(row), expected_value_for_account)

    def test_create_accounts(self):
        rows = [
            [
                "Michael",
                "Murwayi",
                "MichaelMurwayi",
                420,
                "saving",
                "Thika",
                "0746256084",
            ],
            ["Mark", "Anderson", "MarkAnderson", 421, "fixed", "kajiado", "0790134102"],
        ]
        self.assertEqual(create_accounts(rows), expected_value_for_accounts)

    def test_create_accounts_from_csv(self):
        csv_file = "../accounts.csv"
        self.assertEqual(
            create_accounts_from_csv(csv_file), expected_value_for_accounts
        )

    def test_validation_of_firstname(self):
        row = ["", "Murwayi", "MichaelMurwayi", 420, "saving", "Thika", "0746256084"]
        expected_value = (
            "firstname is blank",
            {
                "firstname": "",
                "lastname": "Murwayi",
                "accountname": "MichaelMurwayi",
                "accountnumber": 420,
                "accounttype": "saving",
                "branchname": "Thika",
                "phonenumber": "0746256084",
            },
        )

        self.assertEqual(create_account(row), expected_value)

    def test_validation_of_lastname(self):
        row = ["Michael", "", "MichaelMurwayi", 420, "saving", "Thika", "0746256084"]
        expected_value = (
            "lastname is blank",
            {
                "firstname": "Michael",
                "lastname": "",
                "accountname": "MichaelMurwayi",
                "accountnumber": 420,
                "accounttype": "saving",
                "branchname": "Thika",
                "phonenumber": "0746256084",
            },
        )
        self.assertEqual(create_account(row), expected_value)

    def test_validation_of_account_number(self):
        row = [
            "Michael",
            "Murwayi",
            "MichaelMurwayi",
            "baba",
            "saving",
            "Thika",
            "0746256084",
        ]
        expected_value = (
            "Account number must be a Number",
            [
                "Michael",
                "Murwayi",
                "MichaelMurwayi",
                "baba",
                "saving",
                "Thika",
                "0746256084",
            ],
        )

        self.assertEqual(create_account(row), expected_value)

    def test_validation_of_account_type(self):
        row = [
            "Michael",
            "Murwayi",
            "MichaelMurwayi",
            420,
            "save",
            "Thika",
            "0746256084",
        ]
        expected_value = (
            "provide valid account type",
            [
                "Michael",
                "Murwayi",
                "MichaelMurwayi",
                420,
                "save",
                "Thika",
                "0746256084",
            ],
        )

        self.assertEqual(create_account(row), expected_value)


if __name__ == "__main__":
    unittest.main(module="tests")
