from flask import Flask, render_template, redirect, url_for, request, session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'secret'

@app.route("/")
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/set_language', methods=['POST'])
def set_language():
    session['language'] = request.form['language']
    return redirect(request.referrer or '/')


# route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        # handle login form submission
        username = request.form['username']
        password = request.form['password']
        # check if the credentials are valid
        # (replace this with your own authentication logic)
        if username == 'admin' and password == 'password':
            return redirect(url_for('home'))
        else:
            error = 'Invalid username or password'
    return render_template('login.html', error=error)

# route for the sign-up page
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        # handle sign-up form submission
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        # check if the username is already taken
        # (replace this with your own database query)
        if username == 'admin':
            error = 'That username is already taken'
        # check if the passwords match
        redirect(url_for('home'))
    
    # handle GET request by rendering the sign-up form
    return render_template('signup.html')

    

@app.route('/register', methods=['POST'])
def register():
    # handle form data here
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    # save user data to database or perform other actions
    # return a response
    return f'Thank you for signing up, {username}!'

@app.route('/flags', methods=['GET', 'POST'])
def flags():
    if request.method == 'POST':
        flag = request.form['flag']
        # Do something with the selected flag value (e.g. save it to a database)
        return render_template('flag_result.html', flag=flag)
    else:
        return render_template('flags.html')
    
    
    
@app.route('/handle_flag', methods=['POST'])
def handle_flag():
    selected_flag = request.form.get('flag')
    # Do something with the selected flag...
    return 'You selected the flag: ' + selected_flag

if __name__ =="__main__":
    app.run(host='0.0.0.0',debug=True)