from flask import jsonify,redirect
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from functools import wraps

def adminrole(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claim=get_jwt()
        if claim.get("role")=="Admin":
            jsonify("admin is allowed")
            return func(*args, **kwargs)
        else:
            print("Forbidden")
            return redirect("/")
    return wrapper
        
def normaluser(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        verify_jwt_in_request()
        claim=get_jwt()
        if claim.get("role")=="User":
            return jsonify("USer allowed")
        else:
            return redirect("/")
    return wrapper
    
        
