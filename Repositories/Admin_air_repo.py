from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from Models.Air_quality_Modal import Air_Quality
from Models.UserModal import db


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