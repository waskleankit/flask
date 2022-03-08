import os

from flask import Flask, render_template, request
from  sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__, static_url_path='/static')

engine = create_engine("postgresql://postgres:@nkit2073@localhost:5432/postgres")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/",methods=['GET','POST'])
def index():
          return render_template("Home.html")

@app.route("/aboutus")
def aboutus():
          return render_template("aboutus.html")

@app.route("/contact")
def contact():
          return render_template("contact.html")

@app.route("/services")
def services():
          return render_template("services.html")


if __name__ == "__main__":
                app.run()
