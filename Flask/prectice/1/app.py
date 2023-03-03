from flask import Flask, render_template, request
app = Flask(__name__)

# SPORTS = [
#     "Basketball",
#     "Soccer",
#     "Ultimate Frisbee"
# ]

@app.route("/")
def index():
    name=request.args.get("name")
    return render_template("index.html", name=name)


# @app.route("/register", methods=["POST"])
# def register():

#     # Validate submission
#     if not request.form.get("name") or request.form.get("sport") not in SPORTS:
#         return render_template("failure.html")

#     # Confirm registration
#     return render_template("success.html")
