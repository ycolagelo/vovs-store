from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
import datetime


def make_register_route(app):
    @app.route("/register", methods=["GET", "POST"])
    def register():
        db = SQL("sqlite:///program.db")

        session.clear()

        if request.method == "POST":
            if not request.form.get("username"):
                return ("must provide username",)

            rows = db.execute("SELECT * FROM user WHERE username=:username",
                              username=request.form.get("username"))

            if len(rows) == 1:
                return("Username already in use. Please select a nother username.")

            username = request.form.get("username")

            if not request.form.get("password"):
                return("Please select a password")
            password = request.form.get("password")

            if not request.form.get("confirm_password"):
                return("please confirm password")
            conf_password = request.form.get("confirm_password")

            if password != conf_password:
                return ("Passwords do not match")

            hash_password = generate_password_hash(
                request.form.get("password"))

            rows1 = db.execute(
                "SELECT email FROM user WHERE email=:email", email=request.form.get("email"))

            email = request.form.get("email")
            tel = request.form.get("tel")

            db.execute("INSERT INTO user (username, hash, email, phone, created_date) VALUES (:username, :hash_password, :email, :tel, datetime('now'))",
                       username=username, hash_password=hash_password, email=email, tel=tel)

            return redirect("/login")

        else:
            return render_template("register.html")
