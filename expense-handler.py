import os

print("Expense Handler")

def main():
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. View total spent")
    print("4. Exit")
    add_expense = input("Choose an option (1, 2, 3, 4): ").strip().lower()
    if add_expense == '1':
        add()
    elif add_expense == '2':
        view()
    elif add_expense == '3':
        total()
    elif add_expense == '4':
        exit()
    else:
        print("Invalid option. Please try again.")
        main()
def add():
    user = input("Enter your name: ").strip().lower()
    amount = input("Enter expense amount: ").strip()
    description = input("Enter expense description: ").strip()
    with open(f"{user}_expenses.txt", "a") as file:
        file.write(f"{user}\n{amount},{description}\n")
    print("Expense added successfully.")
    main()
def view():
    user = input("Enter your name: ").strip().lower()
    try:
        with open(f"{user}_expenses.txt", "r") as file:
            lines = file.readlines()[1:]  # Skip the first line (username)
            if not lines:
                print("No expenses found.")
            else:
                print("Your Expenses:")
                for line in lines:
                    amount, description = line.strip().split(",", 1)
                    print(f"Amount: {amount}, Description: {description}")
    except FileNotFoundError:
        print("No expenses found for this user.")
    main()
def total():
    user = input("Enter your name: ").strip().lower()
    total_amount = 0.0
    try:
        with open(f"{user}_expenses.txt", "r") as file:
            lines = file.readlines()[1:]  # Skip the first line (username)
            for line in lines:
                amount, _ = line.strip().split(",", 1)
                total_amount += float(amount)
        print(f"Total amount spent: {total_amount}")
    except FileNotFoundError:
        print("No expenses found for this user.")
    main()


if __name__ == "__main__":
    main()