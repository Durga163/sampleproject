import sqlite3
from tabulate import tabulate

#
conn = sqlite3.connect("employees.db")
cursor = conn.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    department TEXT NOT NULL,
    salary REAL NOT NULL
)
''')
conn.commit()

def add_employee(name, age, department, salary):
    cursor.execute("INSERT INTO employees (name, age, department, salary) VALUES (?, ?, ?, ?)", (name, age, department, salary))
    conn.commit()
    print(f" Employee '{name}' added successfully!")


def view_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    
    if not employees:
        print("\n No employees found!")
    else:
        print("\n Employee List:")
        print(tabulate(employees, headers=["ID", "Name", "Age", "Department", "Salary"], tablefmt="grid"))


def update_salary(emp_id, new_salary):
    cursor.execute("UPDATE employees SET salary = ? WHERE id = ?", (new_salary, emp_id))
    conn.commit()
    print(f" Salary updated for Employee ID {emp_id}.")


def delete_employee(emp_id):
    cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
    conn.commit()
    print(f" Employee ID {emp_id} deleted.")

def search_employee(name):
    cursor.execute("SELECT * FROM employees WHERE name LIKE ?", ('%' + name + '%',))
    employees = cursor.fetchall()
    
    if not employees:
        print(f"\n No employee found with name '{name}'.")
    else:
        print("\n Employee Search Results:")
        print(tabulate(employees, headers=["ID", "Name", "Age", "Department", "Salary"], tablefmt="grid"))

# Main Menu
while True:
    print("\n Options: 1. Add Employee  2. View Employees  3. Update Salary  4. Delete Employee  5. Search Employee  6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        department = input("Enter department: ")
        salary = float(input("Enter salary: "))
        add_employee(name, age, department, salary)
    
    elif choice == "2":
        view_employees()
    
    elif choice == "3":
        emp_id = int(input("Enter Employee ID to update salary: "))
        new_salary = float(input("Enter new salary: "))
        update_salary(emp_id, new_salary)
    
    elif choice == "4":
        emp_id = int(input("Enter Employee ID to delete: "))
        delete_employee(emp_id)
    
    elif choice == "5":
        name = input("Enter name to search: ")
        search_employee(name)
    
    elif choice == "6":
        print(" Exiting... Goodbye!")
        break
    
    else:
        print(" Invalid choice. Please try again.")
]
conn.close()

