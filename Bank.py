import random
import string


class Bank:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.balance = balance
        self.account_number = account_number

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    
    @staticmethod
    def create_accountID():
        account_ID = []

        for i in range(10):
            next_character = random.choice(string.ascii_lowercase + string.digits)
            account_ID.append(next_character)
    
        result = "".join(account_ID)

        return result
        

class BankAccount(Bank):
    def _init_(self,name,balance=0):
        super().__init__(name,balance)
    
    def __str__(self):
        return f"Name: {self.name}, Account ID: {self.account_number}, Balance: ${self.balance:.2f}"

# helper functions


# Generate the random Account ID for User

class NewUser():
    def __init__(self, new_name, new_accountID, new_balance):
        self.new_accountID = new_accountID
        self.new_name = new_name
        self.new_balance = new_balance
        

    def create_account():
        first_name = input("Please enter your first name: ")
        last_name = input("Please enter your last name: ")
        full_name = first_name + " " + last_name
        initial_balance = float(input("Enter your initial deposit amount: "))
        account_number = Bank.create_accountID()
        account = BankAccount(name=full_name,account_number=account_number,balance=initial_balance,)
        print(f"Thank you {full_name}, here is your Account ID: {account.account_number}")
        print(f"Your Bank of America balance: ${initial_balance:.2f}")
       
        p1 = NewUser(full_name, account_number, initial_balance)
        return p1, account
    


        

