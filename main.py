import time
import sqlite3

connection = sqlite3.connect("tasks.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY,
        description TEXT,
        status TEXT,
        created_at TEXT, 
        updated_at TEXT            
        )
""")

while True:
    user_input = input(
        f"===== SELECT TASK OPTION =====\n\n"
        f"1. Add a new task\n"
        f"2. Update a task\n"
        f"3. Delete tasks\n"
        f"4. Mark as in-progress or done\n"
        f"5. List all tasks\n"
        f"6. List done\n"
        f"7. List not done\n"
        f"8. List in-progress\n"
        f"9. Exit\n"
        f"\n choose an option(1, 2, 3, 4, 5, 6, 7)\n"
    )

    if user_input == "1":
        description = input("Enter task description:\n").strip()
        if not description.isalpha():
            print("invalid input\n")
            continue
        status = "In-progress"
        created_at = time.ctime()
        updated_at = time.ctime()
        insert = cursor.execute(
            "INSERT INTO tasks(description, status, created_at) VALUES(?,?,?,?)",
            (description, status, created_at, updated_at)
        )
        if insert.rowcount > 0:
            print("task added successfully")
        else:
            print("could not add task")
        connection.commit()

    if user_input == "2":
        task_id = int(input("Enter an id to update\n"))
        new_description = input("Enter new description\n")
        status = "In-progress"
        if not new_description.isalpha():
            print("Invalid input\n")
            continue
        cursor.execute(
            "UPDATE tasks SET description = ? WHERE id = ?",
            (new_description, task_id,)
        )
        if cursor.rowcount > 0:
            print("Task updated")
        else:
            print("Task not found")
        connection.commit()

    if user_input == "3":
        delete_id = int(input("Enter an id to delete\n"))
        cursor.execute(
            "DELETE FROM tasks WHERE id = ?",
            (delete_id,)
        )
        if cursor.rowcount > 0:
            print("Task deleted")
        else:
            print("Task not found")
        connection.commit()




    # if user_input == "1":
    #     description = input("Enter task description:\n")
    #     task_dict = {
    #         "id" : "Id",
    #         "description": description,
    #         "status" : ["todo", "in-progress", "done"],
    #         "createdAt" : "CreatedAt",
    #         "updatedAt" : "UpdatedAt",
    #     }
    #     with open("tasks.json", "a") as file:
    #         json.dump(task_dict, file, indent=4)

