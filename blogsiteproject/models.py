from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class Posts(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200),unique= False)
    description = db.Column(db.String(500),unique= False , nullable=False)
    date_created = db.Column(db.DateTime,unique= False, default=datetime.utcnow)
    category_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    def __init__(self,title,description,date_created,category_id,user_id):
        self.title = title
        self.description = description
        self.date_created = date_created
        self.category_id=category_id
        self.user_id=user_id

    def __repr__(self):
        return '<User %r>' % self.id


class Category(db.Model):
    category_id = db.Column(db.Integer,primary_key=True)
    category_name = db.Column(db.String(200),unique= False)
    create_date = db.Column(db.DateTime,unique= False, default=datetime.utcnow)
    update_date = db.Column(db.DateTime,unique= False, default=datetime.utcnow)
    def __init__(self,category_name,create_date,update_date):
        self.category_name = category_name
        self.create_date = create_date
        self.update_date = update_date
    def __repr__(self):
        return '<User %r>' % self.category_id


class Users(db.Model):
    user_id = db.Column(db.Integer,primary_key=True)
    role = db.Column(db.String(200),unique= False)
    name = db.Column(db.String(200),unique= False , nullable=False)
    email = db.Column(db.String(200),unique= False)
    password = db.Column(db.String(200),unique= False)

    def __init__(self,name,email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '%r' % self.user_id




class Paymenttable(db.Model):
    payment_id = db.Column(db.String,primary_key=True)
    user_id = db.Column(db.Integer,unique= False)
    payer_id = db.Column(db.String,unique= False)
    amount = db.Column(db.Integer,unique= False)
    email = db.Column(db.String, unique=False)
    name = db.Column(db.String, unique=False)
    json_response = db.Column(db.String(200), unique=False)
    def __init__(self,payment_id, payer_id, email, name,user_id,json_response):
        self.name = name
        self.email = email
        self.payment_id = payment_id
        self.payer_id = payer_id
        self.user_id = user_id
        # self.amount = amount
        self.json_response = json_response


    def __repr__(self):
        return '%r' % self.payment_id











#    user_id integer NOT NULL,
#     role character varying COLLATE pg_catalog."default" DEFAULT USER,
#     name character varying COLLATE pg_catalog."default",
#     email character varying COLLATE pg_catalog."default",
#     password character varying COLLATE pg_catalog."default",
#     CONSTRAINT "Users_pkey" PRIMARY KEY (user_id)
#     def __repr__(self):
#         return '<User %r>' % self.id