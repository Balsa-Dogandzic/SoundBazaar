from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'music'

app.secret_key = "8jLv75e6oOrWxNwbG8RTDA"

db = MySQL(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/authors")
def authors():
    cursor = db.connection.cursor()
    cursor.execute("SELECT * FROM author")
    authors = cursor.fetchall()
    cursor.close()
    return render_template("authors.html", authors=authors)

if __name__ == "__main__":
    app.run(debug=True)