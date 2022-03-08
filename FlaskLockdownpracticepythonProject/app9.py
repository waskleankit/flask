from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
                return render_template("ind1.html")

@app.route("/mor")
def more():
                return render_template("mor.html")
