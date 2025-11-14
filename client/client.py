"""
Client class (Part 1)
- Private attributes per diagram:
    __client_number : int
    __first_name    : str
    __last_name     : str
    __email_address : str
- Read-only properties for each attribute
- __str__ returns: "{last}, {first} [{client_number}] - {email}\n"
"""
from patterns.observer.observer import Observer
        
class Client:
    """
        Represents a bank customer and acts as an Observer in the system.
        When the bank sends a notification (like a low balance or large deposit),
        the client receives it through the update() method.
        """
    def __init__(self, client_number: int, first_name: str, last_name: str, email_address: str) -> None:
        if not isinstance(client_number, int):
            raise ValueError("Client number must be an integer.")
        if not isinstance(first_name, str) or first_name.strip() == "":
            raise ValueError("First name must be a non-blank string.")
        if not isinstance(last_name, str) or last_name.strip() == "":
            raise ValueError("Last name must be a non-blank string.")
        if not isinstance(email_address, str):
            raise ValueError("Email address must be a string.")
        

        self.__client_number = client_number
        self.__first_name = first_name.strip()
        self.__last_name = last_name.strip()
        self.__email_address = email_address

    @property
    def client_number(self) -> int:
        return self.__client_number

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def email_address(self) -> str:
        return self.__email_address

    def __str__(self) -> str:
        return f"{self.__last_name}, {self.__first_name} [{self.__client_number}] - {self.__email_address}\n"
    
    def update(self, message: str) -> None:
        """
        Handle notifications from a BankAccount (Subject).

        Prints a short alert message for the client.
        """
        print(f"Alert for {self.__first_name} {self.__last_name}: {message}")
    

