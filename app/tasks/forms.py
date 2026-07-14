from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    SelectField,
    DateField,
    SubmitField
)
from wtforms.validators import DataRequired, Length


class TaskForm(FlaskForm):

    title = StringField(
        "Task Title",
        validators=[
            DataRequired(),
            Length(min=3, max=150)
        ]
    )

    description = TextAreaField(
        "Description"
    )

    category = SelectField(
        "Category",
        choices=[
            ("Internship", "Internship"),
            ("College", "College"),
            ("Placement", "Placement"),
            ("DSA", "DSA"),
            ("Personal", "Personal"),
            ("Health", "Health"),
            ("Finance", "Finance"),
            ("Other", "Other"),
        ]
    )

    priority = SelectField(
        "Priority",
        choices=[
            ("Low", "Low"),
            ("Medium", "Medium"),
            ("High", "High"),
        ]
    )

    due_date = DateField(
        "Due Date",
        format="%Y-%m-%d"
    )

    submit = SubmitField("Create Task")