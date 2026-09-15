import json
import sqlite3
connection = sqlite3.connect("tasks.db")
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        id INTEGER PRIMARY KEY,
        description TEXT,
        status TEXT,
        createdAt TEXT, 
        updatedAt TEXT            
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
        f"6. List by status\n"
        f"7. Exit\n"
        f"\n choose an option(1, 2, 3, 4, 5, 6, 7)\n"
    )

    if user_input == "1":
        cursor.


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

