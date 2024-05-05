import os
import json

def load_data():
    if not os.path.exists("data.json"):
        return []

    with open("data.json", "r") as file:
        data = json.load(file)
    return data

def save_data(data):
    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)

def show_balance(data):
    incomes = sum(item["amount"] for item in data if item["category"] == "income")
    expenses = sum(item["amount"] for item in data if item["category"] == "expense")
    balance = incomes - expenses

    print(f"Current Balance: {balance}")
    print(f"Incomes: {incomes}")
    print(f"Expenses: {expenses}")

def add_record():
    date = input("Enter date (ГГГГ-ММ-ДД): ")
    category = input("Enter category (income/expense): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    new_record = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }

    data = load_data()
    data.append(new_record)
    save_data(data)
    print("Record added successfully.")

def edit_record():
    search_date = input("Enter the date of the record you want to edit (ГГГГ-ММ-ДД): ")

    data = load_data()
    for record in data:
        if record["date"] == search_date:
            record["category"] = input("Enter new category (income/expense): ")
            record["amount"] = float(input("Enter new amount: "))
            record["description"] = input("Enter new description: ")
            break
    else:
        print("Record not found.")
        return

    save_data(data)
    print("Record edited successfully.")

def search_records():
    search_term = input("Enter search term (category/date/amount): ")
    search_value = input(f"Enter {search_term} to search for: ")

    data = load_data()
    results = [record for record in data if str(record.get(search_term)) == search_value]

    if results:
        for result in results:
            print(result)
    else:
        print("No records found.")

def main():
    while True:
        print("\n1. Show Balance\n2. Add Record\n3. Edit Record\n4. Search Records\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            data = load_data()
            show_balance(data)
        elif choice == "2":
            add_record()
        elif choice == "3":
            edit_record()
        elif choice == "4":
            search_records()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
