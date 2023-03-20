from flask import Flask
from models import generate_password

app = Flask(__name__)

@app.route("/")
def index():
    return generate_password()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)