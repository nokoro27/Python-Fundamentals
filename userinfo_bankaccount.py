##RESUBMIT##
##From previous assignment
class BankAccount:
    def __init__(self, initial_balance=0, interest_rate=0):
        self.balance = initial_balance
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5 
    
    def display_account_info(self):
        print(f"Balance: ${self.balance: f}")
        print(f"Interest rate: {self.interest_rate *100}%")

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

##Create a User class with an __init__method
class User:
    def __init__(self, name):
        self.name = name
        self.account = BankAccount()

##Add a make_deposit method
    def make_deposit(self, amount):
        self.account.deposit(amount)

##Add a make_withdrawal method that calls on it's bank account's instance methods
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

##Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to

    def display_user_info(self):
        print(f"Name: {self.name}")
        self.account.display_account_info()


Nenye = User("Nenye")
Nenye.display_user_info()
Nenye.make_deposit(100)
Nenye.display_user_info()
Nenye.make_withdrawal(50)
Nenye.display_user_info()
