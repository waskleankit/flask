from flask import Flask,render_template,request,session,redirect,url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate,migrate

import paypal
from models import  *
from paypal import  *
from googlelogin import *
from sqlalchemy import or_
import paypalrestsdk
# initialising flask app
app = Flask(__name__,template_folder='venv/templates')
# this is for  google login
app.secret_key='random secret'


#database conectivity
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://mydbuser:ankitwaskle@localhost:5432/mydbuser"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
app.debug = True



# paypal config

paypalrestsdk.configure({
  "mode": "sandbox", # sandbox or live
  "client_id": "AQXrXt15Z-ZX5gEaN1FyfrcVqXHiJy1YO9ZfU5wkzPLVeZNiltQQAJfFmga3qPKNgzBRTwA7r7b0UNTc",
  "client_secret": "EHDVp-F8zYNd9L4CPMSpEFUG21k0es0RrfL7DNwMtl98iHsBeNapyYhZX0M2_qTDF1MJ2x7tRgkl1xyS" })

# gmail login
@app.route('/login')
def login():
    google = oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)
@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
#   resp.raise_for_status()
    user_info = resp.json()
    # do something with the token and profile
    session['email'] = user_info['email']
    session['name'] = user_info['name']
    return redirect('/')
@app.route('/logout')
def logout():
    for key in list (session.keys()):
        session.pop(key)
    return redirect('/')





db = SQLAlchemy(app)
# migrate = Migrate(app,db)




@app.route("/", methods=['POST','GET'])
def home():
    # Set the pagination configuration
    ROWS_PER_PAGE = 5
    page = request.args.get('page', 1, type=int)
    email = dict(session).get('email',None)
    name = dict(session).get('name',None)
    tag = request.form.get('sv')
    # searchcat = request.args.get("s_cat")
    if searchcat != None:
        posts = Posts.query.filter_by(category_id = searchcat).paginate(page=page, per_page=ROWS_PER_PAGE)

    elif tag != None:
        search = "%{}%".format(tag)
        posts = Posts.query.filter(or_(Posts.description.like(search),Posts.title.like(search))).paginate(page=page, per_page=ROWS_PER_PAGE)
    else:
        posts = Posts.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    cate = Category.query.all()
    username = Users.query.all()
    # try:
    # except:
    #     pass
    # if b != None:
    #     print(b)
    user = Users.query.all()
    user1 = Users.query.filter_by(name=name).first()
    if user1 == None:
        userinserting = Users(name,email)
        db.session.add(userinserting)
        db.session.commit()
    # print(f'hello {email}!')
    return render_template('/index.html',email=email,posts=posts,category=cate,username=username,name=name)

@app.route("/home")
def home1():
    return redirect('/')


@app.route("/singlepost",methods = ["GET","POST"])
def singlepost():
    idvalue = request.values.get("b")
    print(idvalue)
    posts = Posts.query.filter_by(id = idvalue).first()
    username = Users.query.all()
    cate = Category.query.all()
    email = dict(session).get('email', None)
    name = dict(session).get('name', None)
    return render_template('singlepost.html',email=email,posts=posts,category=cate,username=username,name=name)

@app.route("/about")
def about():
    email = dict(session).get('email', None)
    name = dict(session).get('name', None)
    return render_template('/aboutus.html',email=email,name=name)

@app.route("/dashboard",methods = ["GET","POST"])
def dashboard():
    email1 = dict(session).get('email', None)
    name = dict(session).get('name', None)
    user = Users.query.filter_by(email = email1).first()
    userid = user.user_id
    cate = Category.query.all()
    tag = request.form.get('sv')
    searchcat = request.args.get("s_cat")
    print(searchcat)
    if searchcat != None:
        posts = Posts.query.filter_by(category_id = searchcat,user_id = userid).all()
    elif tag != None:
        search = "%{}%".format(tag)
        posts = Posts.query.filter(or_(Posts.description.like(search),Posts.title.like(search))).filter_by(user_id = userid).all()
    else:
        posts = Posts.query.filter_by(user_id = userid).all()
    return render_template('blogdashboard.html',email=email1,posts=posts,category=cate,name=name)

@app.route("/createblog")
def createblog():
    email = dict(session).get('email', None)
    name = dict(session).get('name', None)
    user = Users.query.filter_by(email = email).first()
    userid = user.user_id
    countblogs = Posts.query.filter_by(user_id=userid).count()
    if countblogs >= 5:
        pass
        return render_template('plans.html', email=email, name=name)
    else:
        cate = Category.query.all()
        return render_template('createblog.html',email=email,category=cate,name=name)

# this post_user is for creating new  post
@app.route('/post_user',methods=['POST'])
def post_user():
    title = request.form['name']
    description = request.form['desc']
    date_created = datetime.utcnow()
    category_id = request.form['category']
    email1 = dict(session).get('email', None)
    user = Users.query.filter_by(email = email1).first()
    user_id = user.user_id
    post=Posts(title,description,date_created,category_id,user_id)
    db.session.add(post)
    db.session.commit()
    cate = Category.query.all()
    user = Users.query.filter_by(email = email1).first()
    userid = user.user_id
    posts = Posts.query.filter_by(user_id = userid).all()
    name = dict(session).get('name', None)
    return render_template('blogdashboard.html',email=email1,posts=posts,category=cate,name=name)

@app.route("/edit",methods = ["GET","POST"])
def edit():
    idvalue = request.values.get("b")
    posts = Posts.query.filter_by(id = idvalue).first()
    cate = Category.query.all()
    email = dict(session).get('email', None)
    name = dict(session).get('name', None)
    return render_template('editblog.html',email=email, post=posts,category=cate,name=name)

@app.route('/update',methods=['POST'])
def update():
    title = request.form['name']
    description = request.form['desc']
    category = request.form['category']
    date_created = datetime.utcnow().strftime('%B %d %Y ')
    id = request.form['b']
    posts = db.session.query(Posts).filter_by(id = request.form['b']).update({"title": title,"description":description,"date_created":date_created,"category_id":category})
    db.session.commit()
    email1 = dict(session).get('email', None)
    name = dict(session).get('name', None)
    user = Users.query.filter_by(email=email1).first()
    userid = user.user_id
    posts = Posts.query.filter_by(user_id=userid).all()
    cate = Category.query.all()
    return render_template("blogdashboard.html",email=email1,posts=posts,category=cate,name=name)

@app.route('/deletepost',methods=['POST','GET'])
def deletepost():
    idvalue = request.form.get("a")
    posts= db.session.query(Posts).filter_by(id=idvalue).first()
    db.session.delete(posts)
    db.session.commit()
    return redirect('/dashboard')

@app.route("/selectedplan",methods = ["GET","POST"])
def selectedplan():
    idvalue = request.form.get("plan")
    posts = None
    price = None
    plan = None
    if idvalue == "1":
        posts = 20
        price = 1
        plan = "Basic"
    elif idvalue == "2":
        posts = 100
        price = 5
        plan = "Standard"
    elif idvalue == "3":
        posts = 1000
        price = 10
        plan = "Premium"
    email = dict(session).get('email', None)
    name = dict(session).get('name', None)
    return render_template('selectedplan.html',email=email,name=name,planid=idvalue,post=posts,price=price,plan=plan)

@app.route('/payment', methods=['POST'])
def payment():
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "redirect_urls": {
            "return_url": "http://localhost:3000/payment/execute",
            "cancel_url": "http://localhost:3000/"},
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "Blogposts",
                    "sku": "20",
                    "price": "1.00",
                    "currency": "USD",
                    "quantity": 1}]},
            "amount": {
                "total": "1.00",
                "currency": "USD"},
            "description": "This is the payment transaction description."}]})
    if payment.create():
        pass
        # print('Payment success!')
    else:
        print(payment.error)
    return jsonify({'paymentID' : payment.id})

@app.route('/execute', methods=['POST'])
def execute():
    email = dict(session).get('email', None)
    name = dict(session).get('name', None)
    success = False
    payment = paypalrestsdk.Payment.find(request.form['paymentID'])
    if payment.execute({'payer_id' : request.form['payerID']}):
        # print('Execute success!')
        payer_id = request.form['payerID']
        payment_id = request.form['paymentID']
        user = Users.query.filter_by(email=email).first()
        user_id = user.user_id
        json_response = payment.success()
        getresponses = payment
        print(getresponses)
        # amount = payment(id)
        # print(amount)
        success = True
        paymenttable = Paymenttable(payment_id, payer_id, email, name,user_id,json_response)
        db.session.add(paymenttable)
        db.session.commit()
    else:
        print(payment.error)
    return jsonify({'success' : success})



@app.route('/thankyou',methods = ["GET","POST"])
def thank():
    email = dict(session).get('email', None)
    name = dict(session).get('name', None)
    amount = request.args.get('amount')


    # print(amount)
    # print(user_id)
    # success = request.args.get('success')
    # print(success)
    # print(request.form['price'])
    return render_template('thankyou.html',email=email,name=name)






@app.route('/admin',methods = ["GET","POST"])
def admin():
    return render_template('adminlogin.html')

@app.route('/adminpassword',methods = ["GET","POST"])
def adminpassword():
    name = request.form.get("loginid")
    password = request.form.get("pd")
    blogadmin = db.session.query(Users).filter_by(role="admin").first()
    username=blogadmin.role
    userpassword=blogadmin.password
    if name == username and password == userpassword:
        posts = Posts.query.all()
        cate = Category.query.all()
        username = Users.query.all()
        return render_template('admindashboard.html', posts=posts, category=cate, username=username,blogadmin=blogadmin)
    else:
        return render_template('adminlogin.html', message="Enter correct userid and password")


@app.route('/adminboard', methods=["GET", "POST"])
def adminboard():
    posts = Posts.query.all()
    cate = Category.query.all()
    username = Users.query.all()
    blogadmin = db.session.query(Users).filter_by(role="admin").first()
    return render_template('admindashboard.html',posts=posts,category=cate,username=username,blogadmin=blogadmin)

@app.route('/deletebyadmin',methods=['POST','GET'])
def deletebyadmin():
    idvalue = request.form.get("a")
    posts= db.session.query(Posts).filter_by(id=idvalue).first()
    db.session.delete(posts)
    db.session.commit()
    posts = Posts.query.all()
    cate = Category.query.all()
    username = Users.query.all()
    blogadmin = db.session.query(Users).filter_by(role="admin").first()
    return render_template('admindashboard.html',posts=posts,category=cate,username=username,blogadmin=blogadmin)



@app.route("/category")
def category():
    cat=Category.query.all()
    blogadmin = db.session.query(Users).filter_by(role="admin").first()
    return render_template('/categories.html',category = cat,blogadmin=blogadmin)

@app.route('/add_category',methods=['POST'])
def add_category():
    category_name = request.form['name']
    create_date = datetime.utcnow()
    # print(create_date)
    update_date = datetime.utcnow()
    cat=Category(category_name,create_date,update_date)
    db.session.add(cat)
    db.session.commit()
    cate = Category.query.all()
    blogadmin = db.session.query(Users).filter_by(role="admin").first()
    return render_template('categories.html',category=cate,blogadmin=blogadmin)

@app.route('/deletecategory',methods=['POST','GET'])
def deletecategory():
    idvalue = request.form.get("a")
    print(idvalue)
    category= db.session.query(Category).filter_by(category_id = idvalue).first()
    db.session.delete(category)
    db.session.commit()
    return redirect('/category')

@app.route('/editcategory',methods=['POST','GET'])
def editcategory():
    update_date = datetime.utcnow()
    name=request.form['upda']
    posts = db.session.query(Category).filter_by(category_id = request.form['b']).update({"category_name": name })
    db.session.commit()
    return redirect('/category')





if __name__ == '__main__':
    app.run(debug=True)

