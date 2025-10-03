import unittest
from datetime import date
from bank_account.savings_account import SavingsAccount
from bank_account.bank_account import BankAccount

class TestSavingsServiceCharges(unittest.TestCase):
    def test_base_when_at_or_above_minimum(self):
        acc = SavingsAccount(20, 100, 100.0, date(2025,1,1), 50.0)
        self.assertEqual(BankAccount.BASE_SERVICE_CHARGE, round(acc.get_service_charges(), 2))

    def test_premium_when_below_minimum(self):
        acc = SavingsAccount(21, 100, 25.0, date(2025,1,1), 50.0)
        expected = BankAccount.BASE_SERVICE_CHARGE * SavingsAccount.SERVICE_CHARGE_PREMIUM
        self.assertEqual(expected, round(acc.get_service_charges(), 2))

if __name__ == "__main__":
    unittest.main()