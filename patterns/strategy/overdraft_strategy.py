from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class OverdraftStrategy(ServiceChargeStrategy):
    """
    Chequing rule.

    If balance >= overdraft_limit:
        return BASE_SERVICE_CHARGE
    else:
        return BASE + (overdraft_limit - balance) * overdraft_rate
    """
    def __init__(self, overdraft_limit: float, overdraft_rate: float) -> None:
        """Store rule parameters for later calculations."""
        self.__overdraft_limit = float(overdraft_limit)
        self.__overdraft_rate = float(overdraft_rate)

    def calculate_service_charges(self, account) -> float:
        """Return the fee based on current balance and the overdraft rule."""
        if account.balance >= self.__overdraft_limit:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE
        return ServiceChargeStrategy.BASE_SERVICE_CHARGE + (self.__overdraft_limit - account.balance) * self.__overdraft_rate