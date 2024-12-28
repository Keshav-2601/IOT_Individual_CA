from flask_sqlalchemy import SQLAlchemy
from Database.db import db

class User(db.Model):
    __tablename__="Users_Table"
    id=db.Column(db.Integer ,nullable=False, primary_key=True,autoincrement=True)
    name=db.Column(db.String(200),nullable=False,)
    email=db.Column(db.String(20),nullable=False,unique=True)
    address=db.Column(db.String(20),nullable=False,)
    password=db.Column(db.String(100),nullable=False,)

