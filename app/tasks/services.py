from app import db
from app.models.task import Task


# -------------------------
# Create Task
# -------------------------
def create_task(form, user_id):

    task = Task(
        title=form.title.data,
        description=form.description.data,
        category=form.category.data,
        priority=form.priority.data,
        due_date=form.due_date.data,
        user_id=user_id
    )

    db.session.add(task)
    db.session.commit()

    return task


# -------------------------
# Get All Tasks
# -------------------------
def get_user_tasks(user_id):

    return (
        Task.query
        .filter_by(user_id=user_id)
        .order_by(Task.created_at.desc())
        .all()
    )


# -------------------------
# Get Single Task
# -------------------------
def get_task_by_id(task_id, user_id):

    return Task.query.filter_by(
        id=task_id,
        user_id=user_id
    ).first()


# -------------------------
# Update Task
# -------------------------
def update_task(task, form):

    task.title = form.title.data
    task.description = form.description.data
    task.category = form.category.data
    task.priority = form.priority.data
    task.due_date = form.due_date.data

    db.session.commit()


# -------------------------
# Delete Task
# -------------------------
def delete_task(task):

    db.session.delete(task)
    db.session.commit()


# -------------------------
# Complete Task
# -------------------------
def complete_task(task):

    task.status = "Completed"

    db.session.commit()


# -------------------------
# Create AI Task
# -------------------------
def create_ai_task(result, user_id):

    goal = result.get("goal", "AI Generated Task")

    timeline = result.get("timeline", [])
    tips = result.get("tips", "No AI tips available.")

    description = ""

    if timeline:
        for step in timeline:
            description += f"• {step}\n"
    else:
        description += "No timeline generated.\n"

    description += "\n\nAI Tips:\n"
    description += tips

    task = Task(
        title=goal,
        description=description,
        category="AI Planner",
        priority="Medium",
        status="Pending",
        user_id=user_id
    )

    db.session.add(task)
    db.session.commit()

    return task