from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>hello world</p>"

@app.route("/next")
def next_page():
    return "<p> next page</p>"
app.run(debug=True)