from flask import Flask , render_template

app = Flask(__name__)
# app = Flask(__name__, 
#             static_folder='asset',       # change the static folder static to asset by default static folder use
#             static_url_path='/files')    # chnage the url path used to serve those satic file it can not change file name and by default url is /static
@app.route("/")
def hello_world():
    return "<p>hello world</p>"

@app.route("/next")
def next_page():
    return "<p> next page</p>"

@app.route("/about")
def about():
    return render_template("indexx.html")

@app.route("/url")
def url():
    return render_template("url.html")

app.run(debug=True)