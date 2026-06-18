from .validation import validate_task_title, validate_task_description, validate_due_date


def add_task(tasks, title, description, due_date):
    if not isinstance(tasks, list):
        raise TypeError("tasks must be a list")

    valid, message = validate_task_title(title)
    if not valid:
        return False, message

    valid, message = validate_task_description(description)
    if not valid:
        return False, message

    valid, message = validate_due_date(due_date)
    if not valid:
        return False, message

    task = {
        "title": title.strip(),
        "description": description.strip(),
        "due_date": due_date.strip(),
        "completed": False,
    }
    tasks.append(task)
    return True, "Task added successfully!"


def mark_task_as_complete(tasks, index):
    if not isinstance(tasks, list):
        raise TypeError("tasks must be a list")

    if not isinstance(index, int) or index < 0 or index >= len(tasks):
        return False, "Invalid task number."

    if tasks[index].get("completed"):
        return False, "Task is already completed."

    tasks[index]["completed"] = True
    return True, "Task marked as complete!"


def view_pending_tasks(tasks):
    return [task for task in tasks if not task.get("completed", False)]


def calculate_progress(tasks):
    if not isinstance(tasks, list):
        raise TypeError("tasks must be a list")

    if not tasks:
        return 0.0

    completed_count = sum(1 for task in tasks if task.get("completed", False))
    return round((completed_count / len(tasks)) * 100, 2)
