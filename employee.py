import sqlite3
from tabulate import tabulate

# Connect to SQLite database (or create it)
conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

# Create employee table if not exists
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

# Function to add an employee
def add_employee(name, age, department, salary):
    cursor.execute("INSERT INTO employees (name, age, department, salary) VALUES (?, ?, ?, ?)", (name, age, department, salary))
    conn.commit()
    print(f"✅ Employee '{name}' added successfully!")

# Function to view all employees
def view_employees():
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    
    if not employees:
        print("\n📌 No employees found!")
    else:
        print("\n📋 Employee List:")
        print(tabulate(employees, headers=["ID", "Name", "Age", "Department", "Salary"], tablefmt="grid"))

# Function to update employee salary
def update_salary(emp_id, new_salary):
    cursor.execute("UPDATE employees SET salary = ? WHERE id = ?", (new_salary, emp_id))
    conn.commit()
    print(f"✅
