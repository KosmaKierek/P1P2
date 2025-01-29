from flask import Flask, Blueprint, render_template, render_template_string, redirect, request, session, redirect, url_for
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from WarhinczykAI import WarhinczykAI
from Warhinczyk import Warhinczyk
import random
#import socket
#from flask_sqlalchemy import SQAlchemy

Menu = Flask(__name__)
Menu.register_blueprint(WarhinczykAI, url_prefix="")
Menu.register_blueprint(Warhinczyk, url_prefix="")
Scss(Menu)

Menu.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

Menu.secret_key = 'BAD_SECRET_KEY'

#db=SQAlchemy(Menu)

#server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.bind(('127.0.0.1', 5001))
#server.listen(5)

@Menu.route("/", methods=["POST","GET"])
def game():
    return render_template('menu.html')

@Menu.route("/help", methods=["POST","GET"])
def help():
    return render_template('instrukcja.html')

@Menu.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        user=request.form["nm"]
        session["user"]=user
        return render_template("menu.html")
    else:
        if "user" in session:
            return render_template("menu.html")
        return render_template("login.html")

@Menu.route("/user")
def user():
    if "user" in session:
        user=session["user"]
        return render_template("menu.html")
    else:
        return render_template("menu.html")
    
@Menu.route("/logout")
def logout():
    session.pop("user", None)
    return render_template("menu.html")

if __name__ in "__main__":
    Menu.run(debug=True, host='0.0.0.0')

#while True:
    #client, addr=server.accept()