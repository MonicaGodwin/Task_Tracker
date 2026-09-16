import json
import os
import sys
import time
# Create a dictionary of task fields
task = {
    "id" : "Id",
    "description" : "Description",
    "status" : "Status",
    "created_at" : "CreatedAt",
    "updated_at" : "UpdatedAt"
}

# Us os to check if file exists and if not, create a newfile
if not os.path.exists("tasks.json"):
    tasks = []
    with open("tasks.json", "w") as file:
        json.dump(tasks,file,indent=4) # Write the python list into a json file.
else:
    with open("tasks.json", "r") as data:
        tasks = json.load(data) # read the json file as a python list

# Use argument values(it stores the terminal input as a list)
#  to recieve data from the terminal      
if len(sys.argv) < 2:
    print("Usage: python main.py [add | list | delete]")
    sys.exit()
    
command = sys.argv[1].lower()

        
if command == "add":
    if len(sys.argv) > 3:
        print('Usage: python3 [main.py] [add] ["Task description"]')
        sys.exit()
    elif len(sys.argv) < 3:
        print("Error: Please provide a task description.")
        sys.exit()
        
    description = sys.argv[2]
    next_id = len(tasks) + 1 # Calculates the next task id position 
    current_time = time.ctime()
    new_tasks = {
    "id": next_id,
    "description": description,
    "status": "todo",  # Tasks start as "todo" by default
    "created_at": current_time,
    "updated_at": current_time
    }
    tasks.append(new_tasks)
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
        
    print(f"Task added successfully! (ID: {next_id})")


elif command == "list":
    if len(sys.argv) > 2:
        print(f"Usage: python3 [main.py] [list]")
        sys.exit()
    elif len(sys.argv) < 2:
        print(f"Error: please provide the command argument\n")
        sys.exit()
        
    if len(tasks) == 0: # checks if the list is empty
        print("No task to display.")
    else:
        for task in tasks:
            print(f"{task['id']} - {task['description']} - {task['status']} - {task['created_at']} - {task['updated_at']}")

elif command == "delete":
    if len(sys.argv) > 3:
        print(f'Usage: python3 [main.py] [delete] [The task Id to delete]')
        sys.exit()
    elif len(sys.argv) < 3:
        print(f"Error: please provide a task id number to delete\n")
        sys.exit()

    task_id = sys.argv[2]
    # Use python's try and except to handle error smoothly
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
        for number, task in enumerate(tasks, start=1): # Use the enumerate module to re-order the tasks starting from 1
            task["id"] = number
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
    else:
        print("Task Id not found")
    
elif command == "update":
    if len(sys.argv) > 4:
        print('Usage: python3 [main.py] [update] [The task Id to update] ["New description"]')
        sys.exit()
    elif len(sys.argv) < 4:
        print("Error: please provide a task id or description to update\n")
        sys.exit()

    updated = False
    task_id = sys.argv[2]
    description = sys.argv[3]
    current_time = time.ctime
    try:
        task_id = int(task_id)
    except ValueError:
        print("Must be an integer")
        sys.exit()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = description
            task["updated_at"] = current_time()
            updated = True
            print("Task Updated")
            break
    if updated:
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
    else:
        print("Task Id not found")

elif command == "mark-done" or command == "mark-in-progress":
    if len(sys.argv) < 3:
        print('Usage: python3 [main.py] [mark-done] | [mark-in-progress] ["The task Id to mark done"]')
        sys.exit()
    elif len(sys.argv) > 3:
        print("Error: please provide a task id number to mark done")
        sys.exit()

    status_update = False
    status = ""
    current_time = time.ctime
    if command == "mark-done":
        status = "done"
    else:
        status = "in-progress"
    task_id = sys.argv[2]
    try:
        task_id = int(task_id)
    except ValueError:
        print("Must be an integer")
        sys.exit()

    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            task["updated_at"] = current_time()
            status_update = True
            print(f"Status marked as {status}")
            break
    if status_update:
        with open("tasks.json", "w") as file:
            json.dump(tasks, file, indent=4)
    else:
        print(f"Could not mark status as {status}")

elif command == "list-by-status":
    if len(sys.argv) < 3:
        print('Usage: python3 main.py list [todo] | [in-progress] | [done] | [not-done]')
        sys.exit()
    elif len(sys.argv) > 3:
        print("Error: Argument should not be more than 3")
        sys.exit()

    list_task = False
    task_status = sys.argv[2].lower()
    for specified_task in tasks:
        if task_status == "done":
            if specified_task["status"] in ["todo", "in-progress"]:
                list_task = True
                print(specified_task)
        elif specified_task["status"] == task_status:
            list_task = True
            print(specified_task)
    if not list_task:
        print(f"No task found with the status: {task_status}")