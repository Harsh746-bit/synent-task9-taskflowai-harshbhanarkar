from datetime import date
from app.models.task import Task


def get_dashboard_stats(user_id):
    """
    Calculate dashboard statistics for a specific user.
    """

    tasks = Task.query.filter_by(user_id=user_id).all()

    total_tasks = len(tasks)

    pending_tasks = sum(
        1 for task in tasks
        if task.status == "Pending"
    )

    completed_tasks = sum(
        1 for task in tasks
        if task.status == "Completed"
    )

    high_priority = sum(
        1 for task in tasks
        if task.priority == "High"
    )

    overdue_tasks = sum(
        1 for task in tasks
        if (
            task.due_date
            and task.due_date < date.today()
            and task.status != "Completed"
        )
    )

    completion_rate = 0

    if total_tasks > 0:
        completion_rate = round(
            (completed_tasks / total_tasks) * 100
        )

    return {
        "total": total_tasks,
        "pending": pending_tasks,
        "completed": completed_tasks,
        "overdue": overdue_tasks,
        "high_priority": high_priority,
        "completion_rate": completion_rate
    }