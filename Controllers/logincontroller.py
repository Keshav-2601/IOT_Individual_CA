from flask import Flask
from flask import Blueprint, render_template,request,Response ,redirect,flash
from Middlewares import Passwordhashing
from Repositories import UserDB
from Repositories.Admin_air_repo import admin_air_repo
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
        return redirect('/homepage')
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

        result = UserDB.mysqlrepository.insertdata(data)  # Call the repository method

        if result:
            print("Data added successfully!", "success")
            return redirect("/")
        else:
            print("Some error occurred. Can't save to the repository.", "danger")
        
    return render_template("CreateLogin.html")
@login_blueprint.route("/homepage")
def homepage():
    return render_template("Homepage.html")

@login_blueprint.route("/airquality",methods=["POST","GET"])
def airqualitypage():
    data={
        "parameter1":request.form.get("para1"),
        "parameter2":request.form.get("para2"),
        "parameter3":request.form.get("para3"),
    }
    Result=admin_air_repo.air_quality_data(data)
    if(Result):
        print("succesfully air data added to DB!")
    else:
        print("Not able to add data to DB")
    
    return render_template("airqualitypage.html")

@login_blueprint.route("/adminpage")
def adminpage():
    return render_template("adminpage.html")

@login_blueprint.route("/adminlogin")
def adminlogin():
    return render_template("Adminlogin.html")

    