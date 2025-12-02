class BankAccount:
    def __init__(self, initial_balance=0):
        # store the money inside the account (hidden)
        self._balance = float(initial_balance)

    def deposit(self, amount):
        # add money to the account
        if amount <= 0:
            return False
        self._balance += float(amount)
        return True

    def withdraw(self, amount):
        # try to take money out; only do it if there is enough
        if amount <= 0:
            return False
        if amount <= self._balance:
            self._balance -= float(amount)
            return True
        return False

    def display_balance(self):
        # show the current money in a friendly way
        print(f"Current Balance: ${self._balance:.2f}")
