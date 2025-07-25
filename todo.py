import sqlite3
from tabulate import tabulate 
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    status TEXT DEFAULT 'Pending'
)
''')
conn.commit()

def add_task(task):
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    print(f" Task '{task}' added successfully!")

def view_tasks():
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    
    if not tasks:
        print("\n No tasks found!")
    else:
        print("\n To-Do List:")
        print(tabulate(tasks, headers=["ID", "Task", "Status"], tablefmt="grid"))


def update_task(task_id, new_status):
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
    conn.commit()
    print(f"Task ID {task_id} updated to '{new_status}'.")


def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    print(f"Task ID {task_id} deleted.")

while True:
    print("\n🔹 Options: 1. Add Task  2. View Tasks  3. Update Task  4. Delete Task  5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        task_id = int(input("Enter task ID to update: "))
        new_status = input("Enter new status (Pending/Completed): ")
        update_task(task_id, new_status)
    elif choice == "4":
        task_id = int(input("Enter task ID to delete: "))
        delete_task(task_id)
    elif choice == "5":
        print("Exiting... Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

conn.close()
