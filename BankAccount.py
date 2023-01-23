##The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. The account should also have an interest rate in decimal format. For example, a 1% interest rate would be saved as 0.01. The interest rate should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)

class BankAccount:
    def __init__(self, initial_balance=0, interest_rate=0):
        self.balance = initial_balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount
    
    def display_account_info(self):
        print(f"Balance: ${self.balance: f}")
        print(f"Interest rate: {self.interest_rate *100}%")

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

##Create 2 Accounts
account1 = BankAccount()
account2 = BankAccount()

##Chaining Representation
account1.deposit().deposit().deposit().withdraw(50).add_interest().display_account_info()

##Chaining Representation 2]
account2.deposit().deposit().withdraw().withdraw().withdraw().withdraw().add_interest().display_account_info()



