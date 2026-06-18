from datetime import datetime


def validate_task_title(title):
    if not isinstance(title, str) or not title.strip():
        return False, "Task title must be a non-empty string."
    if len(title.strip()) > 100:
        return False, "Task title must be 100 characters or fewer."
    return True, ""


def validate_task_description(description):
    if not isinstance(description, str) or not description.strip():
        return False, "Task description must be a non-empty string."
    if len(description.strip()) > 255:
        return False, "Task description must be 255 characters or fewer."
    return True, ""


def validate_due_date(due_date):
    if not isinstance(due_date, str) or not due_date.strip():
        return False, "Due date must be a non-empty string in YYYY-MM-DD format."

    try:
        datetime.strptime(due_date.strip(), "%Y-%m-%d")
        return True, ""
    except ValueError:
        return False, "Due date must be in YYYY-MM-DD format."
