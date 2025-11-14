__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Krish Malhotra"

""""
Client lookup main window.
This window lets the user:
- enter a client number 
- view the client bank account
- double-click an account to open the AccountDetailsWindow.
"""

from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot

from ui_superclasses.lookup_window import LookupWindow
from user_interface.account_details_window import AccountDetailsWindow
from user_interface.manage_data import load_data
from user_interface.manage_data import update_data
from bank_account.bank_account import BankAccount

class ClientLookupWindow(LookupWindow):
    """
    lets a bank employee look up a client by client number
    and see their bank accounts.
    """

    def __init__(self) -> None:
        """lookup window and load client/account data."""
        super().__init__()

        # Load client data once and store.
        self.client_listing, self.accounts = manage_data.load_data()

        # Connect events to their handlers.
        self.lookup_button.clicked.connect(self.on_lookup_client)
        self.client_number_edit.textChanged.connect(self.on_text_changed)
        self.account_table.cellClicked.connect(self.on_select_account)

    @Slot()
    def on_lookup_client(self) -> None:
        """
        Look up the client number entered.
        - Validate input.
        - Show error messages for invalid input.
        - If found, show client info and list their accounts.
        """
        client_text = self.client_number_edit.text().strip()

        # Basic validation.
        if client_text == "":
            QMessageBox.warning(self, "Invalid Data", "Client Number is required.")
            self.reset_display()
            return

        if not client_text.isdigit():
            QMessageBox.warning(self, "Invalid Data", "Client Number must be numeric.")
            self.reset_display()
            return

        client_number = int(client_text)

        # Check if client exists.
        if client_number not in self.client_listing:
            QMessageBox.information(
                self,
                "Client Not Found",
                f"Client Number {client_number} was not found.",
            )
            self.reset_display()
            return

        # Show client details.
        client = self.client_listing[client_number]
        self.client_info_label.setText(str(client).strip())

        # List this client's accounts.
        self.account_table.setRowCount(0)
        row = 0
        for account in self.accounts.values():
            if account.client_number == client.client_number:
                self.account_table.insertRow(row)

                account_item = QTableWidgetItem(str(account.account_number))
                balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)

                self.account_table.setItem(row, 0, account_item)
                self.account_table.setItem(row, 1, balance_item)

                row += 1

        self.account_table.resizeColumnsToContents()

    @Slot(str)
    def on_text_changed(self, text: str) -> None:
        """
        When the client number text changes, clear any previous results.
        """
        self.reset_display()

    @Slot(int, int)
    def on_select_account(self, row: int, column: int) -> None:
        """
        When the user clicks a row in the account table:
        - Get the account number.
        - Validate.
        - Open the AccountDetailsWindow for that account.
        """
        item = self.account_table.item(row, 0)

        if item is None:
            QMessageBox.warning(self, "Invalid Account", "Selected account is invalid.")
            return

        account_text = item.text().strip()
        if account_text == "":
            QMessageBox.warning(self, "Invalid Account", "Selected account is invalid.")
            return

        try:
            account_number = int(account_text)
        except ValueError:
            QMessageBox.warning(self, "Invalid Account", "Selected account is invalid.")
            return

        if account_number not in self.accounts:
            QMessageBox.warning(
                self,
                "Bank Account Does Not Exist",
                "The selected bank account does not exist.",
            )
            return

        account = self.accounts[account_number]

        # Open the details window.
        dialog = AccountDetailsWindow(account)
        # Connect signal and update the table and CSV after a transaction.
        dialog.balance_updated.connect(self.update_data)
        dialog.exec()

    @Slot(BankAccount)
    def update_data(self, account: BankAccount) -> None:
        """
        Slot called when the AccountDetailsWindow sends an updated BankAccount.
        - Update the balance.
        - Update the accounts dictionary.
        """
        # Update table balance for this account.
        for row in range(self.account_table.rowCount()):
            item = self.account_table.item(row, 0)
            if item is not None and item.text().strip() == str(account.account_number):
                balance_item = QTableWidgetItem(f"${account.balance:,.2f}")
                balance_item.setTextAlignment(Qt.AlignRight | Qt.AlignVCenter)
                self.account_table.setItem(row, 1, balance_item)
                break

        # Keep our data in sync.
        self.accounts[account.account_number] = account

        # Write the new balance.
        manage_data.update_data(account)
        
