import bcrypt
def encrypt(password):
    """Hashes the password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)
    return hashed_password

def decrypt(hashed_password, input_password):
    try:
        if isinstance(hashed_password, str):
            hashed_password = hashed_password.encode() 
        return bcrypt.checkpw(input_password.encode(), hashed_password)
    except Exception as e:
        print(f"Error during password verification: {e}")
        return False
