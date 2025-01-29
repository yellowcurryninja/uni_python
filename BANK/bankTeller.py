import os


balance = 0
AccountCreated = False
Account = []


def openNewAccount():
    os.system("clear")
    username = input("Enter your username: ")
    usernameTrue = True
    while usernameTrue:
        if not username:
            print("Username cannot be empty")
            username = input("Enter your username: ")
        else:
            usernameTrue = False
            
            
    passwordTrue = True
    while passwordTrue:
        password = input("Enter your password: ")
        password2 = input("Re-enter your password: ")
        if password != password2:
            print("Passwords do not match, try again")
        else:
            passwordTrue = False        
        
    accountTrue = True
    while accountTrue:
        accountType = input("Enter your account type(Saving or Checking): ")
        if accountType.lower() not in ["saving", "checking"]:
            print("Invalid account type, try again")
        else:
            accountTrue = False
   
    Account.append((username, password, accountType))

    global AccountCreated
    AccountCreated = True
    print("Account created successfully")
    input("Press Enter to continue")
        
        
        
def processDeposit():
    os.system("clear")
    if AccountCreated == False:
        print("You need to create an account first")
        input("Press Enter to continue")
        return
    global balance
    while True:
        try:
            amount = float(input("Enter the amount to deposit: "))
            if amount <= 0:
                print("Invalid amount")
                return
            balance += amount
            print("Amount deposited successfully")
            print(f"Current balance: ${balance}")
            break
        except ValueError:
            print("Invalid amount")
            return



def processWithdrawal():
    os.system("clear")
    global balance
    while True:
        try:
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= 0:
                print("Invalid amount")
                input("Press Enter to continue")
                return
            if amount > balance:
                print("Insufficient funds")
                input("Press Enter to continue")
                return
            balance -= amount
            print("Amount withdrawn successfully")
            print(f"Current balance: ${balance}")
            input("Press Enter to continue")
            break
        except ValueError:
            print("Invalid amount")
            input("Press Enter to continue")

def issueDebitCard():
    pass

def loanApplication():
    pass

def closeAccount():
    os.system("clear")
    if not AccountCreated:
        print("You need to create an account first")
        input("Press Enter to continue")
        return

    global Account

    for i in range(len(Account)):
        username, password, accountType = Account[i]
        print(f"{i + 1}. {username} ({accountType})")

    choice = input("Select an account to close by number: ")
    try:
        choice_index = int(choice) - 1
        if 0 <= choice_index < len(Account):
            closed_account = Account.pop(choice_index)
            print(f"Account '{closed_account[0]}' closed.")
            input("Press Enter to continue")
        else:
            print("Invalid choice.")
            input("Press Enter to continue")
    except ValueError:
        print("Invalid choice.")
        input("Press Enter to continue")
    

def main():
    os.system("clear")
    is_running = True
    while is_running:
        global balance
        while is_running:
            print("Welcome to the bank")
            print("1. Open a new account")
            print("2. Deposit")
            print("3. Withdrawal")
            print("4. Issue Debit Card")
            print("5. Loan Application")
            print("6. Close Account")
            print("7. Exit")
            print("8. Check Balance")
            option = input("Enter your option: ")
            if option == "1":
                openNewAccount()
            elif option == "2":
                processDeposit()
            elif option == "3":
                processWithdrawal()
            elif option == "4":
                issueDebitCard()
            elif option == "5":
                loanApplication()
            elif option == "6":
                closeAccount()
            elif option == "7":
                is_running = False
            elif option == "8":
                os.system("clear")
                print(f"Current balance: ${balance}")
                input("Press Enter to continue")
            else:
                print("Invalid option, pick again")
                input("Press Enter to continue")


if __name__ == "__main__":
    main()