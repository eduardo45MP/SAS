import mariadb  # Import the mariadb module to work with MariaDB database
import sys  # Import the sys module for system-related functionality
import bcrypt  # Import the bcrypt module for password hashing

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

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
        password VARCHAR(255) NOT NULL
    )
''')
conn.commit()

def get_user(username):
    cursor.execute('SELECT * FROM users WHERE username = ?', (username, ))
    user_data = cursor.fetchone()
    if user_data:
        user = User(user_data[1], user_data[2])
        return user
        
def create_user(username, password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())  # Hash the password
    cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
    conn.commit()
