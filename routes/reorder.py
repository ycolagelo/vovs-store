from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from helpers.product_helpers import get_products, get_purchased_products
from helpers.login_required import login_required


def make_reorder_route(app):
    @app.route("/reorder")
    @login_required
    def reorder():
        rows = get_purchased_products(session["user_id"])

        return render_template("/reorder.html", rows=rows)
