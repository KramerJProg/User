class User:
    bank_name = "Bank of Kramer"

    # Passing in 1 params : name 
    def __init__(self, name):
        # 2 attributes that provide a name and bank account balance.
        self.name = name
        self.account_balance = 0

    # function that prints a message with a greeting of a specific instance.
    def greeting(self):
        print(f"Hello, my name is {self.name}")

    # function that passes in 1 argument from the instance that adds funds to the bank account.
    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    # function that passes in 1 argument from the instance that subtracts funds to the bank account.
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    # function displays user's current account balance.
    def display_user_balance(self):
        print(f"User: {self.name} , Balance: {self.account_balance}")

    # function that transfers funds from one user's account to another user's account.
    def transfer_money(self, amount, user):
        self.account_balance -= amount
        user.account_balance += amount
        self.display_user_balance()
        user.display_user_balance()

# Instances with values passed in. Total of 3.
kramer = User("Kramer")
jessie = User("Jessie")
jason = User("Jason")

kramer.bank_name = "Credit Union of Kramer"

print(kramer.bank_name)
print(jessie.bank_name)

kramer.make_deposit(20).make_deposit(20).make_deposit(20).make_withdrawl(5).transfer_money(5, jason)

jessie.make_deposit(40).make_deposit(40).make_withdrawl(20).make_withdrawl(20)

jason.make_deposit(400).make_withdrawl(50).make_withdrawl(20).make_withdrawl(10)

jessie.display_user_balance()
jason.display_user_balance()