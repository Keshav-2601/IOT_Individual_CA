from werkzeug.security import generate_password_hash

def encrypt(password):
    """Hashes the password using Werkzeug's generate_password_hash."""
    return generate_password_hash(password)
