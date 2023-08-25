# Import necessary modules and functions from Flask and the application
from flask import render_template, request, redirect, url_for
from app.name_tk import is_username_taken
from app.valid_pw import is_valid_password
from app import app, auth
import bcrypt
from datetime import datetime, timedelta

# Define global constants
MAX_LOGIN_ATTEMPTS = 3
LOCKOUT_DURATION = 60  # In seconds

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

# Define a function to lock an account
def lock_account(user):
    user.login_attempts = MAX_LOGIN_ATTEMPTS + 1  # Lock the account
    locked_until = datetime.now() + timedelta(seconds=LOCKOUT_DURATION)  # Set the lockout time
    
    # Update the 'locked_until' column in the database with the timestamp value
    auth.cursor.execute('UPDATE users SET locked_until = ? WHERE username = ?', (locked_until, user.username))
    auth.conn.commit()
    
    return "Account locked due to too many unsuccessful attempts. Please try again later."

# Define a function to check if an account is locked
def is_account_locked(user):
    if user.login_attempts > MAX_LOGIN_ATTEMPTS and user.locked_until > datetime.now():
        return True
    
    # Also check the 'locked_until' column in the database
    auth.cursor.execute('SELECT locked_until FROM users WHERE username = ?', (user.username,))
    result = auth.cursor.fetchone()
    if result is not None and result[0] is not None and result[0] > datetime.now():
        return True
    
    return False

# Define the login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = auth.get_user(username)

        if user:
            login_attempts = user.login_attempts
            
            # Check if the account is locked
            if is_account_locked(user):
                return "Account locked due to too many unsuccessful attempts. Please try again later."

            # Check the password
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                # Reset the login attempts counter after a successful login
                user.login_attempts = 0

                # Update the value in the database
                auth.cursor.execute('UPDATE users SET login_attempts = 0 WHERE username = ?', (username,))
                auth.conn.commit()

                return "Login successful!"
            else:
                # Increment the unsuccessful login attempts counter
                login_attempts += 1

                # Update the value in the database
                auth.cursor.execute('UPDATE users SET login_attempts = ? WHERE username = ?', (login_attempts, username))
                auth.conn.commit()

                # Check if the user has reached the maximum login attempts limit
                if login_attempts >= MAX_LOGIN_ATTEMPTS:
                    lock_account(user)
                    return "Account locked due to too many unsuccessful attempts. Please try again later."

                return "Incorrect username or password."
        else:
            return "Incorrect username or password."

    return render_template('login.html')
