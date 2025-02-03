import os

balance = 0

def checkBalance():
    os.system("clear")
    print(f"Current balance: ${balance}")
    input("Press Enter to continue")

def transferFunds():
    os.system("clear")
    global balance
    

def payBills():
    pass

def requestStatements():
    pass

def updatePersonalInfo():
    pass

def main():
    os.system("clear")
    is_running = True
    while is_running:
        global balance
        while is_running:
            print("Welcome to the bank")
            print("1. Check Balance")
            print("2. Transfer Funds")
            print("3. Pay Bills")
            print("4. Request Statements")
            print("5. Update Personal Info")
            print("6. Exit")
            option = input("Enter your option: ")
            if option == "1":
                checkBalance()
            elif option == "2":
                transferFunds()
            elif option == "3":
                payBills()
            elif option == "4":
                requestStatements()
            elif option == "5":
                updatePersonalInfo()
            elif option == "6":
                is_running = False
            else:
                print("Invalid option, pick again")
                input("Press Enter to continue")
                print()

if __name__ == "__main__":
    main()