from flask import Flask, render_template, request
from models import generate_password

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    """Generates Random Password"""
    """ADD COMMENTS TO CODE"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        length = request.form.get("length")
        if not length:
            # TO DO
            return
        else:
            length = int(length)
        
        if request.form.get("digits_required"):
            digits = request.form.get("digits")
            if not digits:
                # TO DO
                return
            else:
                digits = int(digits)
        else:
            digits = 0

        if request.form.get("symbols_required"):
            symbols = request.form.get("symbols")
            if not symbols:
                # TO DO
                return
            else:
                symbols = int(symbols)
        else:
            symbols = 0
        
        uppercase = 2
        lowercase = 2

        min_length = digits + symbols + uppercase + lowercase

        if length < min_length:
            length = min_length

        password = generate_password(length, uppercase, lowercase, digits, symbols)
        return render_template("index.html", password=password)
    else:
        return render_template("index.html", password="")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)