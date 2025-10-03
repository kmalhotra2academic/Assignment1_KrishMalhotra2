"""
Description: Unit tests for the BankAccount class.
Author: ACE Faculty
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_bank_account.py
"""
import unittest
from bank_account.bank_account import BankAccount

@unittest.skip("BankAccount is abstract in A02; behavior is tested via subclasses.")
class TestBankAccount(unittest.TestCase):
    pass

