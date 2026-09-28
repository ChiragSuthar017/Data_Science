from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def predict():
    name = request.args.get("name", default="unnamed")
    lang = request.args.get("lang", default="unknown")
    print(name , lang)
    return render_template('06_query_parameters.html', name=name, lang=lang,)
app.run(debug=True)