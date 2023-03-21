from flask import Flask, render_template, request
from models import generate_password, apology

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    """Generates Random Password"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        length = request.form.get("length")
        # Ensure length was entered
        if not length:
            return apology("Please input a length")
        
        # Check whether digits checkbox was checked
        if request.form.get("digits_required"):
            digits = request.form.get("digits")
            # Ensure min. no. of digits was entered
            if not digits:
                return apology("Please input the minimum number of digits you would like the password to contain")
            elif digits == "0":
                digits = "1"
        else:
            digits = "0"

        # Check whether symbols checkbox was checked
        if request.form.get("symbols_required"):
            symbols = request.form.get("symbols")
            # Ensure min. no. of symbols was entered
            if not symbols:
                return apology("Please input the minimum number of special characters you would like the password to contain")
            elif symbols == "0":
                symbols = "1"
        else:
            symbols = "0"

        length = int(length)
        digits = int(digits)
        symbols = int(symbols)
        
        # Define the minimum number of uppercase and lowercase letters required
        uppercase = 2
        lowercase = 2

        # Calculate the minimum possible length
        min_length = digits + symbols + uppercase + lowercase
        
        # Ensure the length entered is at least the minimum possible length,
        # and if it isn't, then make it the minimum possible length
        if length < min_length:
            length = min_length

        password = generate_password(length, uppercase, lowercase, digits, symbols)
        return render_template("index.html", password=password)
    
    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("index.html", password="")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)