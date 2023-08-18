# Import necessary modules and functions from Flask and the application
from flask import render_template, request, redirect, url_for
from app.name_tk import is_username_taken
from app.valid_pw import is_valid_password
from app import app, auth
import bcrypt

# Define a route for the root URL
@app.route('/')
def index():
    return render_template('index.html')

# Define a route for the '/signup' URL, with support for both GET and POST methods
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if the username is already taken
        
        if not is_username_taken(username):
            # Check if the password is valid using the 'is_valid_password' function
            if is_valid_password(password):
                # Create a new user using the 'create_user' function from the 'auth' module
                auth.create_user(username, password)
                # Redirect to the login page after successful registration
                return redirect(url_for('login'))
            else:
                return 'Invalid password. Your password must meet the specified criteria.'
        else:
            return "Username already exists."
    return render_template('signup.html')

# Define a route for the '/login' URL, with support for both GET and POST methods
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = auth.get_user(username)
        
        if user and bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):  # Password hash verification
            return "Login successful!"
        else:
            return "Invalid credentials. Please try again."
            
    return render_template('login.html')
