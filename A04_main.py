__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Krish Malhotra"

# REQUIREMENT - add import statements
import sys

from user_interface.client_lookup_window import ClientLookupWindow

# GIVEN:
from PySide6.QtWidgets import QApplication

# GIVEN:
def main () -> None:
    """
    Main function to start the Client Lookup application.
    """
    app = QApplication(sys.argv)
    mainWindow = ClientLookupWindow()
    mainWindow.show()
    sys.exit(app.exec())
if __name__ == "__main__":
    main()