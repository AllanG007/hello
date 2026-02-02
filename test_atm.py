import unittest
from atm import atm_withdrawal

class TestATMWithdrawal(unittest.TestCase):

    def test_insufficient_funds(self):
        message, new_balance = atm_withdrawal(100, 200)
        self.assertEqual(message, "Insufficient Funds")
        self.assertEqual(new_balance, 100)

    def test_invalid_amount(self):
        message, new_balance = atm_withdrawal(100, 0)
        self.assertEqual(message, "Invalid Amount")
        self.assertEqual(new_balance, 100)

    def test_successful_transaction(self):
        message, new_balance = atm_withdrawal(100, 50)
        self.assertEqual(message, "Transaction Successful")
        self.assertEqual(new_balance, 50)

if __name__ == "__main__":
    unittest.main()