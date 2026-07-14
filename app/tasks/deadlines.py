from datetime import date

def get_upcoming_tasks(tasks):

    today = date.today()

    upcoming = []

    for task in tasks:

        if (
            task.due_date
            and task.status != "Completed"
        ):

            days = (task.due_date - today).days

            if days <= 7:

                upcoming.append({
                    "title": task.title,
                    "days": days
                })

    upcoming.sort(key=lambda x: x["days"])

    return upcoming