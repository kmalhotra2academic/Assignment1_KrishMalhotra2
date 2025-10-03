from .bank_account import BankAccount, _money

class ChequingAccount(BankAccount):
    """
    ChequingAccount (A02):
    - overdraft_limit and overdraft_rate (private)
    - __str__ prints limit (currency), rate (percent), and account type
    - get_service_charges: base if balance >= overdraft_limit,
      else base + (overdraft_limit - balance) * overdraft_rate
    """

    def __init__(self, account_number: int, client_number: int, balance: float, date_created,
                 overdraft_limit, overdraft_rate):
        super().__init__(account_number, client_number, balance, date_created)
        try:
            self.__overdraft_limit = float(overdraft_limit)
        except Exception:
            self.__overdraft_limit = -100.0
        try:
            self.__overdraft_rate = float(overdraft_rate)
        except Exception:
            self.__overdraft_rate = 0.05

    def __str__(self) -> str:
        top = super().__str__().rstrip("\n")
        limit = _money(self.__overdraft_limit)
        rate_pct = f"{self.__overdraft_rate * 100:.2f}%"
        extra = f"Overdraft Limit: {limit} Overdraft Rate: {rate_pct} Account Type: Chequing"
        return top + "\n" + extra + "\n"

    def get_service_charges(self) -> float:
        if self.balance >= self.__overdraft_limit:
            return BankAccount.BASE_SERVICE_CHARGE
        return BankAccount.BASE_SERVICE_CHARGE + (self.__overdraft_limit - self.balance) * self.__overdraft_rate
        #Return the account's service charges.