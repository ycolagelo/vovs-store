from helpers.login_required import login_required
from flask import Flask, flash, jsonify, redirect, render_template, request, session, abort


def make_checkout_route(app):
    @app.route("/checkout")
    @login_required
    def checkout():
        # return("yes")

        return render_template("checkout.html")
