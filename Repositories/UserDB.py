from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Models.UserModal import User, db
from sqlalchemy import func
from Middlewares.Passwordhashing import decrypt

class mysqlrepository:
    @staticmethod
    def insertdata(data):
        new_User = User(
            name=data["username"],
            email=data["email"],
            address=data["Address"],
            password=data["password"]
        )
        try:
            db.session.add(new_User)
            db.session.commit()
            print("Data added successfully!")
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error inserting data: {e}")
            return False

    @staticmethod
    def Logindata(data):
        try:
            input_email = data['email']
            if input_email:
                print("input_email: ", input_email)
                input_email = input_email.strip()
            else:
                print("Email is missing in the form data.")
                return False

            input_password = data['password']
            input_password=input_password.encode("utf-8")
            #print("input_password: ", input_password)
            if not input_password:
                print("Password is missing in the form data.")
                return False

            user = User.query.filter(User.email == input_email).first()
            if user:
                print("Return value from filter:", user.email)
               
                print(" Before User password from DB:")
                
                hashed_password = user.password.encode("utf-8")
               
                print("After User password from DB:", type(hashed_password))
                print("Input password:", type(input_password))
                
                if decrypt(hashed_password, input_password):
                    print("Keshav Login successful!")
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
