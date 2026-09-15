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
        f"\n choose an option(1 - 9)\n"
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
        if not task_id.is_integer():
            print("Id must be a number")
            continue 
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
        delete_option = input(
            f"1. Delete by ID\n"
            f"2. Delete All\n"
            "Choose an option to delete\n"
        )
        if delete_option == "1":
            delete_id = int(input("Enter an id to delete\n"))
            cursor.execute(
            "DELETE FROM tasks WHERE id = ?",
            (delete_id,)
        )  
            if cursor.rowcount > 0:
                print("Task deleted")
            else:
                print("Task not found")

        elif delete_option == "2":
            cursor.execute(
                "DELETE FROM tasks"
            )     
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
        if not results:
            print("Task Not Available")
        else:
            for result in results:
                print(result)

    elif user_input == "6":
        status = "Done"
        cursor.execute(
            "SELECT * FROM tasks WHERE status = ?",
            (status,)
        )
        done = cursor.fetchall()
        if not done:
            print("No task available for this status")
            continue
        else:
            for each_status in done:
                print(f"{each_status}")
        
    elif user_input == "7":
        status = "Todo"
        cursor.execute(
            "SELECT * FROM tasks WHERE status = ?",
            (status,)
        )
        todo = cursor.fetchall()
        if not todo:
            print("No task available for this status")
            continue
        else:
            for each_status in todo:
                print(f"{each_status}")
    
    elif user_input == "8":
        status = "In-progress"
        cursor.execute(
            "SELECT * FROM tasks WHERE status = ?",
            (status,)
        )
        in_progress = cursor.fetchall()
        if not in_progress:
            print("No task available for this status")
            continue
        else:
            for each_status in in_progress:
                print(f"{each_status}")
                
    elif user_input == "9":
        print("Goodbye")
        break
    else:
        print("Please select an option(1 - 9)")

