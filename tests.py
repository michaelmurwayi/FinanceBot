import unittest
import csv
import readfile

class TestReadFile(unittest.TestCase):
    def test_ReadFile(self)-> None:
        options = "accounts.csv"    
        self.assertEqual(readfile.ReadFile(options), 
        [
            {
                "First_Name": "Michael ",
                "Last_Name": " Murwayi",
                "Account_Name": "MichaelMurwayi",
                "Account_Number": "420",
                "Account_Type": "saving",
                "Branch_Name": "Thika",
                "PhoneNumber": " +254746256084",
            }
        ]
        )

if __name__ == "__main__":
    unittest.main(module="tests")