from .validation import validate_task


def add_task(tasks, title, description, due_date):
    if not isinstance(tasks, list):
        raise TypeError("tasks must be a list")

    try:
        validate_task(title, description, due_date)
    except ValueError as exc:
        return False, str(exc)

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
    if len(tasks) == 0:
        return 0.0

    completed_tasks = 0

    for task in tasks:
        if task["completed"]:
            completed_tasks += 1

    return (completed_tasks / len(tasks)) * 100
