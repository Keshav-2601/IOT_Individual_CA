from flask import jsonify,redirect,request
from flask_jwt_extended import verify_jwt_in_request, get_jwt,decode_token
from cryptography.fernet import Fernet
import os
from functools import wraps
from dotenv import load_dotenv
load_dotenv()
encryption_key=os.getenv("ENCRYPTION_KEY")

print("Loaded encryption key from protectdedroute :", encryption_key)

cipher = Fernet(encryption_key)
def adminrole(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        admintoken=request.cookies.get("Admin-Jwt_token")
        print("Token in adminrole protected route:", admintoken)
        if not admintoken:
            return redirect('/')
        try:
            decryptjwt=cipher.decrypt(admintoken.encode()).decode()
            print("decryptToken in protected route:", decryptjwt)
            claim=decode_token(decryptjwt)
            if claim.get("role")=="Admin":
                jsonify("Admin is allowed")
                return func(*args, **kwargs) 
            else:
                return redirect("/")
        except Exception as e:
            print("there is an error can't go to wrapper functions",e)    
    return wrapper
        
def normaluser(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        usertoken=request.cookies.get("user-token")
        if not usertoken:
            return redirect('/')
        try:
            decryptjwt=cipher.decrypt(usertoken.encode()).decode()
            claim=decode_token(decryptjwt)
            if claim.get("role")=="User":
                jsonify("normal usrs allowed")
                return func(*args,**kwargs)
            else:
                return redirect("/")
        except Exception as e:
            print("some error occured can't go to wrapper fucntion",e)
    return wrapper
    
def normal_admin_both(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        usertoken = request.cookies.get("user-token")  
        admintoken = request.cookies.get("Admin-Jwt_token")  

        if not usertoken and not admintoken:
            return redirect("/")

        try:
    
            if usertoken:
                decrypt_usertoken = cipher.decrypt(usertoken.encode()).decode()
                claim_user = decode_token(decrypt_usertoken)
                user_role = claim_user.get("role")

                if user_role in ["User", "Admin"]:
                    return func(*args, **kwargs)  

            if admintoken:
                decrypt_admintoken = cipher.decrypt(admintoken.encode()).decode()
                claim_admin = decode_token(decrypt_admintoken)
                admin_role = claim_admin.get("role")

                if admin_role in ["User", "Admin"]:
                    return func(*args, **kwargs) 

        except Exception as e:
            print(f"Token decryption or validation error: {e}")
            return redirect("/")  

    
        return redirect("/")

    return wrapper
