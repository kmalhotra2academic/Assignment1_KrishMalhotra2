import unittest
from datetime import date, timedelta
from bank_account.investment_account import InvestmentAccount
from bank_account.bank_account import BankAccount

class TestInvestmentServiceCharges(unittest.TestCase):
    def test_base_plus_fee_when_newer_than_10_years(self):
        d = date.today() - timedelta(days=365)  # ~1 year old
        acc = InvestmentAccount(30, 100, 100.0, d, 2.55)
        self.assertEqual(BankAccount.BASE_SERVICE_CHARGE + 2.55, round(acc.get_service_charges(), 2))

    def test_base_only_when_older_than_10_years(self):
        d = date.today() - timedelta(days=int(11 * 365.25))  # > 10 years
        acc = InvestmentAccount(31, 100, 100.0, d, 9.99)
        self.assertEqual(BankAccount.BASE_SERVICE_CHARGE, round(acc.get_service_charges(), 2))

if __name__ == "__main__":
    unittest.main()