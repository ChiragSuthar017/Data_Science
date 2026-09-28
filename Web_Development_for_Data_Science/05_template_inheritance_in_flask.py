from flask import Flask
from flask import flash, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/")
def home_page():
    flash("Thanks you")
    return render_template("05_home_page.html")

@app.route("/about")
def about_page():
    flash("Thanks You for Visiting")
    return render_template("05_about_page.html")

app.run(debug=True)