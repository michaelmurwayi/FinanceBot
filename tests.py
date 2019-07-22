import unittest
from bank import create_account, create_accounts, create_accounts_from_csv

maxDiff = None

expected_value_for_account = {
    "first_name": "Michael ",
    "last_name": "Murwayi",
    "account_name": "MichaelMurwayi",
    "account_number": 420,
    "account_type": "saving",
    "branch_name": "Thika",
    "phonenumber": " +254746256084",
}


expected_value_for_accounts = [
    {
        "first_name": "Michael",
        "last_name": "Murwayi",
        "account_name": "MichaelMurwayi",
        "account_number": 420,
        "account_type": "saving",
        "branch_name": "Thika",
        "phonenumber": "+254746256084",
    },
    {
        "first_name": "Mark",
        "last_name": "Anderson",
        "account_name": "MarkAnderson",
        "account_number": 421,
        "account_type": "fixed",
        "branch_name": "kajiado",
        "phonenumber": "+254790134102",
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
            " +254746256084",
        ]
        account = create_account(row)
        self.assertEqual(account, expected_value_for_account)

    def test_create_accounts(self):
        rows = [
            [
                "Michael",
                "Murwayi",
                "MichaelMurwayi",
                420,
                "saving",
                "Thika",
                "+254746256084",
            ],
            [
                "Mark",
                "Anderson",
                "MarkAnderson",
                421,
                "fixed",
                "kajiado",
                "+254790134102",
            ],
        ]
        self.assertEqual(create_accounts(rows), expected_value_for_accounts)

    def test_create_accounts_from_csv(self):
        csv_file = "accounts.csv"
        self.assertEqual(
            create_accounts_from_csv(csv_file), expected_value_for_accounts
        )

    def test_validation_of_firstname(self):
        row = ["", "Murwayi", "MichaelMurwayi", 420, "saving", "Thika", "+254746256084"]
        expected_value = (
            "Missing frist name on record",
            ["", "Murwayi", "MichaelMurwayi", 420, "saving", "Thika", "+254746256084"],
        )
        self.assertEqual(create_account(row), expected_value)

    def test_validation_of_lastname(self):
        row = ["Michael", "", "MichaelMurwayi", 420, "saving", "Thika", "+254746256084"]
        expected_value = (
            "Missing second name on the record ",
            ["Michael", "", "MichaelMurwayi", 420, "saving", "Thika", "+254746256084"],
        )
        self.assertEqual(create_account(row), expected_value)

    def test_validation_of_account_type(self):
        row = [
            "Michael",
            "Murwayi",
            "MichaelMurwayi",
            "420",
            "saving",
            "Thika",
            "+254746256084",
        ]
        expected_value = (
            "Account number must be a Number",
            [
                "Michael",
                "Murwayi",
                "MichaelMurwayi",
                "420",
                "saving",
                "Thika",
                "+254746256084",
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
            "+254746256084",
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
                "+254746256084",
            ],
        )

        self.assertEqual(create_account(row), expected_value)


if __name__ == "__main__":
    unittest.main(module="tests")
