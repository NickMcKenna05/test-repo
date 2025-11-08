# To-Do List App

A simple, feature-rich command-line to-do list application written in Python.

## Features

- Add new tasks with automatic timestamping
- View all tasks or only pending tasks
- Mark tasks as completed
- Delete individual tasks
- Clear all completed tasks at once
- Persistent storage using JSON
- Clean, user-friendly CLI interface

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd test-repo
```

2. Make the script executable (optional):
```bash
chmod +x todo_app.py
```

## Usage

Run the application:
```bash
python3 todo_app.py
```

Or, if you made it executable:
```bash
./todo_app.py
```

## Menu Options

1. **Add a new task** - Create a new task with a description
2. **View all tasks** - Display both pending and completed tasks
3. **View pending tasks only** - Show only tasks that are not completed
4. **Mark task as completed** - Mark a specific task as done
5. **Delete a task** - Remove a task from the list
6. **Clear all completed tasks** - Remove all completed tasks at once
7. **Exit** - Save and exit the application

## Data Storage

Tasks are automatically saved to `todos.json` in the same directory as the application. This file is created automatically and persists between sessions.

## Example

```
TO-DO LIST MENU
1. Add a new task
2. View all tasks
3. View pending tasks only
4. Mark task as completed
5. Delete a task
6. Clear all completed tasks
7. Exit

Enter your choice (1-7): 1
Enter task description: Buy groceries
✓ Task added: 'Buy groceries'
```

## License

This project is open source and available for personal and educational use.
