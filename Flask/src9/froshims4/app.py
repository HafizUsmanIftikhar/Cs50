# Implements a registration form, storing registrants in a SQLite database, with support for deregistration
import pymysql 
pymysql.install_as_MySQLdb()
from flask import Flask, redirect, render_template, request
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

# db = SQL("sqlite:///froshims.db")
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'froshims'
 
db = MySQL(app)
# db1 = db.connection.cursor()
SPORTS = [
    "Basketball",
    "Soccer",
    "Ultimate Frisbee"
]


@app.route("/")
def index():
    return render_template("index.html", sports=SPORTS)


@app.route("/deregister", methods=["POST"])
def deregister():

    # Forget registrant
    id = request.form.get("id")
    if id:
        cursor=db.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute("DELETE FROM registrants WHERE id = %s" , id)
        db.connection.commit()
    return redirect("/registrants")


@app.route("/register", methods=["POST"])
def register():

    # Validate submission
    name = request.form.get("name")
    sport = request.form.get("sport")
    if not name or sport not in SPORTS:
        return render_template("failure.html")

    # Remember registrant
    cursor = db.connection.cursor()
    cursor.execute("INSERT INTO registrants (name, sport) VALUES(%s,%s)",(name, sport))
    db.connection.commit()
    # Confirm registration
    return redirect("/registrants")

@app.route("/registrants",methods=['GET','POST'])
def registrants():
    # cursor = db.connection.cursor()
    cursor=db.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM registrants")
    registrant =cursor.fetchall()
    return render_template("registrants.html", registrants=registrant)

app.run(host='localhost', port=5000)