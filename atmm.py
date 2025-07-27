
accounts = {
    "123456": {"pin": "1234", "name": "John Doe", "balance": 1500.0},
    "789012": {"pin": "5678", "name": "Jane Smith", "balance": 2000.0},
    "345678": {"pin": "9999", "name": "Bob Johnson", "balance": 500.0}
}

daily_withdrawals = {}

def login(accounts):
    attempts = 0
    while attempts < 3:
        acc_num = input("Enter your account number: ")
        pin = input("Enter your PIN: ")
        if acc_num in accounts and pin == accounts[acc_num]["pin"]:
            print(f"\nWelcome, {accounts[acc_num]['name']}!")
            return acc_num
        else:
            print("Invalid account number or PIN.")
        attempts += 1
        print(f"Attempt {attempts} of 3.\n")
    print("Login failed after 3 attempts.")
    return None

def display_header(accounts, account_number):
    name = accounts[account_number]["name"]
    balance = accounts[account_number]["balance"]
    print("\n== ATM MACHINE ==========")
    print(f"Account: {account_number}")
    print(f"Name: {name}")
    print(f"Balance: ${balance:,.2f}")
    print("===")

def display_menu():
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("==")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Change PIN")
    print("6. Exit")

    while True:
        choice = input("\nEnter your choice: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 6:
                return choice
        print("Invalid choice. Please select a number from 1 to 6.")

def check_balance(accounts, account_number):
    name = accounts[account_number]['name']
    balance = accounts[account_number]['balance']
    print(f"\nAccount Holder: {name}")
    print(f"Current Balance: ${balance:,.2f}")

def deposit(accounts, account_number):
    try:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0 or amount < 10 or amount > 5000:
            print("Amount must be between $10 and $5000.")
            return False
        accounts[account_number]['balance'] += amount
        print(f"\nDeposit successful! New balance: ${accounts[account_number]['balance']:,.2f}")
        return True
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return False

def withdraw(accounts, account_number):
    try:
        amount = float(input("Enter amount to withdraw: $"))
        if amount <= 0 or amount < 20 or amount > 500 or amount % 20 != 0:
            print("Amount must be a positive multiple of $20 between $20 and $500.")
            return False
        if amount > accounts[account_number]['balance']:
            print("Insufficient funds.")
            return False
        if account_number not in daily_withdrawals:
            daily_withdrawals[account_number] = 0
        if daily_withdrawals[account_number] + amount > 1000:
            print("Daily withdrawal limit of $1000 exceeded.")
            return False
        accounts[account_number]['balance'] -= amount
        daily_withdrawals[account_number] += amount
        print(f"\nWithdrawal successful! New balance: ${accounts[account_number]['balance']:,.2f}")
        return True
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return False

def transfer(accounts, account_number):
    recipient = input("Enter recipient account number: ")
    if recipient not in accounts or recipient == account_number:
        print("Invalid recipient account.")
        return False
    try:
        amount = float(input("Enter amount to transfer: $"))
        if amount <= 0 or amount < 10 or amount > 2000:
            print("Amount must be between $10 and $2000.")
            return False
        if amount > accounts[account_number]["balance"]:
            print("Insufficient funds.")
            return False
        accounts[account_number]["balance"] -= amount
        accounts[recipient]["balance"] += amount
        print(f"\nTransfer successful!")
        print(f"Sender ({accounts[account_number]['name']}): New Balance = ${accounts[account_number]['balance']:,.2f}")
        print(f"Recipient ({accounts[recipient]['name']}): New Balance = ${accounts[recipient]['balance']:,.2f}")
        return True
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return False

def change_pin(accounts, account_number):
    current_pin = input("Enter your current PIN: ")
    if current_pin != accounts[account_number]["pin"]:
        print("Current PIN is incorrect.")
        return False
    new_pin = input("Enter new 4-digit PIN: ")
    confirm_pin = input("Re-enter new PIN to confirm: ")
    if len(new_pin) != 4 or not new_pin.isdigit():
        print("PIN must be exactly 4 digits.")
        return False
    if new_pin != confirm_pin:
        print("PIN confirmation does not match.")
        return False
    if new_pin == current_pin:
        print("New PIN must be different from current PIN.")
        return False
    accounts[account_number]["pin"] = new_pin
    print("PIN changed successfully.")
    return True

def main():
    print(" Welcome to the ATM Simulator")
    account_number = login(accounts)
    if account_number is None:
        print("Exiting program due to failed login.")
        return
    display_header(accounts, account_number)

    while True:
        choice = display_menu()
        if choice == 1:
            check_balance(accounts, account_number)
        elif choice == 2:
            deposit(accounts, account_number)
        elif choice == 3:
            withdraw(accounts, account_number)
        elif choice == 4:
            transfer(accounts, account_number)
        elif choice == 5:
            change_pin(accounts, account_number)
        elif choice == 6:
            print("Logging out... Goodbye!")
            break

if __name__ == "__main__":
    main()
