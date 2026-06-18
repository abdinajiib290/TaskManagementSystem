import sys
import select

from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress


def stdin_has_data():
    if sys.stdin.isatty():
        return True
    ready, _, _ = select.select([sys.stdin], [], [], 0)
    return bool(ready)


def display_menu():
    print("\nTask Management System")
    print("1. Add a task")
    print("2. Mark a task as complete")
    print("3. View pending tasks")
    print("4. View all tasks")
    print("5. Show progress")
    print("6. Exit")


def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task.get("completed") else "Pending"
        print(f"{index}. {task['title']} ({status})")
        print(f"   Description: {task['description']}")
        print(f"   Due date: {task['due_date']}")


def safe_input(prompt):
    try:
        return input(prompt)
    except EOFError:
        return None


def prompt_for_task_details():
    title = safe_input("Enter task title: ")
    if title is None:
        return None, None, None

    description = safe_input("Enter task description: ")
    if description is None:
        return None, None, None

    due_date = safe_input("Enter due date (YYYY-MM-DD): ")
    if due_date is None:
        return None, None, None

    return title.strip(), description.strip(), due_date.strip()


def main():
    tasks = []

    while True:
        if not sys.stdin.isatty() and not stdin_has_data():
            break

        display_menu()
        choice = safe_input("Choose an option (1-6): ")
        if choice is None:
            break
        choice = choice.strip()

        if choice == "1":
            title, description, due_date = prompt_for_task_details()
            if title is None:
                break

            success, message = add_task(tasks, title, description, due_date)
            print(message)

        elif choice == "2":
            if not tasks:
                print("No tasks available to mark as complete.")
                continue

            display_tasks(tasks)
            selected = safe_input("Enter the number of the task to mark complete: ")
            if selected is None:
                break
            selected = selected.strip()
            if not selected.isdigit():
                print("Please enter a valid task number.")
                continue

            task_index = int(selected) - 1
            success, message = mark_task_as_complete(tasks, task_index)
            print(message)

        elif choice == "3":
            pending_tasks = view_pending_tasks(tasks)
            if not pending_tasks:
                print("No pending tasks.")
            else:
                display_tasks(pending_tasks)

        elif choice == "4":
            display_tasks(tasks)

        elif choice == "5":
            progress = calculate_progress(tasks)
            print(f"Progress: {progress}% complete")

        elif choice == "6":
            print("Exiting Task Management System.")
            break

        else:
            print("Invalid selection. Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()
