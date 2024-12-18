from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy(); ## creating the instance right.

class User(db.Model):
    __tablename__="Users_Table"
    id=db.Column(db.integer ,nullable=False, primary_Key=True)
    name=db.Column(db.String(200),nullable=False,)
    Email=db.Column(db.String(20),nullable=False,unique=True)
    address=db.Column(db.String(20),nullable=False,)
    password=db.Column(db.Sting(40),nullable=False,)

