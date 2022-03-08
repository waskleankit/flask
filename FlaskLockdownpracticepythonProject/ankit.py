# from flask import Flask
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():
#     return "Hello world"
#
# if __name__=='__main__':
#     app.run(debug = True)
#
#
#
#
# from flask import Flask
# app = Flask(__name__)
# @app.route('/hello/<name>')
# def hello_name(name):
#     return 'Hello %s!' %name
# if __name__== '__main__':
#     app.run(debug=True)
#
#
#
#
#
# from flask import Flask
# app=Flask(__name__)
# @app.route('/blog/<int:postID>')
# def show_blog(postID):
#     return 'Blog Number %d ' %postID
#
#
# @app.route('/rev/<float:revNo>')
# def revision(revNo):
#     return 'Revision Number %f' %revNo
# if __name__=='__main__':
#     app.run()




# from flask import Flask
# app=Flask(__name__)
# @app.route('/flask')
# def hello_flask():
#     return 'Hello flask'
#
# @app.route('/python/')
# def hello_python():
#     return 'hello python'
#
#
# if __name__ == '__main__':
#     app.run()
# from flask import Flask,redirect,url_for
# app=Flask(__name__)
# @app.route('/admin')
# def hello_admin():
#     return 'Hello Admin'
#
# @app.route('/guest/<guest>')
# def hello_guest(guest):
#     return 'hello %s as guest' %guest
#
# @app.route('/user/name')
# def hello_user(name):
#     if name == 'admin':
#         return redirect(url_for('hello_admin'))
#     else:
#         return redirect(url_for('hello_guest',guest=name))
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
#






from flask import  Flask,redirect,url_for,request
app=Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' %name

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name=user))

if __name__=='__main__':
    app.run(debug=True)