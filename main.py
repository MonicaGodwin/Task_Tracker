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
        print('Usage: python task_tracker.py add "Your task description here"')
        sys.exit()
        
    description = sys.argv[2]
    next_id = len(tasks) + 1 # Calculates the next id position 
    current_time = time.ctime()
    new_tasks = {
    "id": next_id,
    "description": description,
    "status": "To do",  # Tasks start as "todo" by default
    "created_at": current_time,
    "updated_at": current_time
    }
    tasks.append(new_tasks)
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
        
    print(f"Task added successfully! (ID: {next_id})")


elif command == "list":
    if len(tasks) == "":
        print("No task to display.")
    else:
        for task in tasks:
            print(f"{task["id"]} - {task["description"]} - {task["status"]}")