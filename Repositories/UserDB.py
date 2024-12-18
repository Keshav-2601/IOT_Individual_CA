from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Models.UserModal import User,db
class mysqlrepository:
    @staticmethod 
    def insertdata(data):
        new_User= User(1,data.name,data.email,data.Address,data.password)
        try:
            db.session.add(new_User)
            db.session.commit()
            print("Data addede successfully!")
            return True
        except Exception as e:
            db.session.rollback()     
            print(f"Error inserting data: {e}")
            return False
        
            
            
       
    
    