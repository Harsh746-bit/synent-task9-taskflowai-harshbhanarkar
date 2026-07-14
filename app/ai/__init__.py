from flask import Blueprint

ai = Blueprint(
    "ai",
    __name__,
    template_folder="../templates"
)

from app.ai import routes