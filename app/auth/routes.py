from flask import render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required

from . import auth
from .forms import RegistrationForm, LoginForm
from app import db
from app.models.user import User


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():

        # Check if email already exists
        existing_user = User.query.filter_by(email=form.email.data).first()

        if existing_user:
            flash("Email already registered.", "danger")
            return redirect(url_for("auth.register"))

        # Check if username already exists
        existing_username = User.query.filter_by(username=form.username.data).first()

        if existing_username:
            flash("Username already exists.", "danger")
            return redirect(url_for("auth.register"))

        # Hash password
        hashed_password = generate_password_hash(form.password.data)

        # Create user
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        flash("Registration successful! Please login.", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):
            login_user(user)

            flash("Login successful!", "success")
            return redirect(url_for("tasks.dashboard"))

        flash("Invalid email or password.", "danger")

    return render_template("auth/login.html", form=form)
@auth.route("/logout")
@login_required
def logout():
    logout_user()

    flash("Logged out successfully.", "success")

    return redirect(url_for("tasks.home"))