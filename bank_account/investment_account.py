from datetime import date, timedelta
from .bank_account import BankAccount, _fmt_currency

class InvestmentAccount(BankAccount):
    """
    InvestmentAccount (A02)

    - TEN_YEARS_AGO constant based on today
    - management_fee (private, default 2.55 if invalid)
    - __str__ prints: Date Created and Management Fee; shows 'Waived' when older than 10 years
    - get_service_charges:
        if account age > 10 years -> BASE
        else -> BASE + management_fee
    """
    TEN_YEARS_AGO: date = date.today() - timedelta(days=int(10 * 365.25))

    def __init__(self, account_number: int, client_number: int, balance: float, date_created, management_fee):
        super().__init__(account_number, client_number, balance, date_created)
        try:
            self.__management_fee = float(management_fee)
        except Exception:
            self.__management_fee = 2.55

    def __str__(self) -> str:
        top = super().__str__().rstrip("\n")
        is_older = self._date_created <= InvestmentAccount.TEN_YEARS_AGO
        fee_str = "Waived" if is_older else _fmt_currency(self.__management_fee)
        extra = f"Date Created: {self._date_created} Management Fee: {fee_str} Account Type: Investment"
        return top + "\n" + extra + "\n"

    def get_service_charges(self) -> float:
        if self._date_created <= InvestmentAccount.TEN_YEARS_AGO:
            return BankAccount.BASE_SERVICE_CHARGE
        return BankAccount.BASE_SERVICE_CHARGE + self.__management_fee