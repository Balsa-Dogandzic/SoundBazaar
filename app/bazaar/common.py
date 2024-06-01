from flask import render_template, request, send_from_directory, current_app
from app.bazaar import bp
from app import mysql

@bp.route('/media/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)

@bp.route("/")
def index():
    return render_template("index.html")

@bp.route("/about/")
def about():
    return render_template("about.html")

@bp.route("/contact/")
def contact():
    return render_template("contact.html")
