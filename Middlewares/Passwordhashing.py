from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

def encrypt(password):
    """Hashes the password using Werkzeug's generate_password_hash."""
    return generate_password_hash(password)

def decrypt(hashed_password, input_password):
    """Checks if the input password matches the hashed password."""
    return check_password_hash(hashed_password, input_password)
