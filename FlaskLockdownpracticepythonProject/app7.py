from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
          names = ["alice","bob","charlie"]
          return render_template("index3.html", names=names)
