from datetime import datetime


def validate_task_title(title):
    if not isinstance(title, str):
        return False, "Task title must be a non-empty string."
    if len(title) == 0 or len(title.strip()) == 0:
        return False, "Task title must be a non-empty string."
    if len(title.strip()) > 100:
        return False, "Task title must be 100 characters or fewer."
    return True, ""


def validate_task_description(description):
    if not isinstance(description, str):
        return False, "Task description must be a non-empty string."
    if len(description) == 0 or len(description.strip()) == 0:
        return False, "Task description must be a non-empty string."
    if len(description) > 500:
        return False, "Task description cannot exceed 500 characters."
    if len(description.strip()) > 255:
        return False, "Task description must be 255 characters or fewer."
    return True, ""


def validate_due_date(due_date):
    if not isinstance(due_date, str):
        return False, "Due date must be a non-empty string in YYYY-MM-DD format."
    if len(due_date) == 0 or len(due_date.strip()) == 0:
        return False, "Due date must be a non-empty string in YYYY-MM-DD format."

    try:
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
        return True, ""
    except ValueError:
        return False, "Due date must be in YYYY-MM-DD format."


def validate_task(title, description, due_date):
    if not isinstance(title, str):
        raise ValueError("Title must be a string")
    if len(title) == 0:
        raise ValueError("Title cannot be empty")

    if not isinstance(description, str):
        raise ValueError("Description must be a string")
    if len(description) == 0:
        raise ValueError("Description cannot be empty")

    if not isinstance(due_date, str):
        raise ValueError("Due date must be a string")
    if len(due_date) == 0:
        raise ValueError("Due date cannot be empty")

    try:
        datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Due date must be in YYYY-MM-DD format")

    return True
