import os
import time
from Q2a import Account

# class of DevAccount inherit from Account class


class DevAccount(Account):
    # DevAccount class constructor
    def __init__(self, acc_no, name, balance):
        self._id = acc_no
        self._name = name
        self._balance = balance
    # allows user to call methods only without access to original data attributes directly by supplying _underscore in the attrs

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount
    # represents the class objects as a string

    def __str__(self):
        return f"{self._name}'s account. Balance: ${self._balance}"


# instantiation two objects 1. DevAccount and Shane account
a1 = DevAccount(1001, "Dev", 0)
a2 = DevAccount(1002, "Shane", 0)

# demo to run - python3 Q2b.py | if-else switch concept


def switch():
    # Menu for available banking operations
    os.system("clear")
    print("Welcome to online banking\n\n" +
          a1.__str__() + "\n" + a2.__str__() + "\n")
    menu = int(
        input("Please select operation\n 1. Deposit\n 2. Withdrawal\n 3. Transfer \n\nSelection: "))
    os.system("clear")
    # Calling Deposit method from DevAccount
    if menu == 1:
        os.system("clear")
        print("Please enter amount to deposit: ")
        depo = int(input(""))
        # perform deposit into DevAccount
        a1.deposit(depo)
        os.system("clear")
        print("\n\nYour new balance is: \n$", str(a1.get_balance()) + "\n\n")
        time.sleep(2)
        switch()
    # Calling withdraw method from DevAccount
    elif menu == 2:
        print("Please enter amount to withdraw: ")
        wd = int(input(""))
        # validation for available balance !< amount to be withdrawn
        if wd > a1._balance:
            os.system("clear")
            print("\n\nYou have an insufficient balance to withdraw. Please try again.\n")
            time.sleep(1.5)
            switch()
        else:
            # perform withdraw method and show new balance
            a1.withdraw(wd)
            os.system("clear")
            print("\n\nYour new balance is: \n$",
                  str(a1.get_balance()) + "\n\n")
            time.sleep(2)
            switch()
    # Calling transfer method from DevAccount --> Shane Account
    elif menu == 3:
        print("Please enter amount to transfer: ")
        wt = int(input(""))
        # validation for available balance !< amount to be withdrawn
        if wt > a1._balance:
            os.system("clear")
            print("\n\nYou have an insufficient balance to transfer. Please try again.\n")
            time.sleep(1.5)
            switch()
        else:
            # perform deduction on DevAccount and increment in Shane Account and display both balances
            a1.withdraw(wt)
            a2.deposit(wt)
            os.system("clear")
            print("\n\nYour new balance is: \n$",
                  str(a1.get_balance()) + "\n")
            print("and", a2._name, "new balance is $", str(a2.get_balance()))
            time.sleep(3)
            switch()


# call wrapper from parent class
print("\n" + a1.__str__() + "\n" + a2.__str__() + "\n")
# run switch
switch()
