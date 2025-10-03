import unittest
from datetime import date
from bank_account.chequing_account import ChequingAccount
from bank_account.bank_account import BankAccount

class TestChequingDateCreated(unittest.TestCase):
    def test_date_created_uses_today_when_invalid(self):
        acc = ChequingAccount(10, 100, 0.0, "not-a-date", -100, 0.05)
        self.assertEqual(date.today(), acc._date_created)  # protected per spec

    def test_date_created_passes_through_when_valid(self):
        d = date(2024, 1, 1)
        acc = ChequingAccount(11, 100, 0.0, d, -100, 0.05)
        self.assertEqual(d, acc._date_created)

class TestChequingServiceCharges(unittest.TestCase):
    def test_base_when_balance_at_or_above_limit(self):
        acc = ChequingAccount(12, 100, -100.0, date(2025,1,1), -100.0, 0.05)
        self.assertEqual(BankAccount.BASE_SERVICE_CHARGE, round(acc.get_service_charges(), 2))

    def test_formula_when_below_limit(self):
        acc = ChequingAccount(13, 100, -600.0, date(2025,1,1), -100.0, 0.05)
        # base + (limit - balance)*rate = 0.50 + ((-100) - (-600))*0.05 = 0.50 + 25.00 = 25.50
        self.assertEqual(25.50, round(acc.get_service_charges(), 2))

if __name__ == "__main__":
    unittest.main()