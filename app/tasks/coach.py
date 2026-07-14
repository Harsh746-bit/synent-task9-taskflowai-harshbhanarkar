def get_ai_coach(stats):

    if stats["total"] == 0:
        return {
            "title": "Welcome!",
            "message": "Create your first task to begin your productivity journey. 🚀"
        }

    if stats["overdue"] > 0:
        return {
            "title": "⚠️ Overdue Tasks",
            "message": f"You have {stats['overdue']} overdue task(s). Finish them first."
        }

    if stats["high_priority"] > 0:
        return {
            "title": "🔥 Today's Focus",
            "message": f"You have {stats['high_priority']} high-priority task(s). Complete them before moving to other work."
        }

    if stats["pending"] > 0:
        return {
            "title": "📋 Keep Going",
            "message": f"Only {stats['pending']} task(s) remaining. You're making great progress!"
        }

    return {
        "title": "🎉 Amazing!",
        "message": "All tasks completed. Great job today!"
    }