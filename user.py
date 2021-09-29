class User:
    bank_name = "Bank of Kramer"

    # Passing in 2 params : name and email_address
    def __init__(self, name, email_address):
        # 3 attributes that provide a name, email-address, and bank account balance.
        self.name = name
        self.email = email_address
        self.account_balance = 0

    # function that prints a message with a greeting of a specific instance.
    def greeting(self):
        print(f"Hello, my name is {self.name}")

    # function that passes in 1 argument from the instance that adds funds to the bank account.
    def make_deposit(self, amount):
        self.account_balance += amount

    # function that passes in 1 argument from the instance that subtracts funds to the bank account.
    def make_withdrawl(self, amount):
        self.account_balance -= amount

    # function displays user's current account balance.
    def display_user_balance(self):
        print(f"User: {self.name} , Balance: {self.account_balance}")

# Instances with values passed in. Total of 3.
kramer = User("Kramer", "Kramer@gmail.com")
jessie = User("Jessie", "Jessie@gmail.com")
jason = User("Jason", "Jason@outlook.com")

kramer.bank_name = "Credit Union of Kramer"

print(kramer.bank_name)
print(jessie.bank_name)

kramer.make_deposit(20)
kramer.make_deposit(20)
kramer.make_deposit(20)
kramer.make_withdrawl(5)

jessie.make_deposit(40)
jessie.make_deposit(40)
jessie.make_withdrawl(20)
jessie.make_withdrawl(20)

jason.make_deposit(400)
jason.make_withdrawl(50)
jason.make_withdrawl(20)
jason.make_withdrawl(10)

kramer.display_user_balance()
jessie.display_user_balance()
jason.display_user_balance()