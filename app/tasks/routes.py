from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from . import tasks
from .helpers import get_greeting, get_today
from .forms import TaskForm
from .services import (
    create_task,
    get_user_tasks,
    get_task_by_id,
    update_task,
    delete_task,
    complete_task
)
from .analytics import get_dashboard_stats
from .coach import get_ai_coach
from .deadlines import get_upcoming_tasks


# -------------------------
# Home Page
# -------------------------
@tasks.route("/")
def home():
    return render_template("home.html")


# -------------------------
# Dashboard
# -------------------------
@tasks.route("/dashboard")
@login_required
def dashboard():

    tasks_list = get_user_tasks(current_user.id)

    stats = get_dashboard_stats(current_user.id)

    greeting = get_greeting()

    today = get_today()

    coach = get_ai_coach(stats)

    upcoming = get_upcoming_tasks(tasks_list)

    from collections import Counter

    category_counter = Counter(
        task.category for task in tasks_list
    )

    category_labels = list(category_counter.keys())

    category_counts = list(category_counter.values())

    return render_template(
        "tasks/dashboard.html",
        tasks=tasks_list,
        stats=stats,
        greeting=greeting,
        today=today,
        coach=coach,
        upcoming=upcoming,
        category_labels=category_labels,
        category_counts=category_counts
    )


# -------------------------
# Create Task
# -------------------------
@tasks.route("/create-task", methods=["GET", "POST"])
@login_required
def create_task_page():

    form = TaskForm()

    if form.validate_on_submit():

        create_task(form, current_user.id)

        flash("Task created successfully!", "success")

        return redirect(url_for("tasks.dashboard"))

    return render_template(
        "tasks/create_task.html",
        form=form
    )


# -------------------------
# My Tasks
# -------------------------
@tasks.route("/my-tasks")
@login_required
def my_tasks():

    tasks_list = get_user_tasks(current_user.id)

    return render_template(
        "tasks/my_tasks.html",
        tasks=tasks_list
    )


# -------------------------
# Edit Task
# -------------------------
@tasks.route("/edit-task/<int:task_id>", methods=["GET", "POST"])
@login_required
def edit_task(task_id):

    task = get_task_by_id(task_id, current_user.id)

    if not task:
        flash("Task not found.", "danger")
        return redirect(url_for("tasks.my_tasks"))

    form = TaskForm(obj=task)

    if form.validate_on_submit():

        update_task(task, form)

        flash("Task updated successfully!", "success")

        return redirect(url_for("tasks.my_tasks"))

    return render_template(
        "tasks/edit_task.html",
        form=form
    )


# -------------------------
# Delete Task
# -------------------------
@tasks.route("/delete-task/<int:task_id>")
@login_required
def delete_task_route(task_id):

    task = get_task_by_id(task_id, current_user.id)

    if not task:
        flash("Task not found.", "danger")
        return redirect(url_for("tasks.my_tasks"))

    delete_task(task)

    flash("Task deleted successfully.", "success")

    return redirect(url_for("tasks.my_tasks"))


# -------------------------
# Complete Task
# -------------------------
@tasks.route("/complete-task/<int:task_id>")
@login_required
def complete_task_route(task_id):

    task = get_task_by_id(task_id, current_user.id)

    if not task:
        flash("Task not found.", "danger")
        return redirect(url_for("tasks.my_tasks"))

    complete_task(task)

    flash("Task marked as completed!", "success")

    return redirect(url_for("tasks.my_tasks"))