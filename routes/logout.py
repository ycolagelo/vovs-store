from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session

def make_logout_route(app):
    @app.route("/logout")
    def logout():

    # Forget any user_id
        session.clear()

    # Redirect user to login form
        return redirect("/")
