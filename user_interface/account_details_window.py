__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Krish Malhotra"

from ui_superclasses.details_window import DetailsWindow
from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal
from bank_account.bank_account import BankAccount
import copy

class AccountDetailsWindow(DetailsWindow):
    """
    A class used to display account details and perform bank account transactions.
    """
    # Signal sent after a successful transaction.
    balance_updated = Signal(BankAccount)

    def __init__(self, account: BankAccount) -> None:
        """
        Shows the ExtendedAccountDetails window.
        Args:
            account: The bank account to be displayed.
        Returns:
            None
        """
        
        super().__init__()

        # no assigned account
        self.account = None

        if isinstance(account, BankAccount):
            # making a copy to avoid modifying the original directly
            self.account = copy.copy(account)
            self.account_number_label.setText(str(self.account.account_number))
            self._update_balance_label()

        # Connect buttons to their handlers.
        self.deposit_button.clicked.connect(self.on_deposit_clicked)
        self.withdraw_button.clicked.connect(self.on_withdraw_clicked)
        self.exit_button.clicked.connect(self.on_exit)

    def _update_balance_label(self) -> None:
        """Refresh the balance label based on the current account balance."""
        if self.account is not None:
            self.balance_label.setText(f"${self.account.balance:,.2f}")

    def _apply_transaction(self, transaction_type: str) -> None:
        """
        Apply a deposit or withdrawal based on transaction_type.

        Steps:
        - Read the amount from transaction_amount_edit.
        - If invalid, show 'Amount must be numeric.' and return.
        - Call deposit or withdraw in a try/except block.
        - On exception, show error message and return.      
        """
        if self.account is None:
            return

        raw_value = self.transaction_amount_edit.text().strip()

        # Validate numeric amount.
        try:
            amount = float(raw_value)
        except ValueError:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Invalid Data")
            msg.setText("Amount must be numeric.")
            msg.exec()
            return

        # Try to apply the transaction.
        try:
            if transaction_type == "Deposit":
                self.account.deposit(amount)
            else:
                self.account.withdraw(amount)
        except Exception as exc:
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle(f"{transaction_type} Failed")
            msg.setText(str(exc))
            msg.exec()
            return

        # Successful transaction.
        self.transaction_amount_edit.clear()
        self._update_balance_label()
        self.balance_updated.emit(self.account)
    
    # Slots
    def on_deposit_clicked(self) -> None:
        """Handle Deposit button click."""
        self._apply_transaction("Deposit")

    def on_withdraw_clicked(self) -> None:
        """Handle Withdraw button click."""
        self._apply_transaction("Withdraw")

    def on_exit(self) -> None:
        """Close the dialog window."""
        self.close()

