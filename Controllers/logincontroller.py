from flask import Flask
from flask import Blueprint, render_template,request,Response ,redirect,flash
from Middlewares import Passwordhashing
from Repositories import UserDB
login_blueprint=Blueprint('login',__name__)

@login_blueprint.route('/',methods=["POST","GET"])
def loginpage():
    data={
        "email":request.form.get('email'),
        "password":request.form.get('password'),
    }
    Result=UserDB.mysqlrepository.Logindata(data)
    if(Result):
        print("Successfully login")
        redirect('/homepage')
    else:
        print("Invalid credential")
        redirect('/')
    return render_template("Login.html")

@login_blueprint.route("/createlogin",methods=["POST","GET"])
def creatlogin():
    if request.method == "POST":
        password = request.form.get("password")
        hashed_password = Passwordhashing.encrypt(password)  # Hash the password

        data = {
            "username": request.form.get("username"),
            "email": request.form.get("Email"),
            "Address": request.form.get("Address"),
            "password": hashed_password
        }

        result = UserDB.MySQLRepository.insertdata(data)  # Call the repository method

        if result:
            flash("Data added successfully!", "success")
            return redirect("/")
        else:
            flash("Some error occurred. Can't save to the repository.", "danger")
        
    return render_template("CreateLogin.html")