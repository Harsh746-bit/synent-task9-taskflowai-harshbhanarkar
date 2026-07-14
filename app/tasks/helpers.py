from datetime import datetime


def get_greeting():

    hour = datetime.now().hour

    if hour < 12:
        return "🌞 Good Morning"

    elif hour < 17:
        return "🌤 Good Afternoon"

    else:
        return "🌙 Good Evening"


def get_today():

    return datetime.now().strftime("%A, %d %B %Y")