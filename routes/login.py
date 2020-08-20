

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

db = SQL("sqlite:///program.db")


def make_login_route(app):
    @app.route("/login", methods=["GET", "POST"])
    def login():
        session.clear()
        if request.method == "POST":
            if not request.form.get("username"):
                return("Please provide username")
            username = request.form.get("username")

            if not request.form.get("password"):
                return("Please provide password")
            password = request.form.get("Password")

            rows = db.execute(
                "SELECT * FROM user WHERE username=:username", username=username)

            if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
                return ("invalid username and or Password")

                # Remember which user has logged in
            session["user_id"] = rows[0]["id"]
            session["username"] = rows[0]["username"]

            return redirect("/")
        else:
            return render_template("login.html")
