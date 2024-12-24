from flask import Flask
from Controllers.logincontroller import login_blueprint
from flask_sqlalchemy import SQLAlchemy
from Models.UserModal import db, User
from flask_migrate import Migrate

server = Flask(__name__, template_folder="Views")

server.config["SQLALCHEMY_DATABASE_URI"] = (
    "mariadb+mariadbconnector://Keshav:password123@localhost/iot_air_quality"
)


server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(server)
migrate = Migrate(server, db)
with server.app_context():
    db.create_all()  # Create tables if they don't exist

server.register_blueprint(login_blueprint)

if __name__ == "__main__":
    print("Starting the flask server")
    server.run(debug=True, port=5001)
