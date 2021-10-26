class Account(object):
    def __init__(self, acc_no, name, balance):
        self.id = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        # deposit = balance + amount
        self.balance += amount

    def withdraw(self, amount):
        # withdraw = balance - amount
        self.balance -= amount

    # basically returning the class objects as string.
    def __str__(self):
        return f"{self.name}'s account. Balance: ${self.balance}"
