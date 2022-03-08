#    # userid = Users.query.filter_by(name=name).first()
    # searchuser = "%{}%".format(userid)
    # Count number of records with a `first_name` value
    # countblogs = Posts.query.filter_by(user_id = userid).all()

# # from flask_migrate import Migrate,migrate
# # import os
# from models import *
# import os
# from datetime import datetime
# from flask import Flask,render_template,request,session,redirect,url_for
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import scoped_session,sessionmaker
# app = Flask(__name__,template_folder='venv/templates')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("postgresql+psycopg2://myuser:1234@localhost:5432/pyengine")
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345@localhost/mysqldatabase'
# db = SQLAlchemy(app)
# @app.route("/", methods=['POST','GET'])
# def index():
#     # posts = db.execute("SELECT * FROM flights").fetchall()
#     # flights = db.execute("SELECT * FROM flights").fetchall()
#     # print(posts)
#     flights = Flight.query.all()
#     return render_template("test.html", flight=flights)
# if __name__ == '__main__':
#     app.run(debug=True)

# class Posts(db.Model):
#     name = db.Column(db.String(200),primary_key=True)
#     description = db.Column(db.String(500),unique= False , nullable=False)
#     date_created = db.Column(db.DateTime,unique= False, default=datetime.utcnow)
#
# @app.route("/", methods=['POST','GET'])
# def home():
#     if (request.method=='POST'):
#         name =request.form.get('name')
#         description=request.form.get('description')
#         date_created=request.form.get('date_created')
#         entry = blogdetails(name=name,description=description,date_created=datetime.now())
#         db.session.add(entry)
#         db.session.commit()
#     #email = dict(session).get('email',None)
    # print(f'hello {email}!')
    # posts = db.execute("SELECT * FROM posts").fetchall()
    # return render_template('/test.html',post=posts)
# if __name__ == '__main__':
#     app.run(debug=True)

# initialising flask app
# app = Flask(__name__,template_folder='venv/templates')
# engine = create_engine("mysql://root:12345@localhost:3306/mysql")
# db = scoped_session(sessionmaker(bind=engine))
# db.execute("SELECT * FROM posts").fetchall()
# @app.route("/")
# def index():
#     posts = db.execute("SELECT * FROM posts").fetchall()
#     # print(flights)
#     return render_template("index.html", flights=posts)
# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=1234, debug=True)


# posts = db.execute("SELECT * FROM flights").fetchall()
# print(posts)

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
#database conectivity
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql+psycopg2://myuser:1234@localhost:5432/pyengine"
# db = SQLAlchemy(app)

# migrate = Migrate(app,db)


#
# posts.query.all()
#     return render_template("index.html",solutions = Solutions)
#
# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="12345",
#   database="mysqldatabase"
# )

# mycursor = mydb.cursor()
#
# mycursor.execute("SELECT * FROM posts")

# CREATE USER 'mysqluser' IDENTIFIED BY 'anAN123#$';
# from flask import Flask, render_template, request
# from flask_mysqldb import MySQL
# app = Flask(__name__)
#
#
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = '12345'
# app.config['MYSQL_DB'] = 'mysqldatabase'
#
# db = MySQL(app)
#
#
# @app.route('/', methods=['GET', 'POST'])
# def index():
#   posts = cur.execute("SELECT * FROM posts")
#   cur.close()
#   return posts
#   return render_template('index.html')
#
#
# if __name__ == '__main__':
#     app.run()
