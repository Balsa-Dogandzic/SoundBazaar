from flask import render_template, request
from app.bazaar import bp
from app import mysql

@bp.route("/songs/")
def songs():
    return render_template("songs.html")

@bp.route("/songs/upload/")
def upload_song():
    return render_template("upload_song.html")