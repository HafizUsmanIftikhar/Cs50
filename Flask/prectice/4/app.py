from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/greet", methods=["POST"])
def greet():
    if not request.form.get("name") or request.form.get("sport") not in ["cricket","football"]:
        return render_template("failure.html")

    return render_template("success.html")