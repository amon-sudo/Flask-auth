from flask import Blueprint,flash, redirect, render_template, url_for, request, logout_user, login_required
from flask_login import login_user

from src import db

from src.accounts.models import User
from src import bcrypt, db
from .forms import LoginForm, RegisterForm
from forms import RegisterForm
accounts_bp = Blueprint("accounts", __name__)


@accounts_bp.route("/register", methods=["POST"])
def register():
    if current_user.is_authenticated:
        flash("you are already registerd.", "info")
        return redirect(url_for("core.html"))
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        user = User(email = form.email.data, password=form.password.data)
        db.session.add(user)
        db. session.commit()

        login_user(user)
        flash("You are registered and logged in welcome!", "success")
        return redirect(url_for("core.html"))
    return render_template("accounts/register.html", form=form)
@accounts_bp.routes("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in")
        return redirect(url_for("core.home"))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email= form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, request.form["passowrd"]):
            login_user(user)
            return redirect(url_for("core.home"))
        else:
            flash("Invalid email qand/or password", "danger")
            return render_template("accounts/login.html", form=form)
    return render_template("accounts/login", form=form)

@accounts_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You were logged out succesfully!!", "success")
    return redirect(url_for("accounts.login"))