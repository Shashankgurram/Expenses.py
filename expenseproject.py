import csv
import os

def display_menu():
    print("\nPersonal Expense Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Delete Expense")
    print("4. Exit")

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Transport, Shopping, etc.): ")
    amount = input("Enter amount: ")
    
    with open("expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    
    print("Expense added successfully!")

def view_expenses():
    if not os.path.exists("expenses.csv"):
        print("No expenses recorded yet.")
        return
    
    with open("expenses.csv", mode="r") as file:
        reader = csv.reader(file)
        print("\nDate		Category	Amount")
        print("-" * 30)
        for row in reader:
            print("\t".join(row))

def delete_expense():
    if not os.path.exists("expenses.csv"):
        print("No expenses to delete.")
        return
    
    expenses = []
    with open("expenses.csv", mode="r") as file:
        reader = csv.reader(file)
        expenses = list(reader)
    
    for i, expense in enumerate(expenses):
        print(f"{i + 1}. {expense}")
    
    try:
        index = int(input("Enter the number of the expense to delete: ")) - 1
        if 0 <= index < len(expenses):
            expenses.pop(index)
            with open("expenses.csv", mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(expenses)
            print("Expense deleted successfully!")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            print("Exiting... Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
