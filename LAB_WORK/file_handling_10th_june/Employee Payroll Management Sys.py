# Employee Management System with File Handling

FILENAME = "employees.txt"

# ---------------- Helper Functions ----------------
def load_employees():
    employees = {}
    try:
        with open(FILENAME, "r") as f:
            for line in f:
                eid, name, salary = line.strip().split(",")
                employees[eid] = {"name": name, "salary": int(salary)}
    except FileNotFoundError:
        pass
    return employees

def save_employees(employees):
    with open(FILENAME, "w") as f:
        for eid, info in employees.items():
            f.write(f"{eid},{info['name']},{info['salary']}\n")

# ---------------- Operations ----------------
def display_all(employees):
    for eid, info in employees.items():
        print(eid, ":", info)

def search_employee(employees, eid):
    return employees.get(eid, "Not Found")

def average_salary(employees):
    total = sum(info["salary"] for info in employees.values())
    return total / len(employees)

def highest_lowest(employees):
    high = max(employees.items(), key=lambda x: x[1]["salary"])
    low = min(employees.items(), key=lambda x: x[1]["salary"])
    return high, low

def above_50000(employees):
    return {eid: info for eid, info in employees.items() if info["salary"] > 50000}

def add_employee(employees, eid, name, salary):
    employees[eid] = {"name": name, "salary": salary}
    save_employees(employees)

def salary_categories(employees):
    categories = {"High": [], "Medium": [], "Low": []}
    for eid, info in employees.items():
        sal = info["salary"]
        if sal >= 60000:
            categories["High"].append((eid, info))
        elif sal >= 40000:
            categories["Medium"].append((eid, info))
        else:
            categories["Low"].append((eid, info))
    return categories

# ---------------- Menu Driven ----------------
def main():
    employees = load_employees()

    while True:
        print("\n--- Employee Menu ---")
        print("1. Display all records")
        print("2. Search employee by ID")
        print("3. Calculate average salary")
        print("4. Find highest & lowest paid")
        print("5. Employees earning above 50,000")
        print("6. Add new employee")
        print("7. Salary categories")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            display_all(employees)

        elif choice == "2":
            eid = input("Enter Employee ID: ")
            print(search_employee(employees, eid))

        elif choice == "3":
            print("Average Salary =", average_salary(employees))

        elif choice == "4":
            high, low = highest_lowest(employees)
            print("Highest Paid:", high)
            print("Lowest Paid:", low)

        elif choice == "5":
            print("Employees earning above 50,000:", above_50000(employees))

        elif choice == "6":
            eid = input("Enter new Employee ID: ")
            name = input("Enter name: ")
            salary = int(input("Enter salary: "))
            add_employee(employees, eid, name, salary)
            print("Employee added successfully!")

        elif choice == "7":
            cats = salary_categories(employees)
            print("High:", cats["High"])
            print("Medium:", cats["Medium"])
            print("Low:", cats["Low"])

        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
