from flask import Flask , render_template , request

app = Flask(__name__)

@app.route("/")
def home():
    name = "chirag"
    language = "python"
    luckyno = [1, 17, 24, 76, 69]
    footer = "<p> Copyright 2025 | All right reserved</p>"
    return render_template("04_jinja2.html" , name=name, lang=language, lucky = luckyno, footer= footer)

app.run(debug=True)