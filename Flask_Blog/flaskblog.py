from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '59ced78434ad9766bd66ecdfb966f992'

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

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Log In', form=form)

if __name__ == '__main__':
    app.run(debug=True)

