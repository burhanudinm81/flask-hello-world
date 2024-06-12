from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/hello")
def hello_world():
    return "<h1>Hello World</h1>"

@app.route("/about")
def about():
    return "<h1>About</h1>"