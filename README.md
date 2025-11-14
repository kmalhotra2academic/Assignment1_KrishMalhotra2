# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Krish Malhotra
## Assignment

Assignment 1: BankAccount and Client Classes  
- Implemented Client with private attributes and read-only properties.  
- Implemented BankAccount with deposit, withdraw, and balance validation.  
- Created A01_main.py driver program and basic unit tests.  

Assignment 2: Extending Bank Accounts  
- Added ChequingAccount, SavingsAccount, and InvestmentAccount subclasses.  
- Implemented new behaviors (withdrawal fees, minimum balance, interest).  
- Added corresponding unit test files.    
- Updated Git workflow to use a feature branch for this stage.
Assignment 3:  Strategy Pattern

The Strategy Pattern lets each account type decide its own way of calculating service charges. Instead of putting the rules directly in the account classes, each account uses a separate strategy — like Overdraft, Minimum Balance, or Management Fee — to handle its fees. This keeps the code simple, flexible, and easy to update if bank policies change.

Assignment 4: Implemented a Client Lookup GUI that allows a bank employee to search for a client, view their accounts, and apply transactions using a Qt window.
## Graphical User Interface (Assignment 4)
The main window, `ClientLookupWindow`, lets a user enter a client number, look up the client, and see all of their bank accounts in a table. When the user double-clicks an account, the `AccountDetailsWindow` opens and allows a deposit or withdrawal to be made.

After a successful transaction, the updated balance is shown in both the details window and the main table. The new balance is also written back to `accounts.csv` using the `manage_data` module. This keeps the GUI, data loading, and bank account classes working together in a clear way.


## Encapsulation
Both classes use attributes with read-only properties to protect state.
Validation occurs in IDs, non-blank name
Balance changes are made through deposit, withdraw, update balance to provide a clean api.

## Polymorphism
Polymorphism here means we made BankAccount an abstract base class with an abstract method get_service_charges(). Each subclass has its own calculation: Chequing returns either the base fee or base + (overdraft_limit - balance) * overdraft_rate; Savings returns the base fee or base * SERVICE_CHARGE_PREMIUM; Investment returns the base fee if the account is older than 10 years, otherwise base + management_fee. Because of this, calling get_service_charges() on a BankAccount reference automatically runs the correct subclass logic even though the method name is the same.

