from flask import Flask
from flask import Blueprint, render_template

login_blueprint=Blueprint('login',__name__)

@login_blueprint.route('/')
def loginpage():
    return render_template("Login.html")

@login_blueprint.route("/createlogin")
def creatlogin():
    return render_template("CreateLogin.html")
