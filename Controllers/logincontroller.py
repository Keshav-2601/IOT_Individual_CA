from flask import Flask
from flask import Blueprint, render_template,request,Response ,redirect,flash,jsonify
from Middlewares import Passwordhashing
from Models.Air_quality_Modal import Air_Quality
from Repositories import UserDB
from Repositories.Admin_air_repo import admin_air_repo
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
import datetime
login_blueprint=Blueprint('login',__name__)

@login_blueprint.route('/',methods=["GET","POST"])
def loginpage():
    data={
        "email":request.form.get('email'),
        "password":request.form.get('password'),
    }
    Result=UserDB.mysqlrepository.Logindata(data)
    if(Result):
        jwttoken=create_access_token(identity=data["email"],additional_claims={"role":"User"},expires_delta=datetime.timedelta(days=7))
        if(jwttoken):
            print("Successfully login",jwttoken)
            response = redirect('/homepage')
            response.set_cookie('access_token', jwttoken, httponly=True)  # Secure token storage
            return response
            
    else:
        print(jsonify({"error": "Token generation failed"}), 500)
        print("Invalid credential")
        redirect('/')
    return render_template("Login.html")

@login_blueprint.route("/createlogin",methods=["GET","POST"])
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

@login_blueprint.route("/airquality",methods=["GET","POST"])
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

@login_blueprint.route("/adminpage",methods=["GET","POST"])
def adminpage():
    airqualitydata=Air_Quality.query.all()##to get entire data about air Quality.
    return render_template("adminpage.html",data=airqualitydata)

@login_blueprint.route("/adminlogin",methods=["GET","POST"])
def adminlogin():
    data={
        "email":request.form.get("email"),
        "password":request.form.get("password")
    }
    result=admin_air_repo.adminloginDB(data)
    print("Result is ",result)
    if(result):
        adminjwttoken=create_access_token(identity=data["email"],additional_claims={"role":"Admin"},expires_delta=datetime.timedelta(days=7))
        if(adminjwttoken):
            
           print("successfully enteres as admin")
           response= redirect("/adminpage")
           response.set_cookie("Admin-Jwt_token",adminjwttoken,httponly=True)
           return response
    else:
        print(jsonify("error can't create jwt as well login as well as a admin"))
        print("Invalid Credential!! ")
    return render_template("Adminlogin.html")

    