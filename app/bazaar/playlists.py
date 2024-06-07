from flask import render_template, request, redirect, session, abort
from app.bazaar import bp
from app import mysql
import datetime

@bp.route("/playlists/")
def all_playlists():
    if not session.get('user'):
        return redirect('/')
    cursor = mysql.connection.cursor()
    cursor.execute(f"""
    SELECT 
        playlist.*,
        COUNT(playlist_entry.song_id) AS number_of_songs,
        SEC_TO_TIME(COALESCE(SUM(TIME_TO_SEC(song.duration)),0)) AS total_duration
    FROM 
        playlist
    LEFT JOIN 
        playlist_entry ON playlist.id = playlist_entry.playlist_id
    LEFT JOIN 
        song ON playlist_entry.song_id = song.id
    WHERE 
        playlist.user_id = {session.get('user')}
    GROUP BY 
        playlist.id
    ORDER BY 
        playlist.title
    """)
    playlists = cursor.fetchall()
    cursor.close()
    return render_template("playlists.html", playlists=playlists)


@bp.route("/playlists/<int:id>/")
def playlist(id):
    if not session.get('user'):
        return redirect('/')
    cursor = mysql.connection.cursor()
    cursor.execute(f"SELECT * FROM playlist WHERE playlist.id ={id}")
    playlist = cursor.fetchone()
    cursor.execute(f"SELECT song.title, song.song, playlist_entry.id as entry, author.name FROM playlist_entry JOIN song ON playlist_entry.song_id = song.id JOIN author ON author.id = song.author_id WHERE playlist_entry.playlist_id = {id}")
    songs = cursor.fetchall()
    cursor.close()
    if playlist:
        return render_template("playlist.html", playlist=playlist, songs=songs)
    return abort(404)


@bp.route("/playlists/add/", methods=['GET', 'POST'])
def add_playlist():
    if not session.get('user'):
        return redirect('/')
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        today = datetime.date.today().strftime("%Y-%m-%d")
        cursor = mysql.connection.cursor()
        cursor.execute(f"INSERT INTO playlist VALUES (NULL, '{title}', '{today}', '{description}', {session.get('user')})")
        mysql.connection.commit()
        cursor.close()
        return redirect("/playlists/")
    return render_template("playlist_form.html")


@bp.route("/playlists/delete/<int:id>/")
def delete_playlist(id):
    if not session.get('user'):
        return redirect('/')
    cursor = mysql.connection.cursor()
    cursor.execute(f"DELETE FROM playlist WHERE id = {id}")
    mysql.connection.commit()
    cursor.close()
    return redirect("/playlists/")


@bp.route("/playlists/song/add/<int:song_id>/", methods=['GET', 'POST'])
def add_to_playlist(song_id):
    if not session.get('user'):
        return redirect('/')
    if request.method == 'POST':
        playlist_id = request.form['playlist']
        cursor = mysql.connection.cursor()
        cursor.execute(f"INSERT INTO playlist_entry VALUES (NULL, {song_id}, {playlist_id})")
        mysql.connection.commit()
        cursor.close()
        return redirect(f"/playlists/{playlist_id}/")
    return redirect("/playlists/")


@bp.route("/playlists/song/remove/<int:id>/", methods=['GET', 'POST'])
def remove_from_playlist(id):
    if not session.get('user'):
        return redirect("/")
    cursor = mysql.connection.cursor()
    cursor.execute(f"DELETE FROM playlist_entry WHERE id={id}")
    mysql.connection.commit()
    cursor.close()
    return redirect(request.referrer)