from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request,
    session,
    jsonify
)

from flask_login import login_required, current_user

from . import ai

from .gemini import (
    analyze_task,
    generate_plan,
    ask_ai
)

from app.tasks.services import (
    get_task_by_id,
    create_ai_task
)


# -------------------------
# AI Task Analysis
# -------------------------
@ai.route("/analyze-task/<int:task_id>")
@login_required
def analyze(task_id):

    task = get_task_by_id(task_id, current_user.id)

    if not task:
        flash("Task not found.", "danger")
        return redirect(url_for("tasks.my_tasks"))

    result = analyze_task(task)

    print("\n========== ANALYZE RESULT ==========")
    print(result)
    print("===================================\n")

    return render_template(
        "ai/analysis.html",
        task=task,
        result=result
    )


# -------------------------
# AI Planner
# -------------------------
@ai.route("/planner", methods=["GET", "POST"])
@login_required
def planner():

    if request.method == "POST":

        goal = request.form.get("goal")

        print("\n========== GOAL ==========")
        print(goal)

        result = generate_plan(goal)

        print("\n========== RESULT ==========")
        print(result)
        print(type(result))
        print("===========================\n")

        session["planner_result"] = result

        return render_template(
            "ai/planner_result.html",
            result=result
        )

    return render_template("ai/planner.html")


# -------------------------
# Save AI Plan
# -------------------------
@ai.route("/save-plan", methods=["POST"])
@login_required
def save_plan():

    result = session.get("planner_result")

    if not result:
        flash("No AI plan found.", "danger")
        return redirect(url_for("ai.planner"))

    print("\n========== SAVING PLAN ==========")
    print(result)
    print("=================================\n")

    create_ai_task(result, current_user.id)

    session.pop("planner_result", None)

    flash("AI Plan added successfully!", "success")

    return redirect(url_for("tasks.my_tasks"))


# -------------------------
# AI Assistant
# -------------------------
@ai.route("/assistant", methods=["POST"])
@login_required
def assistant():

    data = request.get_json()

    if not data:
        return jsonify({
            "response": "No message received."
        })

    message = data.get("message", "")

    response = ask_ai(message)

    return jsonify({
        "response": response
    })