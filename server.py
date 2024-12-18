from flask import Flask
from Controllers.logincontroller import login_blueprint 
from flask_sqlalchemy import SQLAlchemy
from Models.UserModal import db, User

server=Flask(__name__,template_folder="Views")


server.config['SQLALCHEMY_DATABASE_URI']='mysql+mysqlconnector://Keshav:password123@localhost/iot_air_quality'
server.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False # it will track changes in ur db so it should be flase to avid unnesscary warning.

db.init_app(server)

server.register_blueprint(login_blueprint)##so basically server goes to contorller ogin_blueprint from bluprint it goes to router("/") then shows view


with server.app_context():
    db.create_all() 
    
if __name__ == "__main__":
    server.run(debug=True)