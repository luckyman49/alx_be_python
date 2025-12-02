import sys
from bank_account import BankAccount

def main():
    # start an account with $100 so you can test easily
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')
    amount = float(params[0]) if params else None

    if command == "deposit" and amount is not None:
        if account.deposit(amount):
            print(f"Deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds or invalid amount.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
