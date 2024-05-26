from flask import Flask, render_template
from flask_mysqldb import MySQL
from login import login_bp
from songs import songs_bp

app = Flask(__name__, static_url_path="/static")

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'music'

app.secret_key = "8jLv75e6oOrWxNwbG8RTDA"

db = MySQL(app)

app.register_blueprint(login_bp)
app.register_blueprint(songs_bp)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)