from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Models.Air_quality_Modal import Air_Quality 
from Models.UserModal import User
from Middlewares.Passwordhashing import decrypt
from Database.db import db
from dotenv import load_dotenv
import os

load_dotenv()

class admin_air_repo:
    @staticmethod
    def air_quality_data(data):
        new_AirQuality = Air_Quality(
            para1=data["parameter1"], para2=data["parameter2"], para3=data["parameter3"]
        )
        try:
            db.session.add(new_AirQuality)
            db.session.commit()
            print(" Air Data added successfully!")
            return True
        except Exception as e:
            db.session.rollback()
            print(f"Error inserting data: {e}")
            return False
    @staticmethod
    def adminloginDB(data):
        try:
            inputemail = data.get("email")  
            password = data.get("password")  
            print("inputemail :",inputemail)
            print("checking what's ging wrong?? ",password)
        
            admin_email = os.getenv("ADMIN_EMAIL")
            admin_password = os.getenv("ADMIN_PASSWORD")
        
            if inputemail == admin_email and password == admin_password:
                print("Admin has logged in successfully!")
                return True
            else:
                print("Invalid credentials")
                return False
        except Exception as e:
            print(f"Error during login: {e}")
            return False
            
        
            
            