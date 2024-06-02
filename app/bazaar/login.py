from flask import render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
from app.bazaar import bp
from app import mysql

@bp.route("/login/", methods=['GET', 'POST'])
def login():
    error = False
    if session.get("user"):
        return redirect("/")
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute(f"SELECT * FROM user WHERE username='{username}'")
        user = cursor.fetchone()
        cursor.close()
        if user and check_password_hash(user.get('password'), password):
            session['user'] = user.get('id')
            session['user_type'] = user.get('user_type')
            return redirect("/")
        error = True
    return render_template("login.html", error=error)


@bp.route("/signup/", methods=['GET', 'POST'])
def register():
    error = False
    if session.get("user"):
        return redirect("/")
    if request.method == 'POST':
        first = request.form['first']
        last = request.form['last']
        username = request.form['username']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        hash = generate_password_hash(password)
        try:
            cursor = mysql.connection.cursor()
            cursor.execute(f"INSERT INTO user VALUES (NULL, '{first}','{last}','{username}','{hash}','{email}','{phone}',1)")
            mysql.connection.commit()
            cursor.close()
            return redirect("/login/")
        except:
            error = True
    return render_template("register.html", error=error)


@bp.route("/logout/")
def logout():
    session.pop('user', None)
    session.pop('user_type', None)
    return redirect('/login/')