import os
from flask import (
    Flask,  render_template, flash, request)
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


# About page
@app.route('/')
def about():
    """
    Renders the homepage
    """
    return render_template("pages/about.html")


# Contact Us page
@app.route("/contact", methods=["GET", "POST"])
def contact():
    """
    Renders Contact Us page,
    allows the logged in user to submit the message
    """
    if request.method == "POST":
        flash(
            "Thanks {}, we have received your message! We'll be in touch with you shortly!".format(
                request.form["name"]))
    return render_template("pages/contact_us.html")


if __name__ == '__main__':
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=os.environ.get("DEBUG"))
