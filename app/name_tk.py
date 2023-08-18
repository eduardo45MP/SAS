# Import the 'mariadb' module
import mariadb

# Import the 'sys' module
import sys

# Define a function to check if a username is already taken
def is_username_taken(username):
    try:
        # Establish a connection to the MariaDB database
        conn = mariadb.connect(
            user='SAS',
            password='USER@SAS2000',
            host='localhost',
            database='SAS'
        )
    except mariadb.Error as e:
        # Print an error message if there's a problem with the database connection
        print(f'Error communicating to MariaDB: {e}')
        sys.exit(1)

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Execute a SELECT query to check if the username already exists in the 'users' table
    cursor.execute('SELECT id FROM users WHERE username = ?', (username,))
    existing_user = cursor.fetchone()

    # Close the database connection
    conn.close()

    # Return True if the username already exists, otherwise return False
    return existing_user is not None

