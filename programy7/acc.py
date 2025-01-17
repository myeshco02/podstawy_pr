import random


class BankAcc:
    def __init__(self, accNumber):
        self.accNumber = accNumber
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: PLN {amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrawn: PLN {amount:.2f}")
            else:
                print("Insufficient funds on the account")
        else:
            print("Withdrawal amount must be positive.")

    def displayInfo(self):
        print(f"Bank Account No: {self.accNumber}")
        print(f"Balance: PLN {self.balance:,.2f}")