class ATM:
    def __init__(self):
        self.balance = 500
        self.transaction_history = []

    def authenticate(self, pin):
        # Simple pin validation (for demo purposes)
        return pin == "2004"

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            print(f"${amount} deposited. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn: ${amount}")
            print(f"${amount} withdrawn. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def display_balance(self):
        print(f"Current balance: ${self.balance}")

    def show_transaction_history(self):
        print("Transaction History:")
        if self.transaction_history:
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")

# Example of how to use the ATM class
def main():
    atm = ATM()
    pin = input("Enter your PIN: ")
    if atm.authenticate(pin):
        while True:
            print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Transaction History\n5. Exit")
            choice = input("Select an option: ")
            if choice == '1':
                amount = float(input("Enter deposit amount: "))
                atm.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter withdrawal amount: "))
                atm.withdraw(amount)
            elif choice == '3':
                atm.display_balance()
            elif choice == '4':
                atm.show_transaction_history()
            elif choice == '5':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Invalid PIN.")

if __name__ == "__main__":
    main()
