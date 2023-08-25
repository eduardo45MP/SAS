import re  # Import the regular expressions module

def is_valid_password(password):
    # Define your password criteria here
    min_length = 8  # Defines the minimum length of the password
    # Uses a regular expression to check if the password contains at least one of the special characters
    has_special_char = re.search(r'[!@#$%^&*(),.?-_":{}|<>]', password)
    # Checks if the password has at least one uppercase letter
    has_uppercase = any(c.isupper() for c in password)
    # Checks if the password has at least one numeric digit
    has_number = any(c.isdigit() for c in password)
    
    # Returns True if all criteria are met, otherwise returns False
    return (
        len(password) >= min_length and
        has_special_char and
        has_uppercase and
        has_number
    )
