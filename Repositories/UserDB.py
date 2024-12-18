from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Models.UserModal import User,db
from Middlewares import encrypt,decrypt
class mysqlrepository:
    @staticmethod 
    def insertdata(data):
        new_User= User(name=data["username"],email=data["email"],address=data["Address"],password=data["password"])
        try:
            db.session.add(new_User)
            db.session.commit()
            print("Data addede successfully!")
            return True
        except Exception as e:
            db.session.rollback()     
            print(f"Error inserting data: {e}")
            return False
    @staticmethod
    def Logindata(data):
        try:
            input_email = data["email"]
            input_password = data["password"]
            # Query the database for the user with the given email
            user = User.query.filter_by(email=input_email).first()
            if user:
                if decrypt(user.password, input_password):
                    print("Login successful!")
                    return True
                else:
                    print("Incorrect password.")
                    return False
            else:
                print("User not found.")
                return False

        except Exception as e:
            print(f"Error during login: {e}")
            return False
            
            
       
    
    