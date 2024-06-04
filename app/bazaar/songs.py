from flask import render_template, request, current_app, redirect, session, abort
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


@bp.route("/songs/update/<int:id>/", methods=['GET', 'POST'])
def update_song(id):
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
        cursor.execute(f"UPDATE  song SET title='{title}', duration='{duration}', song='{filename}', author_id={author}, genre_id={genre} WHERE id={id}")
        mysql.connection.commit()
        cursor.close()
        return redirect('/songs/')
    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT * FROM song WHERE id={id}")
    song = cursor.fetchone()
    cursor.execute("SELECT * FROM author ORDER BY name")
    authors = cursor.fetchall()
    cursor.execute("SELECT * FROM genre ORDER BY genre")
    genres = cursor.fetchall()
    cursor.close()
    if song:
        return render_template("update_song.html", song=song, authors=authors, genres=genres)
    return abort(404)
    


@bp.route("/songs/delete/<int:id>/")
def delete_song(id):
    if session.get('user_type') != 2:
        return redirect("/songs/")
    cursor = mysql.connection.cursor()
    cursor.execute(f"DELETE FROM song WHERE id={id}")
    mysql.connection.commit()
    cursor.close()
    return redirect("/songs/")
