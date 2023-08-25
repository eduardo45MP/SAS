import mariadb  # Import the mariadb module to work with MariaDB database
import sys  # Import the sys module for system-related functionality
import bcrypt  # Import the bcrypt module for password hashing

class User:
    def __init__(self, username, password, login_attempts, locked_until):
        self.username = username
        self.password = password
        self.login_attempts = login_attempts
        self.locked_until = locked_until
# Establish a connection to the MariaDB database

try:
    conn = mariadb.connect(
        user='SAS',
        password='USER@SAS2000',
        host='localhost',
        database='SAS'
    )
except mariadb.Error as e:
    print(f'Error communicating to MariaDB: {e}')
    sys.exit(1)
cursor = conn.cursor()

# Create the 'users' table if it doesn't exist

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        login_attempts INT NOT NULL DEFAULT 0,
        locked_until TIMESTAMP NULL
    )
''')
conn.commit()

def check_login_attempts(username):
    user = get_user(username)
    if user:
        if user.login_attempts >= MAX_LOGIN_ATTEMPTS:
            return True  # A conta está bloqueada
    return False  # A conta não está bloqueada

def get_user(username):
    cursor.execute('SELECT id, username, password, login_attempts, locked_until FROM users WHERE username = ?', (username,))
    user_data = cursor.fetchone()
    if user_data:
        user = User(user_data[1], user_data[2], user_data[3], user_data[4])
        return user
        
def create_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())  # Hash the password
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
    conn.commit()
