import requests
import urllib.parse

from cs50 import SQL
from flask import render_template, session, request, redirect
import datetime
from werkzeug.security import check_password_hash, generate_password_hash
from login_required import login_required

db = SQL("sqlite:///program.db")

def make_change_password_route(app):
     @app.route("/change_password", methods=["GET", "POST"])
     @login_required
     def change_password():

        if request.method == "POST":
            if not request.form.get("password"):
                return("must provide previous passowrd")
            password=request.form.get("password")
            hashed_password= generate_password_hash(password)

            if not request.form.get("newPassword"):
                return("must provide new password")
            newPassword=request.form.get("newPassword")
            hashed_newPassword =password = generate_password_hash(newPassword)

            if len(newPassword) < 6:
                return("passowrd should have 6 characters")

            has_number = False
            for char in newPassword:
                if char.isnumeric():
                    has_number = True

            if not has_number:
                return("must have one number in the password")

            if not request.form.get("confirmPassword"):
                return("must confirm password")
            confirmPassword=request.form.get("confirmPassword")
            #print(newPassword, confirmPassword)

            if newPassword != confirmPassword:
                return("passwords do not match")

            else:
                user_id = session["user_id"]

                rows = db.execute("SELECT hash from user WHERE id =:user_id", user_id=user_id)
                if len(rows) != 1:
                    return("username not found. Please register")

                else:
                    db.execute("UPDATE users SET hash=:hashed_newPassword WHERE id=:user_id", user_id=user_id,hashed_newPassword=hashed_newPassword)

                return redirect("/login")
        else:
            return render_template("change_password.html")





