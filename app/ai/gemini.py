import os

from dotenv import load_dotenv
from google import genai
from google.genai.errors import ServerError

from .prompts import (
    build_task_prompt,
    build_planner_prompt
)

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


# ----------------------------
# Analyze Task
# ----------------------------

def analyze_task(task):

    try:

        prompt = build_task_prompt(task)

        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL"),
            contents=prompt,
            config={
                "response_mime_type": "application/json"
            }
        )

        print("\n========== ANALYZE ==========")
        print(response.text)
        print("=============================\n")

        return response.parsed if response.parsed else response.text

    except ServerError as e:

        print("Server Error:", e)

        return {
            "difficulty": "Unavailable",
            "estimated_time": "Unavailable",
            "suggested_priority": "Unavailable",
            "suggested_deadline": "Unavailable",
            "summary": "Gemini AI is busy.",
            "subtasks": [],
            "tips": "Please try again later."
        }

    except Exception as e:

        print("Analyze Error:", e)

        return {
            "difficulty": "Error",
            "estimated_time": "Error",
            "suggested_priority": "Error",
            "suggested_deadline": "Error",
            "summary": str(e),
            "subtasks": [],
            "tips": str(e)
        }


# ----------------------------
# Generate Planner
# ----------------------------

import json
import re

def generate_plan(goal):

    try:

        prompt = build_planner_prompt(goal)

        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL"),
            contents=prompt
        )

        print("\n========= RAW GEMINI =========")
        print(repr(response.text))
        print("==============================\n")

        text = response.text.strip()

        # Remove markdown if present
        text = text.replace("```json", "").replace("```", "").strip()

        # Extract JSON object
        match = re.search(r"\{.*\}", text, re.DOTALL)

        if not match:
            raise ValueError(f"No JSON found.\n{text}")

        return json.loads(match.group())

    except Exception as e:

        print("Planner Error:", repr(e))

        return {
            "goal": goal,
            "difficulty": "Unavailable",
            "estimated_time": "Unavailable",
            "timeline": [
                "AI service unavailable"
            ],
            "tips": str(e)
        }


# ----------------------------
# AI Chat Assistant
# ----------------------------

def ask_ai(question):

    try:

        prompt = f"""
You are TaskFlowAI.

You are an AI productivity assistant.

Answer briefly and practically.

Question:
{question}
"""

        response = client.models.generate_content(
            model=os.getenv("GEMINI_MODEL"),
            contents=prompt
        )

        return response.text

    except ServerError:

        return "⚠️ Gemini AI is currently busy. Please try again later."

    except Exception as e:

        print("Assistant Error:", e)

        return f"⚠️ {str(e)}"