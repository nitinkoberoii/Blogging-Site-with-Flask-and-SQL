from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '59ced78434ad9766bd66ecdfb966f992'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  #/// => specifies a relative path for the current file
# represent database structure as classes(models)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    # one-to-many relationship
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

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
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
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

if __name__ == '__main__':
    app.run(debug=True)

