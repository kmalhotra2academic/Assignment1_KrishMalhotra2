""""
Description: A client program written to verify correctness of 
the BankAccount and Client classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Krish Malhotra"

from bank_account.bank_account import BankAccount
from client.client import Client

def safe_print_exception(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as e:
        print(e)

def main():
    """Test the functionality of the methods encapsulated 
    in the BankAccount and Client classes.
    """ 
    # In the statements coded below, ensure that any statement that could result 
    # in an exception is handled.  When exceptions are 'caught', display the exception 
    # message to the console.

    # 1. Code a statement which creates a valid instance of the Client class.
    # Use your own unique valid values for the inputs to the class.
    try:
        client = Client(1010, "Susan", "Clark", "susanclark@pixell.com")
    except Exception as e:
        print(e); client = None



    # 2. Declare a BankAccount object with an initial value of None.
    bank_account = None
 

    # 3. Using the bank_account object declared in step 2, code a statement 
    # to instantiate the BankAccount object.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use a floating point value for the balance. 
    try:
        if client is None:
            raise RuntimeError("Client instance was not created.")
        bank_account = BankAccount(20019, client.client_number, 500.00)
    except Exception as e:
        print(e)


    # 4. Code a statement which creates an instance of the BankAccount class.
    # Use any integer value for the BankAccount number.
    # Use the client_number used to create the Client object in step 1 for the 
    # BankAccount's client_number. 
    # Use an INVALID value (non-float) for the balance. 
    try:
        invalid_balance_acct = BankAccount(30001, client.client_number if client else 9999, "not-a-float")
    except Exception as e:
        print(e)


    # 5. Code a statement which prints the Client instance created in step 1. 
    # Code a statement which prints the BankAccount instance created in step 3.
    try:
        if client: print(client, end="")
        if bank_account: print(bank_account, end="")
    except Exception as e:
        print(e)

    if bank_account: #the if statement for each question below)

    # 6. Attempt to deposit a non-numeric value into the BankAccount create in step 3. 
       
        safe_print_exception(bank_account.deposit, "twenty")


    # 7. Attempt to deposit a negative value into the BankAccount create in step 3. 
       
        safe_print_exception(bank_account.deposit, -50.00)


    # 8. Attempt to withdraw a valid amount of your choice from the BankAccount create in step 3. 
       
        safe_print_exception(bank_account.withdraw, 100.00)


    # 9. Attempt to withdraw a non-numeric value from the BankAccount create in step 3. 
       
        safe_print_exception(bank_account.withdraw, "ten")


    # 10. Attempt to withdraw a negative value from the BankAccount create in step 3. 

        safe_print_exception(bank_account.withdraw, -25.00)

    # 11. Attempt to withdraw a value from the BankAccount create in step 3 which 
    # exceeds the current balance of the account. 

        safe_print_exception(bank_account.withdraw, 10000.00)
 

    # 12. Code a statement which prints the BankAccount instance created in step 3. 

        print(bank_account, end="")


if __name__ == "__main__":
    main()
