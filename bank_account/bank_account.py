"""
Changes from A01 → A02 (BankAccount)**
- Made `BankAccount` an **abstract base class**.
- Added protected `self._date_created: date` with validation (defaults to `date.today()` if not a `date`).
- Declared abstract `get_service_charges()` to force subclass polymorphism.
- Kept deposit/withdraw/update_balance and `__str__` (unchanged formatting).
Abstract superclass for all bank accounts.
BankAccount class (Part3)
- Private attributes:
    __account_number : int
    __client_number  : int
    __balance        : float
- Properties (read-only) for each attribute
- update_balance(amount): adds to balance if numeric
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import date
from typing import Any 
from patterns.observer.subject import Subject


def _fmt_currency(x: float) -> str:
    """Return `x` formatted as currency with two decimals."""
    return f"${x:,.2f}"

class BankAccount(Subject, ABC):
    """Abstract bank account.


        Attributes
        ----------
        BASE_SERVICE_CHARGE : float
        Flat fee used by subclasses while computing service charges.
        _date_created : date (protected)
        Creation date for the account. Defaults to `date.today()` if invalid input.
        __account_number, __client_number, __balance : private
        Core identifiers and current balance.
        """
    BASE_SERVICE_CHARGE: float = 0.50
    LARGE_TRANSACTION_THRESHOLD: float = 9_999.99
    LOW_BALANCE_LEVEL: float = 50.0
    def __init__(self, account_number: int, client_number: int, balance: float, date_created: date) -> None:
        if not isinstance(account_number, int):
            raise ValueError("Account number must be an integer.")
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        # Keep it minimal: accept balance convertible to float; if not, set to 0.0
        try:
            bal = float(balance)
        except Exception:
            bal = 0.0

        self.__account_number = account_number
        self.__client_number = client_number
        self.__balance = bal
        self._date_created: date = date_created if isinstance(date_created, date) else date.today()

    @property
    def account_number(self) -> int:
        return self.__account_number

    @property
    def client_number(self) -> int:
        return self.__client_number

    @property
    def balance(self) -> float:
        return self.__balance

    def update_balance(self, amount: float) -> None:
        try:
            self.__balance += float(amount)
        except Exception:
            pass  # minimal: ignore bad input here

    def deposit(self, amount: float) -> None:
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Deposit amount: {amount} must be numeric.")
        amt = float(amount)
        if amt <= 0:
            raise ValueError(f"Deposit amount: {_fmt_currency(amt)} must be positive.")
        self.update_balance(amt)

    def withdraw(self, amount: float) -> None:
        """
        Withdraw a positive amount not exceeding the current balance.

        Raises:
            ValueError: if amount is non-numeric, not positive, or exceeds balance.
            """
        if not isinstance(amount, (int, float)):
            raise ValueError(f"Withdraw amount: {amount} must be numeric.")
        amt = float(amount)
        if amt <= 0:
            raise ValueError(f"Withdraw amount: {_fmt_currency(amt)} must be positive.")
        if amt > self.__balance:
            raise ValueError(
                f"Withdraw amount: {_fmt_currency(amt)} must not exceed the account balance: {_fmt_currency(self.__balance)}."
            )
        self.update_balance(-amt)

        if self.__balance < BankAccount.LOW_BALANCE_LEVEL:
            self.notify(f"Low balance alert on account #{self.__account_number}: {_fmt_currency(self.__balance)} remaining.")

    def __str__(self) -> str:
        return f"Account Number: {self.__account_number} Balance: {_fmt_currency(self.__balance)}\n"
    
    #added abstract method for service charges
    @abstractmethod
    def get_service_charges(self) -> float:
        #Return the account's service charges.      
        pass