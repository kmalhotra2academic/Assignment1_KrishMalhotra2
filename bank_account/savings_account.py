from .bank_account import BankAccount, _fmt_currency 

class SavingsAccount(BankAccount):
    """
    SavingsAccount (A02):
    - SERVICE_CHARGE_PREMIUM = 2.0
    - minimum_balance (private, default 50.0 if invalid)
    - __str__ prints minimum_balance (currency) and account type
    - get_service_charges: base if balance >= minimum_balance, else base * 2.0
    """
    SERVICE_CHARGE_PREMIUM: float = 2.0

    def __init__(self, account_number: int, client_number: int, balance: float, date_created, minimum_balance):
        super().__init__(account_number, client_number, balance, date_created)
        try:
            self.__minimum_balance = float(minimum_balance)
        except Exception:
            self.__minimum_balance = 50.0

    def __str__(self) -> str:
        top = super().__str__().rstrip("\n")
        extra = f"Minimum Balance: {_fmt_currency(self.__minimum_balance)} Account Type: Savings"
        return top + "\n" + extra + "\n"

    def get_service_charges(self) -> float:
        if self.balance >= self.__minimum_balance:
            return BankAccount.BASE_SERVICE_CHARGE
        return BankAccount.BASE_SERVICE_CHARGE * SavingsAccount.SERVICE_CHARGE_PREMIUM