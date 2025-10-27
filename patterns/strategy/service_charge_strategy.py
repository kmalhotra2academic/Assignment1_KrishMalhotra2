class ServiceChargeStrategy:
    """
    Base class for service charge rules.

    Constant:
        BASE_SERVICE_CHARGE (float): default fee used across strategies.

    Method to override:
        calculate_service_charges(account) -> float
    """
    BASE_SERVICE_CHARGE: float = 0.50

    def calculate_service_charges(self, account) -> float:
        """Compute the charge for the given account (override in subclasses)."""
        raise NotImplementedError("Strategy must implement calculate_service_charges().")