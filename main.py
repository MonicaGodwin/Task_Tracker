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
        if description == "":
            print("Task description cannot be empty\n")
            continue
        status = "Todo"
        created_at = time.ctime()
        updated_at = time.ctime()
        insert = cursor.execute(
            "INSERT INTO tasks(description, status, created_at, updated_at) VALUES(?,?,?,?)",
            (description, status, created_at, updated_at)
        )
        if insert.rowcount > 0:
            print("Task added successfully")
        else:
            print("could not add task")
        connection.commit()

    elif user_input == "2":
        task_id = int(input("Enter an id to update\n"))
        new_description = input("Enter new description\n").strip()
        if new_description == "":
            print("Task description cannot be empty\n")
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

    elif user_input == "3":
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

    elif user_input == "4":
        task_id = input("Enter id to mark task\n")
        status_option = input(
            f"1. Done\n"
            f"2. In-progress\n"
            f"choose status option(1 or 2)\n"
        )
        status = ""
        if status_option == "1":
            status = "Done"
        elif status_option == "2":
            status = "In-progress"
        status_update = cursor.execute(
            "UPDATE tasks SET status = ? WHERE id = ?",
            (status,task_id)
        )
        if status_update.rowcount > 0:
            print("Status updated successfully")
        else:
            print("Status not updated")
        connection.commit()

    elif user_input == "5":
        cursor.execute(
            "SELECT * FROM tasks"
        )
        results = cursor.fetchall()
        for result in results:
           print(result)

    elif user_input == "6":
        status = "Done"
        cursor.execute(
            "SELECT * FROM tasks WHERE status = ?",
            (status,)
        )
        done = cursor.fetchall()
        for each_status in done:
            print(f"{each_status}")
        



    #     with open("tasks.json", "a") as file:
    #         json.dump(task_dict, file, indent=4)

