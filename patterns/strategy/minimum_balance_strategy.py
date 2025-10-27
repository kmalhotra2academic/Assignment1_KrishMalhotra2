from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class MinimumBalanceStrategy(ServiceChargeStrategy):
    """
    Savings rule.

    If balance >= minimum_balance -> BASE
    else -> BASE * SERVICE_CHARGE_PREMIUM
    """
    SERVICE_CHARGE_PREMIUM: float = 2.0

    def __init__(self, minimum_balance: float) -> None:
        """Store the required minimum_balance."""
        self.__minimum_balance = float(minimum_balance)

    def calculate_service_charges(self, account) -> float:
        """Return the fee based on balance vs. minimum balance."""
        if account.balance >= self.__minimum_balance:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE
        return ServiceChargeStrategy.BASE_SERVICE_CHARGE * MinimumBalanceStrategy.SERVICE_CHARGE_PREMIUM