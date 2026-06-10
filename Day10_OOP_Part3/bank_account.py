class BankAccount:

    def __init__(self, name, balance):

        self.name = name
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:

            self.__balance += amount

            print(f"Deposited ₹{amount}")

    def withdraw(self, amount):

        if amount <= self.__balance:

            self.__balance -= amount

            print(f"Withdrawn ₹{amount}")

        else:

            print("Insufficient Balance")

    def get_balance(self):

        return self.__balance


account = BankAccount(
    "Shubham",
    10000
)

print("Current Balance:", account.get_balance())

account.deposit(2000)

account.withdraw(1500)

print("Final Balance:", account.get_balance())