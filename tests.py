"""
Import python unittest module
"""
import unittest
from bank import create_account, create_accounts, create_accounts_from_csv

unittest.TestCase.maxDiff = None

EXPECTEDACCOUNT = {
    "firstname": "Michael ",
    "accountname": "MichaelMurwayi",
    "lastname": "Murwayi",
    "accountnumber": 420,
    "accounttype": "saving",
    "branchname": "Thika",
    "phonenumber": "0746256084",
}
EXPECTEDACCOUNTS = [
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
    """
    tests for functions in bank.py file
    """

    def test_create_account(self):
        """
        Tests create account :converts row to dictionary
        """
        row = [
            "Michael ",
            "Murwayi",
            "MichaelMurwayi",
            420,
            "saving",
            "Thika",
            "0746256084",
        ]
        self.assertEqual(create_account(row), EXPECTEDACCOUNT)

    def test_create_accounts(self):
        """
        Tests create accounts :converts rows into list
        """
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
        self.assertEqual(create_accounts(rows), EXPECTEDACCOUNTS)

    def test_create_accounts_from_csv(self):
        """
        Tests create account from csv: takes file and return list of accounts
        """
        csv_file = "accounts.csv"
        self.assertEqual(create_accounts_from_csv(csv_file), EXPECTEDACCOUNTS)

    def test_validation_of_firstname(self):
        """
        tests for missing firstname in accounts dictionary
        """
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
        """
        tests for missing secondname in accounts dictionary
        """
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

    def test_validation_of_account_type(self):
        """
        self.assertEqual(create_account(row), expected_value)
        tests if account type provided is valid
        """
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

    def test_validation_of_account_number(self):
        """
        tests if accountnumber is integer in accounts dictionary
        """
        row = [
            "Michael",
            "Murwayi",
            "MichaelMurwayi",
            "baba",
            "fixed",
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
                "fixed",
                "Thika",
                "0746256084",
            ],
        )
        
        self.assertEqual(create_account(row), expected_value)


if __name__ == "__main__":
    unittest.main(module="tests")
