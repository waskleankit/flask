from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():                                
                return render_template("index10.html")

@app.route("/hello", methods=["GET", "POST"])
def hello():
                if request.method == "GET":
                                return "Please submit the form insted."
                else:
                                name = request.form.get("name")
                                return render_template("hello10.html", name=name)
                                
                
