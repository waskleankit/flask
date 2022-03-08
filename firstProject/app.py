from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate,migrate




app = Flask(__name__,template_folder='venv/templates')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

db = SQLAlchemy(app)
migrate = Migrate(app,db)
class todo(db.Model):
    name = db.Column(db.String(200),primary_key=True)
    description = db.Column(db.String(500),unique= False , nullable=False)
    date_created = db.Column(db.DateTime,unique= False, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.name} - {self.description} - {self.date_created}"

@app.route("/", methods=['POST','GET'])
def home():
    if request.method=='POST':
        identity = request.form['loginid']
        pd = request.form['pd']
        if (identity == "ankit" and pd == "12345"):
            return render_template('admin.html')
    return render_template('firsthtml.html')


@app.route('/admin.html',methods = ["GET","POST"])
def adminfun():
    if request.method=='POST':
        topic = request.form['name']
        description= request.form['description']
        row = todo(name=topic,description=description)
        db.session.add(row)
        db.session.commit()
    alltodo = todo.query.all()
    print(alltodo)
    return render_template('admin.html',alltodo=alltodo)

@app.route("</string:name>")
def hello(name):
    return f"hello,{name}!"

if __name__ == '__main__':
        app.run( debug = True )



@app.route('/todo',methods = ["GET","POST"])
def admintodo():
    return render_template('todo.html')


# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="12345",
# )
# mycursor = mydb.cursor()
#
# mycursor.execute("SHOW TABLES")
#
# for x in mycursor:
#   print(x)

# @app.route("/show")
# def adminfu():
#     alltodo = todo.query.all()
#     print(alltodo)
#     return "this is produce page"
