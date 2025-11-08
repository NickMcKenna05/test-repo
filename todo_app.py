#!/usr/bin/env python3
"""
Simple To-Do List Application
A command-line interface for managing your daily tasks
"""

import json
import os
from datetime import datetime
from typing import List, Dict


class TodoList:
    """Main class for managing to-do list tasks"""

    def __init__(self, filename: str = "todos.json"):
        """Initialize the TodoList with a storage file"""
        self.filename = filename
        self.tasks: List[Dict] = []
        self.load_tasks()

    def load_tasks(self) -> None:
        """Load tasks from JSON file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    self.tasks = json.load(f)
                print(f"Loaded {len(self.tasks)} task(s) from {self.filename}")
            except json.JSONDecodeError:
                print(f"Error reading {self.filename}. Starting with empty list.")
                self.tasks = []
        else:
            print("No existing tasks found. Starting fresh!")
            self.tasks = []

    def save_tasks(self) -> None:
        """Save tasks to JSON file"""
        try:
            with open(self.filename, 'w') as f:
                json.dump(self.tasks, f, indent=2)
            print(f"Tasks saved to {self.filename}")
        except Exception as e:
            print(f"Error saving tasks: {e}")

    def add_task(self, description: str) -> None:
        """Add a new task to the list"""
        task = {
            'id': len(self.tasks) + 1,
            'description': description,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        print(f"✓ Task added: '{description}'")
        self.save_tasks()

    def list_tasks(self, show_all: bool = True) -> None:
        """Display all tasks"""
        if not self.tasks:
            print("\nNo tasks found. Your to-do list is empty!")
            return

        print("\n" + "="*60)
        print("YOUR TO-DO LIST")
        print("="*60)

        pending_tasks = [t for t in self.tasks if not t['completed']]
        completed_tasks = [t for t in self.tasks if t['completed']]

        if pending_tasks:
            print("\n📋 PENDING TASKS:")
            for task in pending_tasks:
                status = "☐"
                print(f"{status} [{task['id']}] {task['description']}")
                print(f"    Created: {task['created_at']}")

        if show_all and completed_tasks:
            print("\n✓ COMPLETED TASKS:")
            for task in completed_tasks:
                status = "☑"
                print(f"{status} [{task['id']}] {task['description']}")
                print(f"    Created: {task['created_at']}")

        print("\n" + "="*60)
        print(f"Total: {len(self.tasks)} tasks ({len(pending_tasks)} pending, {len(completed_tasks)} completed)")
        print("="*60 + "\n")

    def complete_task(self, task_id: int) -> None:
        """Mark a task as completed"""
        for task in self.tasks:
            if task['id'] == task_id:
                if task['completed']:
                    print(f"Task {task_id} is already completed!")
                else:
                    task['completed'] = True
                    print(f"✓ Task {task_id} marked as completed: '{task['description']}'")
                    self.save_tasks()
                return
        print(f"Task {task_id} not found!")

    def delete_task(self, task_id: int) -> None:
        """Delete a task from the list"""
        for i, task in enumerate(self.tasks):
            if task['id'] == task_id:
                description = task['description']
                self.tasks.pop(i)
                # Reindex remaining tasks
                for j, t in enumerate(self.tasks):
                    t['id'] = j + 1
                print(f"✗ Task deleted: '{description}'")
                self.save_tasks()
                return
        print(f"Task {task_id} not found!")

    def clear_completed(self) -> None:
        """Remove all completed tasks"""
        original_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t['completed']]
        # Reindex remaining tasks
        for i, task in enumerate(self.tasks):
            task['id'] = i + 1
        removed = original_count - len(self.tasks)
        print(f"✓ Removed {removed} completed task(s)")
        self.save_tasks()


def print_menu():
    """Display the main menu"""
    print("\n" + "="*60)
    print("TO-DO LIST MENU")
    print("="*60)
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. View pending tasks only")
    print("4. Mark task as completed")
    print("5. Delete a task")
    print("6. Clear all completed tasks")
    print("7. Exit")
    print("="*60)


def main():
    """Main application loop"""
    print("\n" + "="*60)
    print("WELCOME TO YOUR TO-DO LIST APP")
    print("="*60 + "\n")

    todo_list = TodoList()

    while True:
        print_menu()
        choice = input("\nEnter your choice (1-7): ").strip()

        if choice == '1':
            description = input("Enter task description: ").strip()
            if description:
                todo_list.add_task(description)
            else:
                print("Task description cannot be empty!")

        elif choice == '2':
            todo_list.list_tasks(show_all=True)

        elif choice == '3':
            todo_list.list_tasks(show_all=False)

        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to mark as completed: "))
                todo_list.complete_task(task_id)
            except ValueError:
                print("Invalid task ID! Please enter a number.")

        elif choice == '5':
            try:
                task_id = int(input("Enter task ID to delete: "))
                todo_list.delete_task(task_id)
            except ValueError:
                print("Invalid task ID! Please enter a number.")

        elif choice == '6':
            confirm = input("Are you sure you want to clear all completed tasks? (y/n): ").strip().lower()
            if confirm == 'y':
                todo_list.clear_completed()
            else:
                print("Operation cancelled.")

        elif choice == '7':
            print("\n" + "="*60)
            print("Thank you for using the To-Do List App!")
            print("="*60 + "\n")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()
