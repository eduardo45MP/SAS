# Import necessary modules and functions from Flask and the application
from flask import render_template, request, redirect, url_for
from app.name_tk import is_username_taken
from app.valid_pw import is_valid_password
from app import app, auth
import bcrypt
from app import app
from app.auth import create_user, get_user, check_login_attempts
from datetime import datetime, timedelta

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

def lock_account(user):
    LOCKOUT_DURATION = 60
    MAX_LOGIN_ATTEMPTS = 3
    user.login_attempts = MAX_LOGIN_ATTEMPTS + 1  # Bloqueie a conta
    locked_until = datetime.now() + timedelta(seconds=LOCKOUT_DURATION)  # Configure o tempo de bloqueio
    
    # Atualize a coluna locked_until no banco de dados com o valor de timestamp
    auth.cursor.execute('UPDATE users SET locked_until = ? WHERE username = ?', (locked_until, user.username))
    auth.conn.commit()
    
    return "Conta bloqueada devido a muitas tentativas malsucedidas. Tente novamente mais tarde."

# Define a função para verificar se a conta está bloqueada
def is_account_locked(user):
    if user.login_attempts > MAX_LOGIN_ATTEMPTS and user.locked_until > int(time.time()):
        return True
    
    # Verifique também a coluna locked_until no banco de dados
    auth.cursor.execute('SELECT locked_until FROM users WHERE username = ?', (user.username,))
    result = auth.cursor.fetchone()
    if result and result[0] > int(time.time()):
        return True
    
    return False

# Define a rota de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = auth.get_user(username)

        if user:
            MAX_LOGIN_ATTEMPTS = 3
            login_attempts = user.login_attempts
            
            # Verifique se a conta está bloqueada
            if login_attempts >= MAX_LOGIN_ATTEMPTS:
                return "Conta bloqueada devido a muitas tentativas malsucedidas. Tente novamente mais tarde."

            # Verifique a senha
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                # Redefina o contador de tentativas de login após um login bem-sucedido
                user.login_attempts = 0

                # Atualize o valor no banco de dados
                auth.cursor.execute('UPDATE users SET login_attempts = 0 WHERE username = ?', (username,))
                auth.conn.commit()

                return "Login bem-sucedido!"
            else:
                # Incremente o contador de tentativas de login malsucedidas
                login_attempts += 1
                # Atualize o valor no banco de dados
                auth.cursor.execute('UPDATE users SET login_attempts = ? WHERE username = ?', (login_attempts, username))
                auth.conn.commit()

                # Verifique se o usuário atingiu o limite máximo de tentativas
                if login_attempts >= MAX_LOGIN_ATTEMPTS:
                    lock_account(user)
                    return "Conta bloqueada devido a muitas tentativas malsucedidas. Tente novamente mais tarde."

                return "Senha incorreta. Tentativas restantes: {}".format(MAX_LOGIN_ATTEMPTS - login_attempts)
        else:
            return "Usuário não encontrado."

    return render_template('login.html')
