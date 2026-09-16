# CLI TASK TRACKER

A simple command-line task tracker built with Python. It allows you to create, update, delete, and manage tasks directly from your terminal.

Tasks are stored locally in a `tasks.json` file, so your data persists between program runs.

## Features

* Add new tasks
* Update existing tasks
* Delete tasks
* Mark tasks as `done`
* Mark tasks as `In-progress`
* List all tasks by status
* List completed tasks
* List in-progress tasks
* List tasks that are not completed
* Automatically assign task IDs
* Automatically update task timestamps
* Store tasks in a local JSON file
* Handle invalid task IDs and missing arguments

## Requirements

* Python 3.x
* No external libraries or frameworks are required.

The project uses Python's built-in modules.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/MonicaGodwin/Task_Tracker.git
```

### 2. Navigate into the project directory

```bash
cd Task_Tracker
cd json-data
```

### 3. Run the application

```bash
python3 main.py
```

The application stores your tasks in:

```text
tasks.json
```

If the file does not exist, it will be created automatically.

---

# Usage

The general command structure is:

```bash
python3 main.py <command> <arguments>
```

## Add a Task

Use the `add` command followed by the task description.

```bash
python3 main.py add "Learn Python"
```

Example output:

```text
Task added successfully! (ID: 1)
```

A new task is created with the default status:

```text
Todo
```

---

## Update a Task

Use `update`, followed by the task ID and the new description.

```bash
python3 main.py update 1 "Learn Python and SQLite"
```

The task's description will be updated, and its `updated_at` timestamp will change.

The original `created_at` timestamp remains unchanged.

---

## Delete a Task

Use `delete`, followed by the task ID.

```bash
python3 main.py delete 1
```

After a task is deleted, the remaining tasks are automatically re-numbered.

For example:

```text
Before deletion:

1. Learn Python
2. Learn Flask
3. Learn FastAPI
```

If task `2` is deleted:

```text
After deletion:

1. Learn Python
2. Learn FastAPI
```

---

## Mark a Task as Done

Use:

```bash
python3 main.py mark-done 1
```

The task's status will become:

```text
done
```

Its `updated_at` timestamp will also be updated.

---

## Mark a Task as In-Progress

Use:

```bash
python3 main.py mark-in-progress 1
```

The task's status will become:

```text
In-progress
```

---

# Listing Tasks

The `list` command allows you to view tasks based on their status.

## List Completed Tasks

```bash
python3 main.py list done
```

This displays all tasks whose status is:

```text
done
```

## List In-Progress Tasks

```bash
python3 main.py list in-progress
```

This displays all tasks whose status is:

```text
In-progress
```

## List Not-Completed Tasks

```bash
python3 main.py list todo
```

This displays tasks whose status is either:

```text
Todo
```

# Task Data

Each task is stored in `tasks.json` with information similar to:

```json
{
    "id": 1,
    "description": "Learn Python",
    "status": "Todo",
    "created_at": "Wed Sep 16 10:30:00 2026",
    "updated_at": "Wed Sep 16 10:30:00 2026"
}
```

### Fields

| Field         | Description                     |
| ------------- | ------------------------------- |
| `id`          | The task's current ID           |
| `description` | Description of the task         |
| `status`      | Current task status             |
| `created_at`  | Time the task was created       |
| `updated_at`  | Time the task was last modified |

## Task Statuses

The tracker uses the following statuses:

| Status        | Meaning                           |
| ------------- | --------------------------------- |
| `Todo`        | Task has not been started         |
| `In-progress` | Task is currently being worked on |
| `done`        | Task has been completed           |

---

# Example Workflow

You can use the tracker like this:

### Add some tasks

```bash
python3 main.py add "Learn Python"
python3 main.py add "Learn SQLite"
python3 main.py add "Build a REST API"
```

### Start working on a task

```bash
python3 main.py mark-in-progress 1
```

### Complete the task

```bash
python3 main.py mark-done 1
```

### Update another task

```bash
python3 main.py update 2 "Learn SQLite with Python"
```

### View completed tasks

```bash
python3 main.py list done
```

### View tasks that aren't completed

```bash
python3 main.py list not-done
```

### Delete a task

```bash
python3 main.py delete 3
```

---

# Error Handling

The application checks for common input errors, including:

* Missing command arguments
* Invalid task IDs
* Task IDs that don't exist
* Invalid task status filters

For example:

```bash
python3 main.py delete abc
```

will produce an error because task IDs must be integers.

Similarly, trying to update a task that does not exist will notify you that the task ID could not be found.

---

# Project Structure

A simple project structure looks like:

```text
task-tracker/
│__json.data/
├     main.py
├     tasks.json
└     README.md
```

`tasks.json` is created automatically when the application is run and does not already exist.

---

# Technologies Used

* **Python 3**
* **JSON**
* **Python Standard Library**

No external libraries or frameworks are required.

## License

This project is open source and available for learning and personal use.
