def review_account_transactions(transactions):
    print("Reviewing account transactions...")
    if transactions:
        for transaction in transactions:
            print(transaction)
    else:
        print("No transactions available.")


def flag_suspicious_activity(transactions):
    print("Flagging suspicious activity...")
    suspicious_activities = [t for t in transactions if t['amount'] > 10000]
    if suspicious_activities:
        print("Suspicious activities found:")
        for activity in suspicious_activities:
            print(activity)
    else:
        print("No suspicious activities detected.")

def generate_audit_reports(transactions):
    print("Generating audit reports...")
    if transactions:
        print("Audit Report:")
        print("====================")
        for transaction in transactions:
            print(f"Date: {transaction['date']}, Amount: {transaction['amount']}, Description: {transaction['description']}")
        print("====================")
    else:
        print("No transactions available to generate report.")

def verify_compliance_with_policies():
    print("Verifying compliance with policies...")
    compliance_status = "All policies are complied with."
    print(compliance_status)


def provide_improvement_recommendations():
    print("Providing improvement recommendations...")
    recommendations = "Recommendation: Review monthly expenses to identify potential savings."
    print(recommendations)

def main():
    transactions = [] #this is for list to store transactions

    while True:
        print("\nAuditor Menu:")
        print("1: Add a transaction")
        print("2: Review account transactions")
        print("3: Flag suspicious activity")
        print("4: Generate audit reports")
        print("5: Verify compliance with policies")
        print("6: Provide improvement recommendations")
        print("7: Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a transaction
            date = input("Enter transaction date (YYYY-MM-DD): ")
            amount = float(input("Enter transaction amount: "))
            description = input("Enter transaction description: ")
            transactions.append({"date": date, "amount": amount, "description": description})
            print("Transaction added successfully!")

        elif choice == "2":
            review_account_transactions(transactions)

        elif choice == "3":
            flag_suspicious_activity(transactions)

        elif choice == "4":
            generate_audit_reports(transactions)

        elif choice == "5":
            verify_compliance_with_policies()

        elif choice == "6":
            provide_improvement_recommendations()

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Sorry, this number is not available")

main()