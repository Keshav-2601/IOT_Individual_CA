from flask import Flask
from flask import Blueprint, render_template,request,Response ,redirect
from Middlewares import Passwordhashing
from Repositories import UserDB
login_blueprint=Blueprint('login',__name__)

@login_blueprint.route('/',methods=["POST","GET"])
def loginpage():
    username=request.form.get('username');
    password=request.form.get('password');
    return render_template("Login.html")

@login_blueprint.route("/createlogin",methods=["POST","GET"])
def creatlogin():
    password=request.form.get("password");
    Hashed_password=Passwordhashing.encrypt(password)## calling middleware here that will return hashed passwrod;
    
    data={
        "username":request.form.get("username"),
        "email":request.form.get("Email"),
        "Address":request.form.get("Address"),
        "password":Hashed_password
    }
    Result=UserDB.mysqlrepository.insertdata(data)## using reposirtory method directly as it's static.
    if(Result):
        print("Data addes successfully!!")
    else:
        print("Some error occured can't go to repository")
    
    return render_template("CreateLogin.html")
