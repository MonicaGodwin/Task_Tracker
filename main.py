import json
import os
import sys
import time

task = {
    "id" : "Id",
    "description" : "Description",
    "status" : "Status",
    "created_at" : "CreatedAt",
    "updated_at" : "UpdatedAt"
}


if not os.path.exists("tasks.json"):
    tasks = []
    with open("tasks.json", "w") as file:
        json.dump(tasks,file,indent=4)
else:
    with open("tasks.json", "r") as data:
        tasks = json.load(data)
       
if len(sys.argv) < 2:
    print("Usage: python main.py [add | delete | list]")
    sys.exit()
    
command = sys.argv[1].lower()

        
if command == "add":
    if len(sys.argv) < 3:
        print("Error: Please provide a task description.")
        print('Usage: python3 main.py add "Task description"')
        sys.exit()
        
    description = sys.argv[2]
    description = description.strip()
    next_id = len(tasks) + 1 # Calculates the next task id position 
    current_time = time.ctime()
    new_tasks = {
    "id": next_id,
    "description": description,
    "status": "Todo",  # Tasks start as "todo" by default
    "created_at": current_time,
    "updated_at": current_time
    }
    tasks.append(new_tasks)
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
        
    print(f"Task added successfully! (ID: {next_id})")


elif command == "list":
    if len(tasks) == 0:
        print("No task to display.")
    else:
        for task in tasks:
            print(f"{task['id']} - {task['description']} - {task['status']} - {task['created_at']} - {task['updated_at']}")

elif command == "delete":
    if len(sys.argv) < 3:
        print(
            f"Error: please provide a task id to delete\n"
            f'Usage: python3 main.py delete "The task Id to delete"'
        )
        sys.exit()

    task_id = sys.argv[2]
    
    try:
        converted_id = int(task_id)
    except ValueError:
        print("Must be an integer")
        sys.exit()
    found = False
    for task in tasks:
        if task["id"] == converted_id:
            tasks.remove(task)
            found = True
            print("Task deleted")
            break
    if found:
        for number, task in enumerate(tasks, start=1):
            task["id"] = number
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
    else:
        print("Task Id not found")
    
    


