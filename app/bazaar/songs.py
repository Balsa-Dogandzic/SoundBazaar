from flask import render_template, request, current_app, redirect, session
from werkzeug.utils import secure_filename
from app.bazaar import bp
from app import mysql
import os

@bp.route("/songs/")
def songs():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT song.*, author.name FROM song JOIN author ON song.author_id = author.id ORDER BY song.title")
    songs = cursor.fetchall()
    return render_template("songs.html", songs=songs)

@bp.route("/songs/upload/", methods=['GET', 'POST'])
def upload_song():
    if session.get('user_type') != 2:
        return redirect('/songs/')
    if request.method == 'POST':
        title = request.form['title']
        duration = request.form['duration']
        file = request.files['file']
        filename = secure_filename(file.filename)
        file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
        author = request.form['author']
        genre = request.form['genre']
        cursor = mysql.connection.cursor()
        cursor.execute(f"INSERT INTO song VALUES (NULL, '{title}','{duration}','{filename}',{author},{genre})")
        mysql.connection.commit()
        cursor.close()
        return redirect('/songs/')
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM author ORDER BY name")
    authors = cursor.fetchall()
    cursor.execute("SELECT * FROM genre ORDER BY genre")
    genres = cursor.fetchall()
    cursor.close()
    return render_template("upload_song.html", authors=authors, genres=genres)