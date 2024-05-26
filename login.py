from flask import Blueprint, render_template

login_bp = Blueprint("login_bp", __name__)

@login_bp.route("/login/")
def login():
    return render_template("login.html")

@login_bp.route("/signup/")
def register():
    return render_template("register.html")