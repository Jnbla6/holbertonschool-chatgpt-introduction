#!/usr/bin/python3
class Checkbook:
    """
    Class Description:
    Represents a simple checkbook to track a bank account balance.
    Allows for deposits, withdrawals, and balance inquiries.
    """
    def __init__(self):
        """
        Function description:
        Initializes a new Checkbook instance with a starting balance of 0.0.

        Parameters:
        None

        Returns:
        None
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function description:
        Adds a specified amount to the checkbook balance.

        Parameters:
        amount: The float value to be deposited.

        Returns:
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function description:
        Deducts a specified amount from the checkbook balance if funds are sufficient.

        Parameters:
        amount: The float value to be withdrawn.

        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function description:
        Prints the current balance of the checkbook.

        Parameters:
        None

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Function description:
    The main execution loop for the checkbook program. Handles user input
    and calls the appropriate Checkbook methods.

    Parameters:
    None

    Returns:
    None
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount = float(input("Enter the amount to deposit: $"))
                cb.deposit(amount)
            except ValueError:
                print("Invalid input: Please enter a numeric value.")
        elif action.lower() == 'withdraw':
            try:
                amount = float(input("Enter the amount to withdraw: $"))
                cb.withdraw(amount)
            except ValueError:
                print("Invalid input: Please enter a numeric value.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()