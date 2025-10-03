"""
Description: A client program written to verify correctness of 
the BankAccount sub classes.
"""
__author__ = "ACE Faculty"
__version__ = "1.0.0"
__credits__ = "Krish Malhotra"

# 1.  Import all BankAccount types using the bank_account package
#     Import date from datetime
from bank_account import ChequingAccount, SavingsAccount, InvestmentAccount, BankAccount
from datetime import date


# 2. Create an instance of a ChequingAccount with values of your 
# choice including a balance which is below the overdraft limit.
chequing = ChequingAccount(
    account_number=1001,
    client_number=2001,
    balance=-150.00,              # below the overdraft limit (-100.00)
    date_created=date(2025, 1, 1),
    overdraft_limit=-100.00,
    overdraft_rate=0.05
)

# 3. Print the ChequingAccount created in step 2.
# 3b. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
print(chequing, end="")
print(f"Service Charges: ${chequing.get_service_charges():.2f}")


# 4a. Use ChequingAccount instance created in step 2 to deposit 
# enough money into the chequing account to avoid overdraft fees.
# 4b. Print the ChequingAccount
# 4c. Print the service charges amount if calculated based on the 
# current state of the ChequingAccount created in step 2.
chequing.deposit(75.00)  # -150.00 + 75.00 = -75.00 (now at/above overdraft limit → base charge)
print(chequing, end="")
print(f"Service Charges: ${chequing.get_service_charges():.2f}")

print("===================================================")
# 5. Create an instance of a SavingsAccount with values of your 
# choice including a balance which is above the minimum balance.
savings = SavingsAccount(
    account_number=1002,
    client_number=2002,
    balance=100.00,               # above minimum
    date_created=date(2025, 1, 1),
    minimum_balance=50.00
)

# 6. Print the SavingsAccount created in step 5.
# 6b. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
print(savings, end="")
print(f"Service Charges: ${savings.get_service_charges():.2f}")

# 7a. Use this SavingsAccount instance created in step 5 to withdraw 
# enough money from the savings account to cause the balance to fall 
# below the minimum balance.
# 7b. Print the SavingsAccount.
# 7c. Print the service charges amount if calculated based on the 
# current state of the SavingsAccount created in step 5.
savings.withdraw(60.00)  # 100.00 - 60.00 = 40.00 (< 50.00 → premium charge)
print(savings, end="")
print(f"Service Charges: ${savings.get_service_charges():.2f}")


print("===================================================")
# 8. Create an instance of an InvestmentAccount with values of your 
# choice including a date created within the last 10 years.
investment_new = InvestmentAccount(
    account_number=1003,
    client_number=2003,
    balance=100.00,
    date_created=date(2022, 1, 1),  # within last 10 years
    management_fee=2.55
)

# 9a. Print the InvestmentAccount created in step 8.
# 9b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 8.
print(investment_new, end="")
print(f"Service Charges: ${investment_new.get_service_charges():.2f}")

# 10. Create an instance of an InvestmentAccount with values of your 
# choice including a date created prior to 10 years ago.
investment_old = InvestmentAccount(
    account_number=1004,
    client_number=2004,
    balance=100.00,
    date_created=date(2013, 1, 1),  # prior to 10 years ago
    management_fee=9.99
)

# 11a. Print the InvestmentAccount created in step 10.
# 11b. Print the service charges amount if calculated based on the 
# current state of the InvestmentAccount created in step 10.
print(investment_old, end="")
print(f"Service Charges: ${investment_old.get_service_charges():.2f}")

print("===================================================")

# 12. Update the balance of each account created in steps 2, 5, 8 and 10 
# by using the withdraw method of the superclass and withdrawing 
# the service charges determined by each instance invoking the 
# polymorphic get_service_charges method.
for account in (chequing, savings, investment_new, investment_old):
    charge = account.get_service_charges()
    try:
        account.withdraw(charge)
    except Exception as e:
        # If a withdraw is not permitted (e.g., insufficient funds), show the message.
        print(e)


# 13. Print each of the bank account objects created in steps 2, 5, 8 and 10.
print(chequing, end="")
print(savings, end="")
print(investment_new, end="")
print(investment_old, end="")
