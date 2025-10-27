from .bank_account import BankAccount, _fmt_currency 
from patterns.strategy.minimum_balance_strategy import MinimumBalanceStrategy


class SavingsAccount(BankAccount):
    """
    SavingsAccount (A03)
    
    Uses the MinimumBalanceStrategy to determine service charges.

    Rules (Strategy):
        - If balance >= minimum_balance → base fee
        - Otherwise → base fee * SERVICE_CHARGE_PREMIUM (2.0)

    Notes:
        Minimum balance defaults to 50.0 if input is invalid.
    """
    SERVICE_CHARGE_PREMIUM: float = 2.0

    def __init__(self, account_number: int, client_number: int, balance: float, date_created, minimum_balance):
        super().__init__(account_number, client_number, balance, date_created)
        try:
            self.__minimum_balance = float(minimum_balance)
        except Exception:
            self.__minimum_balance = 50.0
       
        # Strategy used to calculate service charges
        self.__strategy = MinimumBalanceStrategy(self.__minimum_balance)
   
    def __str__(self) -> str:
        top = super().__str__().rstrip("\n")
        extra = f"Minimum Balance: {_fmt_currency(self.__minimum_balance)} Account Type: Savings"
        return top + "\n" + extra + "\n"

    def get_service_charges(self) -> float:
        return self.__strategy.calculate_service_charges(self)
        #Return the account's service charges.