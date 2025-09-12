"""
BankAccount class (Part3)
- Private attributes:
    __account_number : int
    __client_number  : int
    __balance        : float
- Properties (read-only) for each attribute
- update_balance(amount): adds to balance if numeric
"""

def _fmt_currency(x: float) -> str:
    return f"${x:,.2f}"

class BankAccount:
    def __init__(self, account_number: int, client_number: int, balance: float) -> None:
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

    def __str__(self) -> str:
        return f"Account Number: {self.__account_number} Balance: {_fmt_currency(self.__balance)}\n"