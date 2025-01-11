from flask_sqlalchemy import SQLAlchemy
from Database.db import db

class Air_Quality(db.Model):
    __tablename__="Air_Quality_Table"
    id=db.Column(db.Integer ,nullable=False, primary_key=True,autoincrement=True)
    para1=db.Column(db.Integer,nullable=False,)
    para2=db.Column(db.Integer,nullable=False)
    para3=db.Column(db.Integer,nullable=False,)
    

    def to_dict(self):
        return {
            "id": self.id,
            "para1": self.para1,
            "para2": self.para2,
            "para3": self.para3
        }