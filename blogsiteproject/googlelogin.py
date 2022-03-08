# google login logout dont touch it
#oauth config
from app import *
from authlib.integrations.flask_client import OAuth
oauth = OAuth(app)
google = oauth.register(
    name='google',
    client_id='315021934177-q3vgt29o4qmo1qcp09duip5g9mau0jjg.apps.googleusercontent.com',
    client_secret='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',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_params=None,
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    authorize_params=None,
    api_base_url='https://www.googleapis.com/oauth2/v1/',
    client_kwargs={'scope': 'openid profile email'},
)



#
# @app.route("/")
# def index():
#           flights = Flight.query.all()
#           return render_template("index12.html", flights=flights)

# if __name__ == "__main__":
#     app.run()
# #
# @app.route("/book", methods=["POST"])
# def book():
#           """ Book a flight."""
#
#           #Get form information
#           name = request.form.get("name")
#           try:
#                     flight_id = int(request.form.get("flight_id"))
#           except ValueError:
#                     return render_template("error.html", message="Invalid flight number.")
#
#           #Make sure te flight exist
#           flight = Flight.query.get(flight_id)
#           if flight is None:
#                     return render_template("error.html", message="No such flights with that id.")
#
#           #Add passenger.
#           flight.add_passenger(name)
#           return render_template("success.html")
#
# @app.route("/flights")
# def flights():
#           """Lists details about  all flights"""
#           flights = Flight.query.all()
#           return render_template("flights.html", flights=flights)
#
#
# @app.route("/flights/<int:flight_id>")
# def flight(flight_id):
#
#           """lists details about a single flights."""
#
#           #make suure  flight exists.
#           flight = Flight.query.get(flight_id)
#           if flight is None:
#                     return render_template("error.html", message = "No  such flight")
#
#           #Get all passengers
#           passenger = flight.passengers
#           return render_template("flight.html", flight=flight, passenger= passenger)
#

# if __name__ == "__main__":
#     app.run(debug=True)
          # with app.app_context():
          #       main()
from flask import Flask, render_template, request,redirect,url_for
# from flask_sqlalchemy import SQLAlchemy
# # from models import *
#
# app = Flask(__name__,template_folder='venv/templates')
# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://mydbuser:ankitwaskle@localhost:5432/mydbuser"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.debug = True
# db = SQLAlchemy(app)
#
# class posts(db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     username = db.Column(db.String(80),unique=True)
#     description = db.Column(db.String(120),unique=True)
#
#     def __init__(self,username,description):
#         self.username = username
#         self.description = description
#
#     def __repr__(self):
#         return '<User %r>' % self.username
#
# @app.route('/')
# def index():
#     myUser = Posts.all()
#     oneItem = Posts.filter_by(username="test").first()
#     return render_template("add_user.html", myUser=myUser,oneItem=oneItem)
#
# @app.route('/post_user',methods=['POST'])
# def post_user():
#     user = User(request.form['username'],request.form['email'])
#     db.session.add(Posts)
#     db.session.commit()
#     return redirect(url_for('index'))
# if __name__ == "__main__":
#     app.run()
#     # if request.method=='POST':
#     #     topic = request.form['name']
#     #     description= request.form['description']
#     #     row = todo(name=topic,description=description)
#     #     db.session.add(row)
#     #     db.session.commit()
#     # alltodo = todo.query.all()
#     # print(alltodo)
#     # return render_template('adminlogin.html',alltodo=alltodo)
#
#
# # @app.route("</string:name>")
# # def hello(name):
# #     return f"hello,{name}!"
#
#
#
#
#
# # @app.route('/todo',methods = ["GET","POST"])
# # def admintodo():
# #     return render_template('todo.html')
#
#
# # return redirect(url_for('index'))
#
#
# # db = SQLAlchemy(app)
# # @app.route("/")
# # def index():
# #     Solutios = tools.query.all()
# #     print(Solutions)
# #     return render_template("index.html",solutions = solutions)
# #
# # class tools(db.Model):
# #     Solution = db.Column(db.VARCHAR, primary_key = True)
# #     TaskList = db.Column(db.VARCHAR)
# #     TaskPath = db.Column(db.VARCHAR)
# #
# # if __name__ == '__main__':
# #         app.run(host="0.0.0.0",port = 8000,debug = True)
#
#
#
#
#
#
# # import mysql.connector
# # mydb = mysql.connector.connect(
# #   host="localhost",
# #   user="root",
# #   password="12345",
# # )
# # mycursor = mydb.cursor()
# #
# # mycursor.execute("SHOW TABLES")
# #
# # for x in mycursor:
# #   print(x)
#
# # @app.route("/show")
# # def adminfu():
# #     alltodo = todo.query.all()
# #     print(alltodo)
# #     return "this is produce page"#