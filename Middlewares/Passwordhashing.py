import bcrypt
def encrypt(password):
    """Hashes the password using bcrypt."""
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def decrypt(hashed_password, input_password):
    """Checks the hashed password against the input password."""
    try:
        print("Inside decrypt:")
        print("Hashed password (bytes):", hashed_password)
        print("Input password (bytes):", input_password)
        if bcrypt.checkpw(input_password, hashed_password):
            print("Password matches!")
            return True
        else:
            print("Password does not match")
    except Exception as e:
        
        print(f"Error during password verification: {e}")
        return False

# plain_text_password = "password"
# hashed_password = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
# print("Generated Hash:", hashed_password)

# # Step 2: Verify the password against the hash
# if bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_password):
#     print("Password matches!")
# else:
#     print("Password does NOT match!")