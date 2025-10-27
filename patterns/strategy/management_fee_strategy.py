from datetime import date, timedelta
from patterns.strategy.service_charge_strategy import ServiceChargeStrategy

class ManagementFeeStrategy(ServiceChargeStrategy):
    """
    Investment rule.

    Accounts older than TEN_YEARS_AGO pay BASE only.
    Newer accounts pay BASE + management_fee.
    """
    TEN_YEARS_AGO: date = date.today() - timedelta(days=int(365.25 * 10))

    def __init__(self, date_created: date, management_fee: float) -> None:
        """Capture account age and fee inputs for the calculation."""
        self.__date_created = date_created
        self.__management_fee = float(management_fee)

    def calculate_service_charges(self, account) -> float:
        """Return the fee using the 10-year age rule."""
        if self.__date_created <= ManagementFeeStrategy.TEN_YEARS_AGO:
            return ServiceChargeStrategy.BASE_SERVICE_CHARGE
        return ServiceChargeStrategy.BASE_SERVICE_CHARGE + self.__management_fee