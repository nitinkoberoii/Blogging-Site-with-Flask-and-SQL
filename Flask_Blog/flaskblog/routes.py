from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': 'Nitin Kumar',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'April 2, 2024'
    },
    {
        'author': 'Tejas Pakhale',
        'title': 'Blog Post 2',
        'content': 'Second Post Content',
        'date_posted': 'April 3, 2024'
    }
]

# app.route decorator handle all the backend complexity and return the information that we wish
# to be shown on our website '/'->root/home page
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your Account has been Created!!, You are now able to LogIn', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful, please check username or password', 'danger')    #danger => alert or failure in BS classes
    return render_template('login.html', title='Log In', form=form)
