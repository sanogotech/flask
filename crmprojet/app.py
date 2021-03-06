import os
from flask import Flask, flash, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import configparser

app = Flask(__name__)
## Get Application  Settings
config = configparser.ConfigParser()
config.read('config.ini')
urldbconfigvalue = config['DEFAULT']['SQLALCHEMY_DATABASE_URI']
print("-----* DataBase Url is : ", urldbconfigvalue)
# If you do that, your browser will not cache static assets that are served by Flask .No Cache Browser
sendfilemaxageconfigvalue = config['DEFAULT']['SEND_FILE_MAX_AGE_DEFAULT']
#The secret key is needed to keep the client-side sessions secure. You can generate some random
secretkeyconfigvalue = config['DEFAULT']['SECRET_KEY']

app.config['SQLALCHEMY_DATABASE_URI'] = urldbconfigvalue
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = int(sendfilemaxageconfigvalue)
app.config['SECRET_KEY'] = secretkeyconfigvalue

db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(20), nullable=False, default='N/A')
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return 'Blog post ' + str(self.id)


@app.route('/')
def displayloginpage():
    return render_template('login.html')
    
@app.route('/authlogin', methods=['POST'])
def authlogin():

    username = request.form['username']
    password = request.form['password']
    if (username == "admin") and (password == "admin"):
        flash('You were successfully logged in')
        return render_template('index.html')
    else :
        flash('Login Failed !')
        #return render_template('login.html')
        return redirect('/')
   
    
    
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/posts', methods=['GET', 'POST'])
def posts():

    if request.method == 'POST':
        post_title = request.form['title']
        post_content = request.form['content']
        post_author = request.form['author']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        all_posts = BlogPost.query.order_by(BlogPost.date_posted).all()
        return render_template('posts.html', posts=all_posts)

@app.route('/posts/delete/<int:id>')
def delete(id):
    post = BlogPost.query.get_or_404(id)
    db.session.delete(post)
    db.session.commit()
    return redirect('/posts')

@app.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    
    post = BlogPost.query.get_or_404(id)

    if request.method == 'POST':
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('edit.html', post=post)

@app.route('/posts/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        post.title = request.form['title']
        post.author = request.form['author']
        post.content = request.form['content']
        new_post = BlogPost(title=post_title, content=post_content, author=post_author)
        db.session.add(new_post)
        db.session.commit()
        return redirect('/posts')
    else:
        return render_template('new_post.html')

if __name__ == "__main__":
    
    db.create_all()
    app.run()
    #app.run(debug=True,host='0.0.0.0', port=8080)
    # If you are talking about test/dev environments, then just use the debug option.
    # It will auto-reload the flask app when a code change happens.