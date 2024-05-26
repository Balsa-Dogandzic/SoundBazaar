from flask import Blueprint, render_template

songs_bp = Blueprint("songs_bp", __name__)

@songs_bp.route("/songs/")
def songs():
    return render_template("songs.html")

@songs_bp.route("/songs/upload/")
def upload_song():
    return render_template("upload_song.html")