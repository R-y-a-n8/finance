from models import add_user, add_transaction, view_transactions, delete_transaction, user_exists, category_exists

def main():
    while True:
        print("Business Finance Tracker")
        print("1. Add User")
        print("2. Add Transaction")
        print("3. View Transactions")
        print("4. Delete Transaction")
        print("5. Exit")

        option = input("Select an option: ")

        if option == '1':
            name = input("Enter user name: ")
            user_id = add_user(name)
            print(f"User '{name}' added successfully.")

        elif option == '2':
            try:
                user_id = int(input("Enter user ID: "))
                if not user_exists(user_id):
                    print("User ID does not exist. Please add the user first.")
                    continue
                
                amount = float(input("Enter amount: "))
                date = input("Enter date (YYYY-MM-DD): ")
                transaction_type = input("Enter transaction type (income/expense): ")
                category_id = int(input("Enter category ID: "))
                if not category_exists(category_id):
                    print("Category ID does not exist. Please add the category first.")
                    continue

                add_transaction(user_id, amount, date, transaction_type, category_id)
                print("Transaction added successfully.")
            except ValueError:
                print("Invalid input. Please enter numbers for user ID and category ID.")

        elif option == '3':
            transactions = view_transactions()
            if transactions:
                print("Transactions:")
                for transaction in transactions:
                    print(transaction)
            else:
                print("No transactions found.")

        elif option == '4':
            transaction_id = int(input("Enter transaction ID to delete: "))
            delete_transaction(transaction_id)
            print("Transaction deleted successfully.")

        elif option == '5':
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
