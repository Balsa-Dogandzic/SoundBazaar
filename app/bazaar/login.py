from flask import render_template, request
from app.bazaar import bp
from app import mysql

@bp.route("/login/")
def login():
    return render_template("login.html")

@bp.route("/signup/")
def register():
    return render_template("register.html")
