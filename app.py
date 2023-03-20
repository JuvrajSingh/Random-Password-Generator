from flask import Flask, render_template, request
from models import generate_password

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    """Generates Random Password"""
    if request.method == "POST":
        password = generate_password()
        return render_template("index.html", password=password)
    else:
        return render_template("index.html", password="")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)