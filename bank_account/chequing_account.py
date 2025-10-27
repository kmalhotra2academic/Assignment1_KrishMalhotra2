from .bank_account import BankAccount, _fmt_currency
from patterns.strategy.overdraft_strategy import OverdraftStrategy

class ChequingAccount(BankAccount):
    """
    Chequing account that calculates service charges using OverdraftStrategy.

    Rules (Strategy):
        - If balance >= overdraft_limit → base fee
        - Else → base fee + (overdraft_limit - balance) * overdraft_rate

    Notes:
        The base fee is defined in the strategy layer, not in BankAccount.
    """

    def __init__(self, account_number: int, client_number: int, balance: float, date_created, overdraft_limit, overdraft_rate):  
        """
        Initialize the chequing account and wire up the overdraft strategy.
        """
        super().__init__(account_number, client_number, balance, date_created)
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except Exception:
            self.__overdraft_limit = -100.0
        try:
            self.__overdraft_rate = float(overdraft_rate)
        except Exception:
            self.__overdraft_rate = 0.05

         # Strategy object used to compute fees
        self.__strategy = OverdraftStrategy(self.__overdraft_limit, self.__overdraft_rate)


    def __str__(self) -> str:
        top = super().__str__().rstrip("\n")
        limit = _fmt_currency(self.__overdraft_limit)
        rate_pct = f"{self.__overdraft_rate * 100:.2f}%"
        extra = f"Overdraft Limit: {limit} Overdraft Rate: {rate_pct} Account Type: Chequing"
        return top + "\n" + extra + "\n"

    def get_service_charges(self) -> float:
        return self.__strategy.calculate_service_charges(self)
        #Return the account's service charges.