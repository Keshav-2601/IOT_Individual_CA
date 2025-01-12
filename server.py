from flask import Flask
from Controllers.logincontroller import login_blueprint
from Database.db import db
from Models.UserModal import User
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv
load_dotenv()

encryption_key = Fernet.generate_key()
encryption_key=os.getenv("ENCRYPTION_KEY")
print("Loaded encryption key from server side :", encryption_key)

cipher = Fernet(encryption_key)

server = Flask(__name__, template_folder="static/Views")

# server.config["SQLALCHEMY_DATABASE_URI"] = (
#     "mariadb+mariadbconnector://Keshav:password123@127.0.0.1:3306/iot_air_quality"
# )
server.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mariadb+mariadbconnector://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@"
    f"{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
server.config["JWT_SECRET_KEY"]=os.getenv("JWT_KEY")

jwt = JWTManager(server)
server.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(server)

migrate = Migrate(server, db)

server.register_blueprint(login_blueprint)

if __name__ == "__main__":
    print("Starting the flask server")
    server.run(debug=True, port=5001)
