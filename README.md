# Intermediate Software Development Automated Teller Project
This project will be developed over the course of several assignments.  Each assignment will build on the work done in the previous assignment(s).  Ultimately, an entire system will be created to manage bank transactions for clients who have one or more bank accounts.

## Author
Krish Malhotra

## Assignment
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

## Encapsulation
Both classes use attributes with read-only properties to protect state.
Validation occurs in IDs, non-blank name
Balance changes are made through deposit, withdraw, update balance to provide a clean api.