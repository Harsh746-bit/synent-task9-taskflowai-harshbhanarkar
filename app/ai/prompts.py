def build_task_prompt(task):

    return f"""
You are an expert project planner and productivity coach.

Analyze the following task.

Title:
{task.title}

Description:
{task.description}

Category:
{task.category}

Priority:
{task.priority}

Due Date:
{task.due_date}

Current Status:
{task.status}

Return ONLY valid JSON.

{{
    "difficulty": "",
    "estimated_time": "",
    "suggested_priority": "",
    "suggested_deadline": "",
    "summary": "",
    "subtasks": [
        "",
        "",
        ""
    ],
    "tips": ""
}}

Return only JSON.
"""


def build_planner_prompt(goal):

    return f"""
You are an AI Productivity Coach.

The user wants to achieve this goal:

{goal}

Generate a complete action plan.

Return ONLY valid JSON.

{{
    "goal": "",
    "difficulty": "",
    "estimated_time": "",
    "timeline": [
        "",
        "",
        "",
        ""
    ],
    "tips": ""
}}

Return only JSON.
"""