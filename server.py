from flask import Flask
from Controllers.logincontroller import login_blueprint 
server=Flask(__name__,template_folder="Views")


server.register_blueprint(login_blueprint)##so basically server goes to contorller ogin_blueprint from bluprint it goes to router("/") then shows view

if __name__ == "__main__":
    server.run(debug=True)